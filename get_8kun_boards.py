import json

from hexlib.log import logger
from vanwanet_scrape.scraper import Scraper

from chan.chan import CHANS

existing = CHANS["8kun2"]._boards
updated = list(existing)
added = set()

scraper = Scraper(
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


def mask(board):
    for i, b in enumerate(updated):
        if b == board:
            updated[i] = "_" + board
            print("[-] " + board)


def unmask(board):
    for i, b in enumerate(updated):
        if b == ("_" + board):
            updated[i] = board
            print("[*] " + board)


for i in range(0, 500, 50):
    r = scraper.get("https://sys.8kun.top/board-search.php?page=" + str(i))
    j = json.loads(r.text)

    for board in j["boards"]:
        added.add(board)

        if ("_" + board) in updated:
            unmask(board)
        elif board not in existing:
            updated.append(board)
            print("[+] " + board)

for board in existing:
    if board not in added and not board.startswith("_"):
        mask(board)

print("(" + ",".join('"' + u + '"' for u in updated) + ")")
