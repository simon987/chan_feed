import datetime
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from chan.desuchan_html import DesuChanHtmlChanHelper


def _ro_datefmt(text):
    return re.sub(r"\s*[A-Z]\w{2,} ", "", text)


def _ts(time, r):
    # /int/ (International) board is in english...
    if "/int/" in r.url:
        return int(datetime.datetime.strptime(time, "\n%d-%m-%y (%a) %H:%M:%S\n").timestamp())
    return int(datetime.datetime.strptime(_ro_datefmt(time), "\n[%d.%m.%Y](%H:%M:%S)\n").timestamp())


class ChanonHtmlChanHelper(DesuChanHtmlChanHelper):

    def parse_threads_list(self, r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        threads = []

        for threadEl in soup.find_all("div", id=lambda tid: tid and re.match("thread([0-9]+)[a-zA-Z]*", tid)):
            omit = threadEl.find("span", class_="omittedposts")
            threads.append({
                "id": int(re.search("thread([0-9]+)[a-zA-Z]*", threadEl.get("id")).group(1)),
                "omit": int(omit.text.split("\n")[1]) if omit else 0
            })

        for form in soup.find_all("form"):
            next_button = form.find("input", attrs={"value": "Înainte"})
            if next_button and form.get("action") != "none":
                return threads, urljoin(self._base_url, form.get("action"))
        return threads, None

    @staticmethod
    def parse_thread(r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        thread_el = soup.find("div", id=lambda x: x and re.match("thread[0-9]+[a-zA-Z]*", x))

        for post_el in thread_el.find_all("table", recursive=False):
            *_, time = post_el.find("label").children
            yield {
                "id": int(post_el.find("td", attrs={"class", "reply"}).get("id")[5:]),
                "type": "post",
                "html": str(post_el),
                "time": _ts(time, r)
            }
            post_el.decompose()

        *_, time = thread_el.find("label").children
        yield {
            "id": int(re.search("thread([0-9]+)[a-zA-Z]*", thread_el.get("id")).group(1)),
            "type": "thread",
            "html": str(thread_el),
            "time": _ts(time, r)
        }
