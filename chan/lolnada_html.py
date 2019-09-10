from urllib.parse import urljoin

from bs4 import BeautifulSoup
from dateutil import parser

from chan.helper import ChanHelper
from post_process import get_links_from_html_body


class LolNadaHtmlChanHelper(ChanHelper):

    def threads_url(self, board):
        return "%s%s/" % (self._base_url, board)

    def posts_url(self, board, thread):
        return "%s%s" % (self._base_url, thread["url"])

    @staticmethod
    def item_id(item):
        return item["id"]

    def item_urls(self, item, board):
        return [
            x for
            x in set(get_links_from_html_body(item["html"], self._base_url))
            if "google.com" not in x and "iqdb.org" not in x
        ]

    @staticmethod
    def item_type(item):
        return item["type"]

    @staticmethod
    def thread_mtime(thread):
        return thread["omit"]

    @staticmethod
    def item_mtime(item):
        return item["time"]

    def parse_threads_list(self, r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        threads = []

        for threadEl in soup.find_all("div", class_="hilo"):
            omit = threadEl.find("span", class_="omitted")
            threads.append({
                "id": int(threadEl.get("data-id")),
                "url": threadEl.find("a", class_="post_no").get("href"),
                "omit": int(omit.get("data-omitidos")) if omit else 0
            })

        for form in soup.find_all("form"):
            next_button = form.find("input", attrs={"value": "Siguiente"})
            if next_button and form.get("action") != "none":
                return threads, urljoin(self._base_url, form.get("action"))
        return threads, None

    @staticmethod
    def parse_thread(r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        op_el = soup.find("div", class_="hilo")
        for post_el in op_el.find_all("div", class_="post reply"):
            yield {
                "id": int(post_el.get("id")[6:]),
                "type": "post",
                "html": str(post_el),
                "time": int(parser.parse(post_el.find("time").get("datetime")).timestamp())
            }
            post_el.decompose()
        yield {
            "id": int(op_el.get("id")[5:]),
            "type": "thread",
            "html": str(op_el),
            "time": int(parser.parse(op_el.find("time").get("datetime")).timestamp())
        }
