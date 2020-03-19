import hashlib
import os
import zlib
from io import BytesIO
from urllib.parse import urljoin, urlparse

import imagehash
from PIL import Image
from hexlib.imhash import b64hash

from util import logger

from hexlib.regex import HTML_HREF_RE, LINK_RE

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


def image_meta(url, url_idx, web, helper, board):
    r = web.get(url)
    if not r:
        logger.warning("Could not download image")
        return None
    buf = r.content

    sha1 = hashlib.sha1(buf).hexdigest()

    if helper.save_folder:
        path = os.path.join(helper.save_folder, str(helper.db_id), board)
        path += "/" + sha1[0]
        path += "/" + sha1[1:3]
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, sha1 + os.path.splitext(url)[1]), "wb") as out:
            out.write(buf)

    try:
        f = BytesIO(buf)
        im = Image.open(f)

        meta = {
            "url": url_idx,
            "size": len(buf),
            "width": im.width,
            "height": im.height,
            "sha1": sha1,
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
    item["_v"] = 1.6
    item["_id"] = helper.item_unique_id(item, board)

    item["_board"] = board
    item["_chan"] = helper.db_id

    item["_urls"] = helper.item_urls(item, board)

    item["_img"] = [image_meta(url, i, web, helper, board) for i, url in enumerate(item["_urls"]) if _is_image(url)]

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


def get_links_from_html_body(body, base_url):
    result = []
    for match in HTML_HREF_RE.finditer(body):
        url = match.group(1)
        result.append(urljoin(base_url, url))
    return result


def is_external(url):
    return not url.startswith(("#", "/"))
