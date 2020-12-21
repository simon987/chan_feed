import datetime
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from chan.helper import ChanHelper
from post_process import get_links_from_html_body


class Plus4ChanHelper(ChanHelper):

    def threads_url(self, board):
        return "%s%s/" % (self._base_url, board)

    def posts_url(self, board, thread):
        return "%s%s/t%d.html" % (self._base_url, board, self.item_id(thread))

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

        for threadEl in soup.find_all("section", class_="t", id=lambda x: x and x[1:].isnumeric()):

            omit = threadEl.find("a", class_="omittedbreakdown")

            threads.append({
                "id": int(threadEl.get("id")[1:]),
                "omit": int(omit.text.strip().split(" ")[1]) if omit else 0
            })

        for link in soup.find_all("a", href=lambda x: x):
            if link.text == "next":
                return threads, urljoin(r.url, link.get("href"))
        return threads, None

    @staticmethod
    def parse_thread(r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        thread_el = soup.find("section", class_="t")
        tid = int(thread_el.get("id")[1:])

        for post_el in soup.find_all("div", class_="p", id=lambda x: x and x[1:].isnumeric()):
            pid = int(post_el.get("id")[1:])
            if pid == tid:
                yield {
                    "id": tid,
                    "type": "thread",
                    "html": str(post_el),
                    "time": int(datetime.datetime.strptime(post_el.find("time", class_="date").text,
                                                           "%Y/%m/%d %H:%M:%S").timestamp())
                }
            else:
                yield {
                    "id": pid,
                    "type": "post",
                    "html": str(post_el),
                    "time": int(datetime.datetime.strptime(post_el.find("time", class_="date").text,
                                                           "%Y/%m/%d %H:%M:%S").timestamp()),
                    "parent": tid
                }
