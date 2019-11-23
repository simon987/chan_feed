import datetime
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from hexlib.misc import strhash, signed64

from chan.helper import ChanHelper
from post_process import get_links_from_html_body
import re

SUBDOMAIN_PATTERN = re.compile("<([a-z]{3})>")

TIME_PATTERN = re.compile(r"([0-9]{2}/[0-9]{2}/[0-9]{2}\(.\)[0-9]{2}:[0-9]{2}:[0-9]{2})")


def _ja_datefmt(text):
    return re.sub(r"\(.\)", " ", text)


class Chan2Helper(ChanHelper):

    def _subdomain(self, board):
        m = SUBDOMAIN_PATTERN.search(board)
        if m:
            return m.group(1)
        return "www"

    def _trim(self, board):
        return SUBDOMAIN_PATTERN.sub("", board)

    def threads_url(self, board):
        return "%s/%s/" % (self._base_url.replace("<sub>", self._subdomain(board)), self._trim(board))

    def posts_url(self, board, thread):
        return "%s/%s%s%d.htm" % (self._base_url.replace("<sub>", self._subdomain(board)), self._trim(board), self._thread_path,
                                  self.item_id(thread))

    @staticmethod
    def item_id(item):
        return item["id"]

    def item_urls(self, item, board):
        return [url for url in
                set(get_links_from_html_body(item["html"], self._base_url.replace("<sub>", self._subdomain(board))))
                if "javascript" not in url
                ]

    @staticmethod
    def item_type(item):
        return item["type"]

    @staticmethod
    def thread_mtime(thread):
        return thread["omit"]

    @staticmethod
    def item_mtime(item):
        return item["time"]

    def parse_threads_list(self, r):
        soup = BeautifulSoup(r.content.decode('Shift_JIS', 'ignore'), "html.parser")

        threads = []

        for threadEl in soup.find_all("div", class_="thre"):
            omit = threadEl.find("font", color="#707070")
            # Example: <font color="#707070">レス9件省略。全て読むには返信ボタンを押してください。</font>

            threads.append({
                "id": int(threadEl.get("data-res")),
                "omit": signed64(strhash(omit.text)) if omit else 0
            })

        # for btn in soup.find_all("input"):
        #     if btn.get("value") == "次のページ":
        #         return threads, urljoin(r.url, btn.parent.get("action"))
        return threads, None

    @staticmethod
    def parse_thread(r):
        soup = BeautifulSoup(r.content.decode('Shift_JIS', 'ignore'), "html.parser")

        op_el = soup.find("div", class_="thre")
        tid = int(op_el.get("data-res"))

        for post_el in op_el.find_all("table", recursive=False):

            cnw = post_el.find("span", class_="cnw")
            if cnw:
                time = cnw.text.split(" ")[0]
            else:
                time = TIME_PATTERN.search(post_el.text).group(1)

            sod = post_el.find("a", id=lambda x: x and x[2:].isnumeric())
            if sod:
                # www
                id_str = sod.get("id")[2:]
            else:
                # may
                inputEl = post_el.find("input")
                if inputEl:
                    id_str = inputEl.get("name")
                else:
                    id_str = post_el.find("span", id=lambda x: x).get("id")[len("delcheck"):]

            yield {
                "id": int(id_str),
                "type": "post",
                "html": str(post_el),
                "time": int(datetime.datetime.strptime(_ja_datefmt(time), "%y/%m/%d %H:%M:%S").timestamp()),
                "parent": tid
            }
            post_el.decompose()

        cnw = op_el.find("span", class_="cnw")
        if cnw:
            # www
            time = cnw.text.split(" ")[0]
        else:
            # may
            time = TIME_PATTERN.search(op_el.text).group(1)
        yield {
            "id": tid,
            "type": "thread",
            "html": str(op_el),
            "time": int(datetime.datetime.strptime(_ja_datefmt(time), "%y/%m/%d %H:%M:%S").timestamp()),
        }
