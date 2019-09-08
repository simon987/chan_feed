from chan.json import JsonChanHelper
from post_process import get_links_from_body


class AlokalJsonChanHelper(JsonChanHelper):

    def item_urls(self, item, board):
        urls = set()

        if "com" in item and item["com"]:
            urls.update(get_links_from_body(item["com"]))
        elif "sub" in item and item["sub"]:
            urls.update(get_links_from_body(item["sub"]))
        if "fsize" in item and item["fsize"]:
            urls.add(self._image_url + self._image_path + item["tim"] + "/" + str(item["no"]) + item["ext"])

        return list(urls)
