import json
from datetime import datetime
from json import JSONDecodeError
from urllib.parse import urljoin

import cloudscraper

from chan.helper import ChanHelper
from util import logger


class LynxChanHelper(ChanHelper):
    """See https://gitgud.io/LynxChan/LynxChan/blob/master/doc/Json.txt"""

    def __init__(self, db_id, base_url, image_url, thread_path, image_path, boards, rps):
        super().__init__(db_id, base_url, image_url, thread_path, image_path, boards, rps)

        scraper = cloudscraper.create_scraper()
        self.get_method = scraper.get

    @staticmethod
    def item_id(item):
        return item["threadId"] if LynxChanHelper.item_type(item) == "thread" else item["postId"]

    @staticmethod
    def item_mtime(item):
        return datetime.fromisoformat(item["creation"]).timestamp()

    def item_urls(self, item, board):
        return [
            urljoin(self._base_url, im["path"])
            for im in item["files"]
        ] if "files" in item and item["files"] else []

    @staticmethod
    def item_type(item):
        return "thread" if "threadId" in item else "post"

    def threads_url(self, board):
        return "%s%s/1.json" % (self._base_url, board)

    @staticmethod
    def thread_mtime(thread):
        return (thread["ommitedPosts"] if "ommitedPosts" in thread else 0) + len(thread["posts"])

    @staticmethod
    def parse_threads_list(r):
        try:
            j = json.loads(r.content.decode('utf-8', 'ignore'))
            if len(j) == 0 or "threads" not in j:
                logger.warning("No threads in response for %s: %s" % (r.url, r.text,))
                return [], None
        except JSONDecodeError:
            logger.warning("JSONDecodeError for %s:" % (r.url,))
            logger.warning(r.text)
            return [], None

        next_page = None
        url = r.url[:r.url.rfind("?")] if "?" in r.url else r.url
        current_page = int(url[url.rfind("/") + 1:-5])
        if current_page < j["pageCount"]:
            next_page = urljoin(r.url, "%d.json" % (current_page + 1))

        return j["threads"], next_page

    @staticmethod
    def parse_thread(r):
        try:
            j = json.loads(r.content.decode('utf-8', 'ignore'))
        except JSONDecodeError:
            logger.warning("JSONDecodeError for %s:" % (r.url,))
            logger.warning(r.text)
            return []

        all_items = []
        for post in j["posts"]:
            post["_parent"] = j["threadId"]
            all_items.append(post)

        del j["posts"]
        all_items.append(j)

        return all_items
