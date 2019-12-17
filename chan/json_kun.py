from vanwanet_scrape.scraper import Scraper

from chan.json import JsonChanHelper
from util import logger


class JsonKunChanHelper(JsonChanHelper):

    @staticmethod
    def item_type(item):
        return "thread" if item["resto"] == 0 else "post"

    def __init__(self, db_id, base_url, image_url, thread_path, image_path, boards, rps):
        super().__init__(db_id, base_url, image_url, thread_path, image_path, boards, rps)

        self._scraper = Scraper(
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Referer": "https://8kun.top/index.html"
            },
            domains=[
                "8kun.top",
                "media.8kun.top",
                "sys.8kun.net"
            ],
            logger=logger
        )

        self.get_method = self._scraper.get

    def image_url(self, board, tim, extension):
        return "%s%s%s%s" % (self._image_url, self._image_path, tim, extension)
