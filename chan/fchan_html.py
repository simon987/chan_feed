import datetime
import _strptime
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from chan.desuchan_html import DesuChanHtmlChanHelper


class FChanHtmlChanHelper(DesuChanHtmlChanHelper):

    def parse_threads_list(self, r):
        soup = BeautifulSoup(r.text, "html.parser")

        threads = []

        for threadEl in soup.find_all("div", id=lambda tid: tid and re.match("thread[0-9]+", tid)):
            threads.append({
                "id": int(threadEl.get("id")[6:]),
            })

        next_url = None
        for a in soup.find_all("a"):
            if a.text == "Next":
                next_url = a
                break
        if next_url:
            return threads, urljoin(r.url, next_url.get("href"))
        return threads, None

    @staticmethod
    def parse_thread(r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        op_el = soup.find("div", id=lambda tid: tid and re.match("thread[0-9]+", tid))

        is_op = True

        for post_el in op_el.find_all("table", recursive=False):
            label = post_el.find("label")
            *_, time = label.children
            if is_op:
                yield {
                    "id": int(op_el.get("id")[6:]),
                    "type": "thread",
                    "html": str(post_el),
                    "time": int(datetime.datetime.strptime(time.strip(), "%y/%m/%d(%a)%H:%M").timestamp())
                }
                is_op = False
            else:
                yield {
                    "id": int(post_el.find("td", class_=lambda x: x and "reply" in x).get("id")[5:]),
                    "type": "post",
                    "html": str(post_el),
                    "time": int(datetime.datetime.strptime(time.strip(), "%y/%m/%d(%a)%H:%M").timestamp())
                }

