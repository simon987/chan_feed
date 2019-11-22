import datetime
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from chan.helper import ChanHelper
from post_process import get_links_from_html_body


class Kev4PhpHelper(ChanHelper):

    def threads_url(self, board):
        return "%sboards/%s/" % (self._base_url, board)

    def posts_url(self, board, thread):
        return "%s%s?op=%d" % (self._base_url, self._thread_path, self.item_id(thread))

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
        return thread["omit"]

    @staticmethod
    def item_mtime(item):
        return item["time"]

    def parse_threads_list(self, r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        threads = []

        for threadEl in soup.find_all("p", class_="info"):
            threads.append({
                "id": int(threadEl.find("a").get("id")[len("expandButton"):]),
                "omit": int(threadEl.text.split(" ")[1])
            })

        current_page = int(r.url[-2:].strip("=")) if "&page=" in r.url else 0

        buttons = soup.find_all("button", class_="pageButton")
        for btn in buttons:
            if int(btn.text) == current_page + 1:
                return threads, urljoin(r.url, btn.parent.get("href"))
        return threads, None

    @staticmethod
    def parse_thread(r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        op_el = soup.find("div", class_="post op")
        if not op_el:
            return []
        tid = int(op_el.get("id"))
        yield {
            "id": tid,
            "type": "thread",
            "html": str(op_el),
            "time": int(datetime.datetime.strptime(op_el.find("span", class_="info").text,
                                                   " %d/%m/%Y %H:%M:%S").timestamp())
        }

        for post_el in soup.find_all("div", class_="post", id=lambda x: x and x.isnumeric()):
            if "op" in post_el.get("class"):
                continue
            yield {
                "id": int(post_el.get("id")),
                "type": "post",
                "html": str(post_el),
                "time": int(datetime.datetime.strptime(post_el.find("span", class_="info").text,
                                                       " %d/%m/%Y %H:%M:%S").timestamp()),
                "parent": tid
            }
