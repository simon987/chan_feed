from json import JSONDecodeError
from urllib.parse import urljoin

import json

from hexlib.log import logger

from chan.helper import ChanHelper
from post_process import get_links_from_body


class JsonInfinityNextChanHelper(ChanHelper):

    def threads_url(self, board):
        return "%s%s/index.json" % (self._base_url, board)

    def posts_url(self, board, thread):
        return "%s%s%s%d.json" % (self._base_url, board, self._thread_path, thread["board_id"])

    @staticmethod
    def item_type(item):
        return "thread" if "reply_to" not in item or item["reply_to"] is None else "post"

    @staticmethod
    def item_id(item):
        return item["post_id"]

    @staticmethod
    def item_mtime(item):
        return item["updated_at"]

    def item_urls(self, item, board):
        urls = set()

        if "content_raw" in item and item["content_raw"]:
            urls.update(get_links_from_body(item["content_raw"]))
        if "attachments" in item and item["attachments"]:
            for attachment in item["attachments"]:
                urls.add(urljoin(self._image_url, attachment["file_url"]))

        return list(urls)

    @staticmethod
    def thread_mtime(thread):
        return thread["updated_at"]

    @staticmethod
    def parse_threads_list(r):
        try:
            j = json.loads(r.content.decode('utf-8', 'ignore'))
            if len(j) == 0 or "post_id" not in j[0]:
                logger.warning("No threads in response for %s: %s" % (r.url, r.text,))
                return [], None
        except JSONDecodeError:
            logger.warning("JSONDecodeError for %s:" % (r.url,))
            logger.warning(r.text)
            return [], None

        return j, None

    @staticmethod
    def parse_thread(r):
        try:
            j = json.loads(r.content.decode('utf-8', 'ignore'))
        except JSONDecodeError:
            logger.warning("JSONDecodeError for %s:" % (r.url,))
            logger.warning(r.text)
            return []
        thread = j.copy()
        del thread["replies"]
        yield thread
        for post in j["replies"]:
            yield post
