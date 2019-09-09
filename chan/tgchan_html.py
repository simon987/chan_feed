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
            threads.append({
                "id": int(re.search("thread([0-9]+)[a-zA-Z]*", threadEl.get("id")).group(1)),
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

        for post_el in op_el.find_all("table", recursive=False):
            label = post_el.find("label")
            *_, time = label.children
            yield {
                "id": int(post_el.find("td", attrs={"class", "reply"}).get("id")[5:]),
                "type": "post",
                "html": str(post_el),
                "time": int(datetime.datetime.strptime(time, "\n\n%Y/%m/%d(%a)%H:%M\n").timestamp())
            }
            post_el.decompose()

        *_, time = op_el.find("label").children
        yield {
            "id": int(op_el.find("a", attrs={"name": lambda x: x and x.isdigit()}).get("name")),
            "type": "thread",
            "html": str(op_el),
            "time": int(datetime.datetime.strptime(time, "\n\n%Y/%m/%d(%a)%H:%M\n").timestamp())
        }
