import datetime
import re

from bs4 import BeautifulSoup

from chan.desuchan_html import DesuChanHtmlChanHelper


def _ru_datefmt(text):
    return re.sub(r"\(.{2}\)", "", text)


class Chan410HtmlChanHelper(DesuChanHtmlChanHelper):

    def parse_threads_list(self, r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        threads = []

        for threadEl in soup.find_all("div", id=lambda tid: tid and re.match("thread([0-9]+)[a-zA-Z]*", tid)):
            omit = threadEl.find("span", class_="omittedposts")
            threads.append({
                "id": int(re.search("thread([0-9]+)[a-zA-Z]*", threadEl.get("id")).group(1)),
                "omit": int(omit.text.split(" ")[1]) if omit else 0
            })

        return threads, None

    @staticmethod
    def parse_thread(r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        op_el = soup.find("form", id="delform")

        for post_el in op_el.find_all("div", class_="reply"):
            yield {
                "id": int(post_el.get("id")[5:]),
                "type": "post",
                "html": str(post_el),
                "time": int(datetime.datetime.strptime(_ru_datefmt(op_el.find("span", class_="time").text),
                                                       "%d.%m.%Y %H:%M:%S").timestamp())
            }
            post_el.decompose()

        yield {
            "id": int(op_el.find("a", attrs={"name": lambda x: x and x.isdigit()}).get("name")),
            "type": "thread",
            "html": str(op_el),
            "time": int(datetime.datetime.strptime(_ru_datefmt(op_el.find("span", class_="time").text),
                                                   "%d.%m.%Y %H:%M:%S").timestamp())
        }
