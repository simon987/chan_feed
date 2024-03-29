import datetime
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from chan.desuchan_html import DesuChanHtmlChanHelper


class TgChanHtmlChanHelper(DesuChanHtmlChanHelper):

    def parse_threads_list(self, r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        threads = []

        for threadEl in soup.find_all("div", id=lambda tid: tid and tid[6:7].isdigit()):
            omit = threadEl.find("span", class_="omittedposts")
            threads.append({
                "id": int(re.search("thread([0-9]+)[a-zA-Z]*", threadEl.get("id")).group(1)),
                "omit": int(omit.text.split(" ")[0]) if omit else 0
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
        for post_el in op_el.find_all("table", recursive=False):
            *_, time = post_el.find("label").children

            if post_el.get("class") and "userdelete" in post_el.get("class"):
                continue

            posts.append({
                "id": int(post_el.find("td", attrs={"class", "reply"}).get("id")[5:]),
                "type": "post",
                "html": str(post_el),
                "time": int(datetime.datetime.strptime(time, "\n\n%Y/%m/%d(%a)%H:%M\n").timestamp())
            })
            post_el.decompose()

        *_, time = op_el.find("label").children
        tid = int(op_el.find("a", attrs={"name": lambda x: x and x.isdigit()}).get("name"))
        yield {
            "id": tid,
            "type": "thread",
            "html": str(op_el),
            "time": int(datetime.datetime.strptime(time, "\n\n%Y/%m/%d(%a)%H:%M\n").timestamp())
        }

        for post in posts:
            post["parent"] = tid
            yield post
