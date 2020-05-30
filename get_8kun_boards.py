import json
import requests
from chan.chan import CHANS

existing = CHANS["8kun2"]._boards
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


for i in range(0, 500, 50):
    r = requests.get("https://sys.8kun.top/board-search.php?page=" + str(i))

    j = json.loads(r.text)

    for board in j["boards"]:
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
