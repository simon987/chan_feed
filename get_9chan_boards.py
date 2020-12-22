import json
import time
import requests
from chan.chan import CHANS

existing = CHANS["9chan"]._boards
updated = list(existing)
added = set()


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


for i in range(0, 50):
    r = requests.get(
        f"https://9chan.tw/boards.html?lang=&tags=&time={int(time.time())}&title=&sfw=0&sort=&sortBy=desc&page={i}",
        headers={
            "Accept": "application/json",
        })

    j = json.loads(r.text)

    if not j["boards"]:
        break

    for board in j["boards"].values():
        board = board["board_uri"]
        added.add(board)

        if ("_" + board) in updated:
            unmask(board)
        elif board not in existing:
            updated.append(board)
            print("[+] " + board)

for board in existing:
    if board not in added:
        mask(board)

print("(" + ",".join('"' + u + '"' for u in updated) + ")")
