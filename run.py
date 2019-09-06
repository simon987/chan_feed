import datetime
import json
import sqlite3
import sys
import traceback
from datetime import datetime
from queue import Queue
from threading import Thread

import pika

import monitoring
from chan import CHANS
from post_process import post_process
from util import logger, Web

MONITORING = False


class ChanScanner:
    def __init__(self, helper):
        self.web = Web(monitoring if MONITORING else None)
        self.helper = helper
        self.state = ChanState()

    def _threads(self, board):
        r = self.web.get(self.helper.threads_url(board))
        if not r or r.status_code != 200:
            return []

        while True:
            threads, next_url = self.helper.parse_threads_list(r)
            for thread in threads:
                yield thread
            if not next_url:
                break
            r = self.web.get(next_url)
            if not r or r.status_code != 200:
                break

    def _fetch_posts(self, board, thread):
        r = self.web.get(self.helper.posts_url(board, thread))
        if r and r.status_code == 200:
            return self.helper.parse_thread(r)
        return []

    def _posts(self, board):
        for thread in self._threads(board):
            if self.state.has_new_posts(thread, self.helper, board):
                for post in self._fetch_posts(board, self.helper.item_id(thread)):
                    yield post
                self.state.mark_thread_as_visited(thread, self.helper, board)

    def all_posts(self):
        for board in self.helper.boards():
            for post in self._posts(board):
                yield post, board


def once(func):
    def wrapper(item, board, helper):
        if not state.has_visited(helper.item_unique_id(item, board), helper):
            func(item, board, helper)
            state.mark_visited(helper.item_unique_id(item, board), helper)

    return wrapper


class ChanState:
    def __init__(self):
        self._db = "state.db"

        with sqlite3.connect(self._db) as conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS posts "
                "("
                "   post INT,"
                "   ts INT DEFAULT (strftime('%s','now')),"
                "   chan INT,"
                "   PRIMARY KEY(post, chan)"
                ")"
            )
            conn.execute(
                "CREATE TABLE IF NOT EXISTS threads "
                "("
                "   thread INT,"
                "   last_modified INT,"
                "   ts INT DEFAULT (strftime('%s','now')),"
                "   chan INT,"
                "   PRIMARY KEY(thread, chan)"
                ")"
            )
            conn.execute("PRAGMA journal_mode=wal")
            conn.commit()

    def mark_visited(self, item: int, helper):
        with sqlite3.connect(self._db) as conn:
            conn.execute(
                "INSERT INTO posts (post, chan) VALUES (?,?)",
                (item, helper.db_id)
            )

    def has_visited(self, item: int, helper):
        with sqlite3.connect(self._db) as conn:
            cur = conn.cursor()
            cur.execute(
                "SELECT post FROM posts WHERE post=? AND chan=?",
                (item, helper.db_id)
            )
            return cur.fetchone() is not None

    def has_new_posts(self, thread, helper, board):
        mtime = helper.thread_mtime(thread)
        if mtime == -1:
            return True

        with sqlite3.connect(self._db, timeout=5000) as conn:
            cur = conn.cursor()
            cur.execute(
                "SELECT last_modified FROM threads WHERE thread=? AND chan=?",
                (helper.item_unique_id(thread, board), helper.db_id)
            )
            row = cur.fetchone()
            if not row or helper.thread_mtime(thread) != row[0]:
                return True
            return False

    def mark_thread_as_visited(self, thread, helper, board):
        with sqlite3.connect(self._db, timeout=5000) as conn:
            conn.execute(
                "INSERT INTO threads (thread, last_modified, chan) "
                "VALUES (?,?,?) "
                "ON CONFLICT (thread, chan) "
                "DO UPDATE SET last_modified=?",
                (helper.item_unique_id(thread, board), helper.thread_mtime(thread), helper.db_id,
                 helper.thread_mtime(thread))
            )
            conn.commit()


def publish_worker(queue: Queue, helper):
    while True:
        try:
            item, board = queue.get()
            publish(item, board, helper)

        except Exception as e:
            logger.error(str(e) + ": " + traceback.format_exc())
        finally:
            queue.task_done()


@once
def publish(item, board, helper):
    item_type = helper.item_type(item)
    post_process(item, board, helper)

    while True:
        try:
            chan_channel.basic_publish(
                exchange='chan',
                routing_key="%s.%s.%s" % (chan, item_type, board),
                body=json.dumps(item)
            )

            if MONITORING:
                distance = datetime.utcnow() - datetime.fromtimestamp(helper.item_mtime(item))
                monitoring.log([{
                    "measurement": chan,
                    "time": str(datetime.utcnow()),
                    "tags": {
                        "board": board
                    },
                    "fields": {
                        "distance": distance.total_seconds()
                    }
                }])
            break
        except Exception as e:
            logger.debug(traceback.format_exc())
            logger.error(str(e))
            connect()


def connect():
    global chan_channel
    rabbit = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    chan_channel = rabbit.channel()
    chan_channel.exchange_declare(exchange="chan", exchange_type="topic")


if __name__ == "__main__":

    if len(sys.argv) < 3:
        logger.error("You must specify RabbitMQ host & chan!")
        quit(1)

    rabbitmq_host = sys.argv[1]
    chan = sys.argv[2]
    chan_helper = CHANS[chan]

    if MONITORING:
        monitoring.init()
    state = ChanState()

    publish_q = Queue()
    publish_thread = Thread(target=publish_worker, args=(publish_q, chan_helper))
    publish_thread.start()

    connect()

    s = ChanScanner(chan_helper)
    while True:
        for p, b in s.all_posts():
            publish_q.put((p, b))
