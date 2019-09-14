import datetime

from bs4 import BeautifulSoup

from chan.helper import ChanHelper
from post_process import get_links_from_html_body


class DesuChanHtmlChanHelper(ChanHelper):

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

        for threadEl in soup.find_all("div", id=lambda tid: tid and tid[1:].isdigit()):
            omit = threadEl.find("span", class_="omittedposts")
            threads.append({
                "id": int(threadEl.get("id")[1:]),
                "omit": int(omit.text.split(" ")[0]) if omit else 0
            })

        for form in soup.find_all("form"):
            next_button = form.find("input", attrs={"value": "Next"})
            if next_button and form.get("action") != "none":
                return threads, self._base_url.rstrip("/") + form.get("action")
        return threads, None

    @staticmethod
    def parse_thread(r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        op_el = soup.find("div", id=lambda tid: tid and tid[1:].isdigit())

        tid = int(op_el.get("id")[1:])
        for post_el in op_el.find_all("table", recursive=False):
            *_, time = post_el.find("label").children
            yield {
                "id": int(post_el.find("td", attrs={"class", "reply"}).get("id")[5:]),
                "type": "post",
                "html": str(post_el),
                "time": int(datetime.datetime.strptime(time, "\n%y/%m/%d(%a)%H:%M").timestamp()),
                "parent": tid
            }
            post_el.decompose()

        *_, time = op_el.find("label").children
        yield {
            "id": tid,
            "type": "thread",
            "html": str(op_el),
            "time": int(datetime.datetime.strptime(time, "\n%y/%m/%d(%a)%H:%M").timestamp())
        }
