import json
import os
import time
import traceback
from queue import Queue
from threading import Thread

from hexlib.concurrency import queue_iter
from hexlib.db import VolatileBooleanState, VolatileState
from hexlib.env import get_web, get_redis
from hexlib.log import logger

from chan.chan import CHANS
from post_process import post_process

CHAN = os.environ.get("CF_CHAN", None)


class ChanScanner:
    def __init__(self, helper):
        self.web = get_web()
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


class ChanState:
    def __init__(self, prefix):
        self._posts = VolatileBooleanState(prefix)
        self._threads = VolatileState(prefix)

    def mark_visited(self, item: int):
        self._posts["posts"][item] = True

    def has_visited(self, item: int):
        return self._posts["posts"][item]

    def has_new_posts(self, thread, helper, board):
        mtime = helper.thread_mtime(thread)
        if mtime == -1:
            return True

        t = self._threads["threads"][helper.item_unique_id(thread, board)]

        return not t or helper.thread_mtime(thread) != t

    def mark_thread_as_visited(self, thread, helper, board):
        self._threads["threads"][helper.item_unique_id(thread, board)] = helper.thread_mtime(thread)


def publish_worker(queue: Queue, helper):
    for item, board in queue_iter(queue):
        try:
            publish(item, board, helper)
        except Exception as e:
            logger.error(str(e) + ": " + traceback.format_exc())


def publish(item, board, helper):
    post_process(item, board, helper)

    item_type = helper.item_type(item)
    routing_key = "%s.%s.%s" % (CHAN, item_type, board)

    message = json.dumps(item, separators=(',', ':'), ensure_ascii=False, sort_keys=True)
    rdb.lpush("arc.chan2." + routing_key, message)


if __name__ == "__main__":
    chan_helper = CHANS[CHAN]
    save_folder = os.environ.get("CF_SAVE_FOLDER", "")

    if save_folder:
        chan_helper.save_folder = save_folder

    state = ChanState(CHAN)
    rdb = get_redis()

    publish_q = Queue()
    publish_thread = Thread(target=publish_worker, args=(publish_q, chan_helper))
    publish_thread.setDaemon(True)
    publish_thread.start()

    s = ChanScanner(chan_helper)
    while True:
        try:
            for p, b in s.all_posts():
                publish_q.put((p, b))
        except KeyboardInterrupt as e:
            print("cleanup..")
            publish_q.put(None)
            break
