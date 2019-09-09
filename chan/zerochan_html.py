import datetime
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from chan.doushio_html import DoushioHtmlChanHelper
from post_process import get_links_from_html_body


def _ru_datefmt(text):
    # For some reason, the dates are not compatible with ru_RU.UTF-8...

    return re.sub(r"\(.{3}\)", "", text) \
        .replace("Янв", "Jan") \
        .replace("Фев", "Feb") \
        .replace("Мар", "Mar") \
        .replace("Апр", "Apr") \
        .replace("Май", "May") \
        .replace("Июн", "Jun") \
        .replace("Июл", "Jul") \
        .replace("Авг", "Aug") \
        .replace("Сеп", "Sep") \
        .replace("Окт", "Oct") \
        .replace("Ноя", "Nov") \
        .replace("Дек", "Dec")


class ZerochanHtmlChanHelper(DoushioHtmlChanHelper):

    @staticmethod
    def thread_mtime(thread):
        return thread["omit"]

    def item_urls(self, item, board):
        return [
            x for
            x in set(get_links_from_html_body(item["html"], self._base_url))
            if "google.com" not in x and "whatanime.ga" not in x and "iqdb.org" not in x and "saucenao.com" not in x
        ]

    def parse_threads_list(self, r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        threads = []

        for threadEl in soup.find_all("section", attrs={"data-id": lambda x: x}):
            omit = threadEl.find("span", class_="omit")
            threads.append({
                "id": int(threadEl.get("data-id")),
                "omit": int(omit.get("data-omit")) if omit else 0
            })

        for a in soup.find_all("a"):
            if a.text == ">":
                return threads, urljoin(r.url, a.get("href"))
        return threads, None

    @staticmethod
    def parse_thread(r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        op_el = soup.find("section", attrs={"data-id": lambda x: x})

        for post_el in op_el.find_all("article", attrs={"data-id": lambda x: x}):
            yield {
                "id": int(post_el.get("data-id")),
                "type": "post",
                "html": str(post_el),
                "time": int(datetime.datetime.strptime(_ru_datefmt(post_el.find("time").text),
                                                       "%d %b %Y %H:%M").timestamp())
            }
            post_el.decompose()
        yield {
            "id": int(op_el.get("data-id")[1:]),
            "type": "thread",
            "html": str(op_el),
            "time": int(datetime.datetime.strptime(_ru_datefmt(op_el.find("time").text),
                                                   "%d %b %Y %H:%M").timestamp())
        }
