import re

LINK_RE = re.compile(r"(https?://[\w\-_.]+\.[a-z]{2,4}([^\s<'\"]*|$))")


def post_process(item, board, helper):
    item["_v"] = 1.2
    item["_id"] = helper.item_id(item)

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


def is_external(url):
    return not url.startswith(("#", "/"))
