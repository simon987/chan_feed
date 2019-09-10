import json
from json import JSONDecodeError

from chan.helper import ChanHelper
from post_process import get_links_from_body
from util import logger


class RussianJsonChanHelper(ChanHelper):

    @staticmethod
    def item_id(item):
        return int(item["num"])

    @staticmethod
    def item_mtime(item):
        return item["timestamp"]

    @staticmethod
    def parse_threads_list(r):
        try:
            j = json.loads(r.content.decode('utf-8', 'ignore'))
        except JSONDecodeError:
            logger.warning("JSONDecodeError for %s:" % (r.url,))
            logger.warning(r.text)
            return [], None
        return j["threads"], None

    @staticmethod
    def parse_thread(r):
        try:
            j = json.loads(r.content.decode('utf-8', 'ignore'))
        except JSONDecodeError:
            logger.warning("JSONDecodeError for %s:" % (r.url,))
            logger.warning(r.text)
            return []
        for thread in j["threads"]:
            for post in thread["posts"]:
                yield post

    @staticmethod
    def thread_mtime(thread):
        return thread["posts_count"]

    @staticmethod
    def item_type(item):
        return "thread" if "subject" in item and item["subject"] != "" else "post"

    def item_urls(self, item, board):
        urls = set()

        if "comment" in item and item["comment"]:
            urls.update(get_links_from_body(item["comment"]))
        elif "subject" in item and item["subject"]:
            urls.update(get_links_from_body(item["subject"]))

        for file in item["files"]:
            urls.add(self._base_url.rstrip("/") + file["path"])

        return list(urls)
