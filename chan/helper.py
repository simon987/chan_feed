from bs4 import BeautifulSoup


class ChanHelper:
    def __init__(self, db_id, base_url, image_url, thread_path, image_path, boards, rps):
        self.db_id = db_id
        self._base_url = base_url
        self._image_url = image_url
        self._thread_path = thread_path
        self._image_path = image_path
        self._boards = boards
        self.rps = rps

    def boards(self):
        return [b.replace("\\_", "_") for b in self._boards if not b.startswith("_")]

    def image_url(self, board, tim, extension):
        return "%s%s%s%s%s" % (self._image_url, board, self._image_path, tim, extension)

    def threads_url(self, board):
        return "%s%s/threads.json" % (self._base_url, board)

    def posts_url(self, board, thread):
        return "%s%s%s%d.json" % (self._base_url, board, self._thread_path, self.item_id(thread))

    def board_hash(self, board):
        return str((self._boards.index(board) + 1) * 10000)

    @staticmethod
    def item_id(item):
        raise NotImplementedError

    @staticmethod
    def item_mtime(item):
        raise NotImplementedError

    def item_unique_id(self, item, board):
        return int(self.board_hash(board) + str(self.item_id(item)))

    @staticmethod
    def thread_mtime(thread):
        raise NotImplementedError

    def item_urls(self, item, board):
        raise NotImplementedError

    @staticmethod
    def item_type(item):
        raise NotImplementedError

    @staticmethod
    def parse_threads_list(r):
        raise NotImplementedError

    @staticmethod
    def parse_thread(r):
        raise NotImplementedError

    @staticmethod
    def parse_thread(r):
        soup = BeautifulSoup(r.text, "html.parser")

        op_el = soup.find("div", attrs={"class": "innerOP"})
        yield {
            "id": int(soup.find("div", class_="opCell").get("id")),
            "type": "thread",
            "html": str(op_el),
        }

        for post_el in soup.find_all("div", class_="postCell"):
            yield {
                "id": int(post_el.get("id")),
                "type": "post",
                "html": str(post_el),
            }
