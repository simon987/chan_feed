from chan.json import JsonChanHelper


class JsonKunChanHelper(JsonChanHelper):

    def image_url(self, board, tim, extension):
        return "%s%s%s%s" % (self._image_url, self._image_path, tim, extension)

