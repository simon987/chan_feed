import datetime
import json
import os
import sqlite3
import time
import traceback
from collections import defaultdict
from datetime import datetime
from queue import Queue
from threading import Thread

import pika
from hexlib.misc import buffered
from hexlib.monitoring import Monitoring

from chan.chan import CHANS
from post_process import post_process
from util import logger, Web

BYPASS_RPS = False

DBNAME = "chan_feed"
if os.environ.get("CF_INFLUXDB"):
    influxdb = Monitoring(DBNAME, host=os.environ.get("CF_INFLUXDB"), logger=logger, batch_size=100, flush_on_exit=True)
    MONITORING = True


class ChanScanner:
    def __init__(self, helper, proxy):
        self.web = Web(influxdb if MONITORING else None, rps=helper.rps, get_method=helper.get_method, proxy=proxy)
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
                for post in self._fetch_posts(board, thread):
                    yield post
                self.state.mark_thread_as_visited(thread, self.helper, board)

    def all_posts(self):
        for board in self.helper.boards():
            for post in self._posts(board):
                yield post, board


def once(func):
    def wrapper(item, board, helper, channel, web):
        if not state.has_visited(helper.item_unique_id(item, board), helper):
            func(item, board, helper, channel, web)
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
        with sqlite3.connect(self._db, timeout=10000) as conn:
            conn.execute(
                "INSERT INTO posts (post, chan) VALUES (?,?)",
                (item, helper.db_id)
            )

    def has_visited(self, item: int, helper):
        with sqlite3.connect(self._db, timeout=10000) as conn:
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

        with sqlite3.connect(self._db, timeout=10000) as conn:
            cur = conn.cursor()
            cur.execute(
                "SELECT last_modified, ts FROM threads WHERE thread=? AND chan=?",
                (helper.item_unique_id(thread, board), helper.db_id)
            )
            row = cur.fetchone()
            if not row or helper.thread_mtime(thread) != row[0] or row[1] + 86400 < int(time.time()):
                return True
            return False

    def mark_thread_as_visited(self, thread, helper, board):
        with sqlite3.connect(self._db, timeout=10000) as conn:
            conn.execute(
                "INSERT INTO threads (thread, last_modified, chan) "
                "VALUES (?,?,?) "
                "ON CONFLICT (thread, chan) "
                "DO UPDATE SET last_modified=?, ts=(strftime('%s','now'))",
                (helper.item_unique_id(thread, board), helper.thread_mtime(thread), helper.db_id,
                 helper.thread_mtime(thread))
            )
            conn.commit()


def publish_worker(queue: Queue, helper, p):
    channel = connect()
    web = Web(influxdb if MONITORING else None, rps=helper.rps, get_method=helper.get_method, proxy=p)

    while True:
        try:
            item, board = queue.get()
            if item is None:
                break
            publish(item, board, helper, channel, web)

        except Exception as e:
            logger.error(str(e) + ": " + traceback.format_exc())
        finally:
            queue.task_done()


@buffered(batch_size=150, flush_on_exit=True)
def _publish_buffered(items):
    if not items:
        return

    buckets = defaultdict(list)
    for item in items:
        buckets[item[1]].append(item)

    for bucket in buckets.values():
        channel, routing_key, _ = bucket[0]
        body = [item[2] for item in bucket]

        while True:
            try:
                channel.basic_publish(
                    exchange='chan',
                    routing_key=routing_key,
                    body=json.dumps(body, separators=(',', ':'), ensure_ascii=False, sort_keys=True)
                )
                logger.debug("RabbitMQ: published %d items" % len(body))
                break
            except Exception as e:
                # logger.debug(traceback.format_exc())
                logger.error(str(e))
                time.sleep(0.5)
                channel = connect()


@once
def publish(item, board, helper, channel, web):
    post_process(item, board, helper, web)

    item_type = helper.item_type(item)
    routing_key = "%s.%s.%s" % (chan, item_type, board)

    _publish_buffered([(channel, routing_key, item)])

    if MONITORING:
        distance = datetime.utcnow() - datetime.utcfromtimestamp(helper.item_mtime(item))
        influxdb.log([{
            "measurement": chan,
            "time": str(datetime.utcnow()),
            "tags": {
                "board": board
            },
            "fields": {
                "distance": distance.total_seconds()
            }
        }])


def connect():
    while True:
        try:
            rabbit = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
            channel = rabbit.channel()
            channel.exchange_declare(exchange="chan", exchange_type="topic")
            return channel
        except Exception as e:
            logger.error(str(e))
            time.sleep(0.5)
            pass


if __name__ == "__main__":

    rabbitmq_host = os.environ.get("CF_MQ_HOST", "localhost")
    chan = os.environ.get("CF_CHAN", None)
    chan_helper = CHANS[chan]

    proxy = None
    if os.environ.get("CF_PROXY"):
        proxy = os.environ.get("CF_PROXY")
        logger.info("Using proxy %s" % proxy)

    if BYPASS_RPS:
        chan_helper.rps = 10

    state = ChanState()

    publish_q = Queue()
    for _ in range(10):
        publish_thread = Thread(target=publish_worker, args=(publish_q, chan_helper, proxy))
        publish_thread.setDaemon(True)
        publish_thread.start()

    s = ChanScanner(chan_helper, proxy)
    while True:
        try:
            for p, b in s.all_posts():
                publish_q.put((p, b))
        except KeyboardInterrupt as e:
            for _ in range(5):
                publish_q.put((None, None))
            break
