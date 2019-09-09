import datetime
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from chan.helper import ChanHelper
from post_process import get_links_from_html_body


class EndchanHtmlChanHelper(ChanHelper):

    def threads_url(self, board):
        return "%s%s/" % (self._base_url, board)

    def posts_url(self, board, thread):
        return "%s%s%s%d.html" % (self._base_url, board, self._thread_path, self.item_id(thread))

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

        for threadEl in soup.find_all("div", attrs={"class": "opCell"}):
            omit = threadEl.find("div", class_="labelOmission")
            threads.append({
                "id": int(threadEl.get("id")),
                "omit": int(omit.text.split(" ")[0]) if omit else 0
            })

        next_url = soup.find("a", attrs={"id": "linkNext"})
        if next_url:
            return threads, urljoin(r.url, next_url.get("href"))
        return threads, None

    @staticmethod
    def parse_thread(r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        op_el = soup.find("div", attrs={"class": "innerOP"})
        if not op_el:
            return []
        yield {
            "id": int(soup.find("div", class_="opCell").get("id")),
            "type": "thread",
            "html": str(op_el),
            "time": int(datetime.datetime.strptime(op_el.find("span", class_="labelCreated").text,
                                                   "%m/%d/%Y (%a) %H:%M:%S").timestamp())
        }

        for post_el in soup.find_all("div", class_="postCell"):
            yield {
                "id": int(post_el.get("id")),
                "type": "post",
                "html": str(post_el),
                "time": int(datetime.datetime.strptime(post_el.find("span", class_="labelCreated").text,
                                                       "%m/%d/%Y (%a) %H:%M:%S").timestamp())
            }
