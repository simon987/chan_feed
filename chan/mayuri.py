import json
from json import JSONDecodeError

from chan.helper import ChanHelper
from post_process import get_links_from_body
from hexlib.log import logger


class MayuriChanHelper(ChanHelper):

    def __init__(self, db_id, base_url, image_url, boards):
        super().__init__(db_id, base_url, image_url, None, None, boards)

    @staticmethod
    def item_id(item):
        return item["id"]

    @staticmethod
    def item_mtime(item):
        return item["timestamp"]

    @staticmethod
    def thread_mtime(thread):
        return thread["replies_count"]

    def item_urls(self, item, board):
        urls = set()

        if "message" in item and item["message"]:
            urls.update(get_links_from_body(item["message"]))
        elif "subject" in item and item["subject"]:
            urls.update(get_links_from_body(item["subject"]))
        if item["files"]:
            for file in item["files"]:
                urls.add(self._image_url % file["storage"] + file["name"] + "." + file["ext"])

        return list(urls)

    @staticmethod
    def item_type(item):
        return "thread" if "replies_count" in item else "post"

    def parse_threads_list(self, r):
        try:
            j = json.loads(r.content.decode('utf-8', 'ignore'))
        except JSONDecodeError:
            logger.warning("JSONDecodeError for %s:" % (r.url,))
            logger.warning(r.text)
            return [], None
        if j["currentPage"] < j["totalPages"]:
            return j["data"], self._base_url + "boards/%d" % (j["currentPage"] + 1,)
        return j["data"]

    @staticmethod
    def parse_thread(r):
        try:
            j = json.loads(r.content.decode('utf-8', 'ignore'))
        except JSONDecodeError:
            logger.warning("JSONDecodeError for %s:" % (r.url,))
            logger.warning(r.text)
            return []

        thread = dict(j["data"])
        del thread["replies"]
        yield thread

        if j["data"]["replies"]:
            for post in j["data"]["replies"]:
                yield post

    def threads_url(self, board):
        return "%sboards/1" % (self._base_url,)

    def posts_url(self, board, thread):
        return "%sthreads/%d" % (self._base_url, self.item_id(thread))
