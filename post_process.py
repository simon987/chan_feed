from urllib.parse import urljoin

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


def post_process(item, board, helper):
    item["_v"] = 1.7
    item["_id"] = helper.item_unique_id(item, board)

    item["_board"] = board
    item["_chan"] = helper.db_id

    item["_urls"] = helper.item_urls(item, board)

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
