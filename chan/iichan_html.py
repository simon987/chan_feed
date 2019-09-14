import datetime
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from chan.desuchan_html import DesuChanHtmlChanHelper
from util import logger


def _ts(text):
    time = re.sub(r"^\w{2} ", "", text.strip()) \
        .replace("января", "01") \
        .replace("февраля", "02") \
        .replace("марта", "03") \
        .replace("апреля", "04") \
        .replace("мая", "05") \
        .replace("июня", "06") \
        .replace("июля", "07") \
        .replace("августа", "08") \
        .replace("сентября", "09") \
        .replace("октября", "10") \
        .replace("ноября", "11") \
        .replace("декабря", "12")  \
        .replace("⑨", "9")
    # For some reason, some dates are fuzzed / in chinese
    try:
        return int(datetime.datetime.strptime(time, "%d %m %Y %H:%M:%S").timestamp())
    except Exception as e:
        logger.warning("Error during date parsing (iichan): " + str(e))
        return 0


class IichanHtmlChanHelper(DesuChanHtmlChanHelper):

    def parse_threads_list(self, r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        threads = []

        for threadEl in soup.find_all("div", id=lambda tid: tid and re.match("thread-([0-9]+)$", tid)):
            omit = threadEl.find("span", class_="omittedposts")
            threads.append({
                "id": int(re.search("thread-([0-9]+)", threadEl.get("id")).group(1)),
                "omit": int(omit.text.strip().split(" ")[1]) if omit else 0
            })

        for form in soup.find_all("form"):
            next_button = form.find("input", attrs={"value": "Далее"})
            if next_button and form.get("action") != "none":
                return threads, urljoin(self._base_url, form.get("action"))
        return threads, None

    @staticmethod
    def parse_thread(r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        thread_el = soup.find("div", id=lambda x: x and re.match("thread-[0-9]+", x))

        tid = int(re.search("thread-([0-9]+)[a-zA-Z]*", thread_el.get("id")).group(1))
        for post_el in thread_el.find_all("table", recursive=False):
            *_, time = post_el.find("label").children
            yield {
                "id": int(post_el.find("td", attrs={"class", "reply"}).get("id")[5:]),
                "type": "post",
                "html": str(post_el),
                "time": _ts(time),
                "parent": tid
            }
            post_el.decompose()

        *_, time = thread_el.find("label").children
        yield {
            "id": tid,
            "type": "thread",
            "html": str(thread_el),
            "time": _ts(time)
        }
