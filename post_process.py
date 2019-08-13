import re

LINK_RE = re.compile(r"(https?://[\w\-_.]+\.[a-z]{2,4}([^\s<'\"]*|$))")


def post_process(thing, board, helper):
    thing["v"] = 1.0

    thing["board"] = board
    thing["chan"] = helper.db_id

    if "com" in thing and thing["com"]:
        thing["urls"] = get_links_from_body(thing["com"])
    elif "sub" in thing and thing["sub"]:
        thing["urls"] = get_links_from_body(thing["sub"])
    if "fsize" in thing and thing["fsize"]:
        url = helper.image_url(board, thing["tim"], thing["ext"])
        if "urls" in thing:
            thing["urls"].append(url)
        else:
            thing["urls"] = [url]
    if "urls" not in thing:
        thing["urls"] = []

    return thing


def get_links_from_body(body):
    result = set()

    body = body \
        .replace("<wbr>", "") \
        .replace("</s>", "") \
        .replace(" dot ", ".")

    for match in LINK_RE.finditer(body):
        url = match.group(1)
        if is_external(url):
            result.add(url)

    return list(result)


def is_external(url):
    return not url.startswith(("#", "/"))
