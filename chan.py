import json

from post_process import get_links_from_body


class ChanHelper:
    def __init__(self, db_id, base_url, image_url, thread_path, image_path, boards):
        self.db_id = db_id
        self._base_url = base_url
        self._image_url = image_url
        self._thread_path = thread_path
        self._image_path = image_path
        self.boards = boards

    def image_url(self, board, tim, extension):
        return "%s%s%s%s%s" % (self._image_url, board, self._image_path, tim, extension)

    def threads_url(self, board):
        return "%s%s/threads.json" % (self._base_url, board)

    def posts_url(self, board, thread):
        return "%s%s%s%d.json" % (self._base_url, board, self._thread_path, thread)

    @staticmethod
    def item_id(item):
        return item["no"]

    def item_urls(self, item, board):
        urls = set()

        if "com" in item and item["com"]:
            urls.update(get_links_from_body(item["com"]))
        elif "sub" in item and item["sub"]:
            urls.update(get_links_from_body(item["sub"]))
        if "fsize" in item and item["fsize"]:
            urls.add(self.image_url(board, item["tim"], item["ext"]))

        return list(urls)

    @staticmethod
    def item_type(item):
        return "thread" if "sub" in item else "post"

    @staticmethod
    def thread_mtime(thread):
        return thread["last_modified"]

    @staticmethod
    def parse_threads_list(content):
        j = json.loads(content)
        for page in j:
            for thread in page["threads"]:
                yield thread

    @staticmethod
    def parse_thread(content):
        j = json.loads(content)
        return j["posts"]


class RussianChanHelper(ChanHelper):

    @staticmethod
    def item_id(item):
        return int(item["num"])

    @staticmethod
    def parse_threads_list(content):
        j = json.loads(content)
        return j["threads"]

    @staticmethod
    def parse_thread(content):
        j = json.loads(content)
        for thread in j["threads"]:
            for post in thread["posts"]:
                yield post

    @staticmethod
    def thread_mtime(thread):
        return thread["posts_count"]

    @staticmethod
    def item_type(item):
        return "thread" if "subject" in item and item["subject"] != "" else "post"

    def item_urls(self, item, board):
        urls = set()

        if "comment" in item and item["comment"]:
            urls.update(get_links_from_body(item["comment"]))
        elif "subject" in item and item["subject"]:
            urls.update(get_links_from_body(item["subject"]))

        if urls:
            print(list(urls))

        for file in item["files"]:
            urls.add(self._base_url + file["path"])

        return list(urls)


CHANS = {
    "4chan": ChanHelper(
        1,
        "https://a.4cdn.org/",
        "https://i.4cdn.org/",
        "/thread/",
        "/",
        [
            "a", "b", "c", "d", "e", "f", "g", "gif", "h", "hr",
            "k", "m", "o", "p", "r", "s", "t", "u", "v", "vg",
            "vr", "w", "wg", "i", "ic", "r9k", "s4s", "vip", "qa",
            "cm", "hm", "lgbt", "y", "3", "aco", "adv", "an", "asp",
            "bant", "biz", "cgl", "ck", "co", "diy", "fa", "fit",
            "gd", "hc", "his", "int", "jp", "lit", "mlp", "mu", "n",
            "news", "out", "po", "pol", "qst", "sci", "soc", "sp",
            "tg", "toy", "trv", "tv", "vp", "wsg", "wsr", "x"
        ]
    ),
    "lainchan": ChanHelper(
        2,
        "https://lainchan.org/",
        "https://lainchan.org/",
        "/res/",
        "/src/",
        [
            "λ", "diy", "sec", "tech", "inter", "lit", "music", "vis",
            "hum", "drg", "zzz", "layer" "q", "r", "cult", "psy",
            "mega", "random"
        ]
    ),
    "uboachan": ChanHelper(
        3,
        "https://uboachan.net/",
        "https://uboachan.net/",
        "/res/",
        "/src/",
        [
            "yn", "yndd", "fg", "yume", "o", "lit", "media", "og",
            "ig", "2", "ot", "hikki", "cc", "x", "sugg"
        ]
    ),
    "22chan": ChanHelper(
        4,
        "https://22chan.org/",
        "https://22chan.org/",
        "/res/",
        "/src/",
        [
            "a", "b", "f", "yu", "i", "k", "mu", "pol", "sewers",
            "sg", "t", "vg"
        ]
    ),
    "wizchan": ChanHelper(
        5,
        "https://wizchan.org/",
        "https://wizchan.org/",
        "/res/",
        "/src/",
        [
            "wiz", "dep", "hob", "lounge", "jp", "meta", "games", "music",
        ]
    ),
    "2chhk": RussianChanHelper(
        7,
        "https://2ch.hk/",
        "https://2ch.hk/",
        "/res/",
        "/src/",
        [
            "d", "b", "o", "soc", "media", "r", "api", "rf", "int",
            "po", "news", "hry", "au", "bi", "biz", "bo", "c", "em",
            "fa", "fiz", "fl", "ftb", "hh", "hi", "me", "mg", "mlp",
            "mo", "mov", "mu", "ne", "psy", "re",
            "sci", "sf", "sn", "sp", "spc", "tv", "un", "w", "wh",
            "wm", "wp", "zog", "de", "di", "diy", "mus", "pa", "p",
            "wrk", "trv", "gd", "hw", "mobi", "pr", "ra", "s", "t",
            "web", "bg", "cg", "gsg", "ruvn", "tes", "v", "vg", "wr",
            "a", "fd", "ja", "ma", "vn", "fg", "fur", "gg", "ga",
            "vape", "h", "ho", "hc", "e", "fet", "sex", "fag"
        ],
    )
}
