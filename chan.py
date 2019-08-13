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
            "a", "b", "f", "feels", "i", "k", "mu", "pol", "sewers",
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
    "1chan": ChanHelper(
        6,
        "https://www.1chan.net/",
        "https://www.1chan.net/",
        "/res/",
        "/src/",
        [
            "rails"
        ]
    )
}
