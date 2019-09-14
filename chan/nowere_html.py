import datetime
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from chan.desuchan_html import DesuChanHtmlChanHelper


def _ts(text):
    if re.search(r"^\s*20[1-9][0-9]/", text):
        return int(datetime.datetime.strptime(text.replace(" ", ""), "%Y/%m/%d(%a)%H:%M").timestamp())
    else:
        return int(datetime.datetime.strptime(text, " %d/%m/%y(%a)%H:%M").timestamp())


class NowereHtmlChanHelper(DesuChanHtmlChanHelper):

    def parse_threads_list(self, r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        threads = []

        for a in soup.find("form", id="delform")\
                .find_all("a", attrs={"name": lambda x: x and x.isdigit()}, recursive=False):

            omit = None
            for sibling in a.next_siblings:
                if sibling.name == "span" and sibling.get("class") == "omittedposts":
                    omit = sibling
                    break

            threads.append({
                "id": int(a.get("name")),
                "omit": int(omit.text.split(" ")[1]) if omit else 0
            })

        for form in soup.find_all("form"):
            next_button = form.find("input", attrs={"value": "Next"})
            if next_button and form.get("action") != "none":
                return threads, urljoin(self._base_url, form.get("action"))
        return threads, None

    @staticmethod
    def parse_thread(r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        op_el = soup.find("form", id="delform")

        posts = []
        for post_el in op_el.find_all("table", class_=lambda x: not x, recursive=False):
            *_, time = post_el.find("label").children
            posts.append({
                "id": int(post_el.find("td", attrs={"class", "reply"}).get("id")[5:]),
                "type": "post",
                "html": str(post_el),
                "time": _ts(time)
            })
            post_el.decompose()

        tid = int(op_el.find("a", attrs={"name": lambda x: x and x.isdigit()}).get("name"))
        *_, time = op_el.find("label").children
        yield {
            "id": tid,
            "type": "thread",
            "html": str(op_el),
            "time": _ts(time)
        }

        for post in posts:
            post["parent"] = tid
            yield post

