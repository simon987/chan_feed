import datetime
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from chan.desuchan_html import DesuChanHtmlChanHelper


class HispachanHtmlHelper(DesuChanHtmlChanHelper):

    def item_urls(self, item, board):
        return [
            x for
            x in super().item_urls(item, board)
            if "google.com" not in x and "javascript:" not in x
        ]

    def parse_threads_list(self, r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        threads = []

        for threadEl in soup.find_all("div", id=lambda tid: tid and tid[6:7].isdigit()):
            omit = threadEl.find("span", class_="typecount")
            threads.append({
                "id": int(re.search("thread([0-9]+)[a-zA-Z]*", threadEl.get("id")).group(1)),
                "omit": int(re.match(r"R:\s+([0-9]+).*", omit.text).group(1)) if omit else 0
            })

        next_url = soup.find("a", attrs={"rel": "next"})
        if next_url:
            return threads, urljoin(r.url, next_url.get("href"))
        return threads, None

    @staticmethod
    def parse_thread(r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        op_el = soup.find("div", class_="thread")

        posts = []
        for post_el in op_el.find_all("table", recursive=False):
            time = op_el.find("a", attrs={"data-date": lambda x: x}).get("data-date")
            posts.append({
                "id": int(post_el.find("td", attrs={"class", "reply"}).get("id")[5:]),
                "type": "post",
                "html": str(post_el),
                "time": int(datetime.datetime.strptime(time, "%d/%m/%y %H:%M UTC").timestamp())
            })
            post_el.decompose()

        time = op_el.find("a", attrs={"data-date": lambda x: x}).get("data-date")
        tid = int(op_el.find("a", attrs={"name": lambda x: x and x.isdigit()}).get("name"))
        yield {
            "id": tid,
            "type": "thread",
            "html": str(op_el),
            "time": int(datetime.datetime.strptime(time, "%d/%m/%y %H:%M UTC").timestamp())
        }

        for post in posts:
            post["parent"] = tid
            yield post
