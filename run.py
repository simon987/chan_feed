import datetime
import json
import os
import time
import traceback
from datetime import datetime
from queue import Queue
from threading import Thread
import redis

from hexlib.db import VolatileBooleanState
from hexlib.monitoring import Monitoring

from chan.chan import CHANS
from post_process import post_process
from util import logger, Web

BYPASS_RPS = False

DBNAME = "chan_feed"
if os.environ.get("CF_INFLUXDB"):
    influxdb = Monitoring(DBNAME, host=os.environ.get("CF_INFLUXDB"), logger=logger, batch_size=100, flush_on_exit=True)
    MONITORING = True
else:
    MONITORING = False

REDIS_HOST = os.environ.get("CF_REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("CF_REDIS_PORT", 6379)
CHAN = os.environ.get("CF_CHAN", None)

ARC_LISTS = os.environ.get("CF_ARC_LISTS", "arc").split(",")


class ChanScanner:
    def __init__(self, helper, proxy):
        self.web = Web(influxdb if MONITORING else None, rps=helper.rps, get_method=helper.get_method, proxy=proxy)
        self.helper = helper
        self.state = state

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
    def wrapper(item, board, helper):
        if not state.has_visited(helper.item_unique_id(item, board)):
            func(item, board, helper)
            state.mark_visited(helper.item_unique_id(item, board))

    return wrapper


class ChanState:
    def __init__(self, prefix):
        self._state = VolatileBooleanState(prefix, host=REDIS_HOST, port=REDIS_PORT)
        print("redis host=" + REDIS_HOST)

    def mark_visited(self, item: int):
        self._state["posts"][item] = True

    def has_visited(self, item: int):
        return self._state["posts"][item] is not None

    def has_new_posts(self, thread, helper, board):
        mtime = helper.thread_mtime(thread)
        if mtime == -1:
            return True

        t = self._state["threads"][helper.item_unique_id(thread, board)]

        if not t or helper.thread_mtime(thread) != t["last_modified"] or t["ts"] + 86400 < int(time.time()):
            return True
        return False

    def mark_thread_as_visited(self, thread, helper, board):
        self._state["threads"][helper.item_unique_id(thread, board)] = {
            "ts": time.time(),
            "last_modified": helper.thread_mtime(thread)
        }


def publish_worker(queue: Queue, helper, p):
    while True:
        try:
            item, board = queue.get()
            if item is None:
                break
            publish(item, board, helper,)

        except Exception as e:
            logger.error(str(e) + ": " + traceback.format_exc())
        finally:
            queue.task_done()


@once
def publish(item, board, helper):
    post_process(item, board, helper)

    item_type = helper.item_type(item)
    routing_key = "%s.%s.%s" % (CHAN, item_type, board)

    message = json.dumps(item, separators=(',', ':'), ensure_ascii=False, sort_keys=True)
    rdb.publish("chan." + routing_key, message)
    for arc in ARC_LISTS:
        rdb.lpush(arc + ".chan." + routing_key, message)

    if MONITORING:
        distance = datetime.utcnow() - datetime.utcfromtimestamp(helper.item_mtime(item))
        influxdb.log([{
            "measurement": CHAN,
            "time": str(datetime.utcnow()),
            "tags": {
                "board": board
            },
            "fields": {
                "distance": distance.total_seconds()
            }
        }])


if __name__ == "__main__":
    chan_helper = CHANS[CHAN]
    save_folder = os.environ.get("CF_SAVE_FOLDER", "")

    if save_folder:
        chan_helper.save_folder = save_folder

    proxy = None
    if os.environ.get("CF_PROXY"):
        proxy = os.environ.get("CF_PROXY")
        logger.info("Using proxy %s" % proxy)

    if BYPASS_RPS:
        chan_helper.rps = 10

    state = ChanState(CHAN)
    rdb = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

    publish_q = Queue()
    for _ in range(3):
        publish_thread = Thread(target=publish_worker, args=(publish_q, chan_helper, proxy))
        publish_thread.setDaemon(True)
        publish_thread.start()

    s = ChanScanner(chan_helper, proxy)
    while True:
        try:
            for p, b in s.all_posts():
                publish_q.put((p, b))
        except KeyboardInterrupt as e:
            print("cleanup..")
            for _ in range(3):
                publish_q.put((None, None))
            break
