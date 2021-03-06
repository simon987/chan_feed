import datetime
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from chan.desuchan_html import DesuChanHtmlChanHelper


class FChanHtmlChanHelper(DesuChanHtmlChanHelper):

    def parse_threads_list(self, r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        threads = []

        for threadEl in soup.find_all("div", id=lambda tid: tid and re.match("thread[0-9]+", tid)):
            omit = threadEl.find("span", class_="omittedposts")
            threads.append({
                "id": int(threadEl.get("id")[6:]),
                "omit": int(omit.text.split(" ")[0]) if omit and omit.text else 0
            })

        for a in soup.find_all("a"):
            if a.text == "Next":
                return threads, urljoin(r.url, a.get("href"))
        return threads, None

    @staticmethod
    def parse_thread(r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        op_el = soup.find("div", id=lambda tid: tid and re.match("thread[0-9]+", tid))

        is_op = True

        posts = []
        tid = None
        for post_el in op_el.find_all("table", recursive=False):
            label = post_el.find("label")
            *_, time = label.children
            if is_op:
                tid = int(op_el.get("id")[6:])
                yield {
                    "id": tid,
                    "type": "thread",
                    "html": str(post_el),
                    "time": int(datetime.datetime.strptime(time.strip(), "%y/%m/%d(%a)%H:%M").timestamp())
                }
                is_op = False
            else:
                posts.append({
                    "id": int(post_el.find("td", class_=lambda x: x and "reply" in x).get("id")[5:]),
                    "type": "post",
                    "html": str(post_el),
                    "time": int(datetime.datetime.strptime(time.strip(), "%y/%m/%d(%a)%H:%M").timestamp())
                })

        for post in posts:
            post["parent"] = tid
            yield post

