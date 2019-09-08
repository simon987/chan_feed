import base64
import hashlib
import re
import zlib
from io import BytesIO

import imagehash
from PIL import Image

from util import logger

LINK_RE = re.compile(r"(https?://[\w\-_.]+\.[a-z]{2,4}([^\s<'\"]*|$))")

IMAGE_FILETYPES = (
    # :orig for twitter cdn
    '.jpg',
    '.jpg:orig',
    '.jpeg',
    '.jpeg:orig',
    '.png',
    '.png:orig',
    '.gif',
    '.gif:orig',
    '.tiff',
    '.bmp',
    '.webp'
)


def _is_image(url):
    return url.lower().endswith(IMAGE_FILETYPES)


def b64hash(imhash, bcount):
    return base64.b64encode(
        sum(1 << i for i, b in enumerate(imhash.hash.flatten()) if b).to_bytes(bcount, "big")
    ).decode("ascii")


def image_meta(url, url_idx, web):
    r = web.get(url)
    if not r:
        logger.warning("Could not download image")
        return None
    buf = r.content

    try:
        f = BytesIO(buf)
        im = Image.open(f)

        meta = {
            "url": url_idx,
            "size": len(buf),
            "width": im.width,
            "height": im.height,
            "sha1": hashlib.sha1(buf).hexdigest(),
            "md5": hashlib.md5(buf).hexdigest(),
            "crc32": format(zlib.crc32(buf), "x"),
            "dhash": b64hash(imagehash.dhash(im, hash_size=12), 18),
            "phash": b64hash(imagehash.phash(im, hash_size=12), 18),
            "ahash": b64hash(imagehash.average_hash(im, hash_size=12), 18),
            "whash": b64hash(imagehash.whash(im, hash_size=8), 8),
        }
    except Exception as e:
        logger.warning("exception during image post processing: " + str(e))
        return None

    del im, r, buf

    return meta


def post_process(item, board, helper, web):
    item["_v"] = 1.4
    item["_id"] = helper.item_unique_id(item, board)

    item["_board"] = board
    item["_chan"] = helper.db_id

    item["_urls"] = helper.item_urls(item, board)

    item["_img"] = [image_meta(url, i, web) for i, url in enumerate(item["_urls"]) if _is_image(url)]

    return item


def get_links_from_body(body):
    result = []

    body = body \
        .replace("<wbr>", "") \
        .replace("</s>", "") \
        .replace(" dot ", ".")

    for match in LINK_RE.finditer(body):
        url = match.group(1)
        if is_external(url):
            result.append(url)

    return result


def is_external(url):
    return not url.startswith(("#", "/"))
