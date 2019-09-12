import datetime
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from chan.desuchan_html import DesuChanHtmlChanHelper


def _trim_time(text):
    return re.sub(r"ID: \w+", "", text)


class Chan7HtmlChanHelper(DesuChanHtmlChanHelper):

    def parse_threads_list(self, r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        threads = []

        for threadEl in soup.find_all("div", class_="thread"):
            omit = threadEl.find("span", class_="omittedposts")
            threads.append({
                "id": int(re.search("thread_([0-9]+)_[a-zA-Z]*", threadEl.get("id")).group(1)),
                "omit": int(omit.text.split("\n")[1]) if omit else 0
            })

        for form in soup.find_all("form"):
            next_button = form.find("input", attrs={"value": "Next"})
            if next_button and form.get("action") != "none":
                return threads, urljoin(self._base_url, form.get("action"))
        return threads, None

    @staticmethod
    def parse_thread(r):
        soup = BeautifulSoup(r.content.decode('utf-8', 'ignore'), "html.parser")

        thread_el = soup.find("div", id=lambda x: x and re.match("thread_[0-9]+_[a-zA-Z]*", x))
        op_el = thread_el.find("div", class_="post")
        time = "".join(s for s in op_el.find("div", class_="post_header").contents if isinstance(s, str))
        yield {
            "id": int(op_el.get("id")),
            "type": "thread",
            "html": str(op_el),
            "time": int(datetime.datetime.strptime(_trim_time(time), "\n%y/%m/%d(%a)%H:%M\n").timestamp())
        }

        for post_el in thread_el.find_all("div", class_="reply"):
            time = "".join(s for s in op_el.find("div", class_="post_header").contents if isinstance(s, str))
            yield {
                "id": int(post_el.get("id")[6:]),
                "type": "post",
                "html": str(post_el),
                "time": int(datetime.datetime.strptime(_trim_time(time), "\n%y/%m/%d(%a)%H:%M\n").timestamp())
            }
