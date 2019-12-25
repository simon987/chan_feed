import json
from json import JSONDecodeError

from chan.helper import ChanHelper
from post_process import get_links_from_body
from util import logger


class JsonChanHelper(ChanHelper):

    @staticmethod
    def item_id(item):
        return item["no"]

    @staticmethod
    def item_mtime(item):
        return item["time"]

    def item_urls(self, item, board):
        urls = set()

        if "com" in item and item["com"]:
            urls.update(get_links_from_body(item["com"]))
        elif "sub" in item and item["sub"]:
            urls.update(get_links_from_body(item["sub"]))
        if "fsize" in item and item["fsize"]:
            urls.add(self.image_url(board, item["tim"], item["ext"]))

        return list(urls)

    @staticmethod
    def item_type(item):
        return "thread" if "sub" in item else "post"

    @staticmethod
    def thread_mtime(thread):
        return thread["last_modified"]

    @staticmethod
    def parse_threads_list(r):
        try:
            j = json.loads(r.content.decode('utf-8', 'ignore'))
            if len(j) == 0 or "threads" not in j[0]:
                logger.warning("No threads in response for %s: %s" % (r.url, r.text,))
                return [], None
        except JSONDecodeError:
            logger.warning("JSONDecodeError for %s:" % (r.url,))
            logger.warning(r.text)
            return [], None

        threads = []
        for page in j:
            for thread in page["threads"]:
                threads.append(thread)
        return threads, None

    @staticmethod
    def parse_thread(r):
        try:
            j = json.loads(r.content.decode('utf-8', 'ignore'))
        except JSONDecodeError:
            logger.warning("JSONDecodeError for %s:" % (r.url,))
            logger.warning(r.text)
            return []
        return j["posts"]
