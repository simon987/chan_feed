from urllib.parse import urljoin
from dateutil import parser

from bs4 import BeautifulSoup

from chan.helper import ChanHelper
from post_process import get_links_from_html_body


class DoushioHtmlChanHelper(ChanHelper):

    def threads_url(self, board):
        return "%s%s/" % (self._base_url, board)

    def posts_url(self, board, thread):
        return "%s%s/%d" % (self._base_url, board, thread)

    @staticmethod
    def item_id(item):
        return item["id"]

    def item_urls(self, item, board):
        return list(set(get_links_from_html_body(item["html"], self._base_url)))

    @staticmethod
    def item_type(item):
        return item["type"]

    @staticmethod
    def thread_mtime(thread):
        return -1

    @staticmethod
    def item_mtime(item):
        return item["time"]

    def parse_threads_list(self, r):
        soup = BeautifulSoup(r.text, "html.parser")

        threads = []

        for threadEl in soup.find_all("section"):
            threads.append({
                "id": int(threadEl.get("id")),
            })

        next_url = soup.find("link", attrs={"rel": "next"})
        if next_url:
            return threads, urljoin(r.url, next_url.get("href"))
        return threads, None

    @staticmethod
    def parse_thread(r):
        soup = BeautifulSoup(r.text, "html.parser")

        op_el = soup.find("section")
        for post_el in op_el.find_all("article"):
            yield {
                "id": int(post_el.get("id")),
                "type": "post",
                "html": str(post_el),
                "time": int(parser.parse(post_el.find("header").find("time").get("datetime")).timestamp())
            }
            post_el.decompose()
        yield {
            "id": int(op_el.get("id")),
            "type": "thread",
            "html": str(op_el),
            "time": int(parser.parse(op_el.find("header").find("time").get("datetime")).timestamp())
        }





