import itertools

import orjson
import psycopg2
from hexlib.misc import buffered
from tqdm import tqdm
from hexlib.db import pg_fetch_cursor_all

from chan.chan import CHANS

if __name__ == '__main__':

    conn = psycopg2.connect(
        host="192.168.1.70",
        port="5432",
        user="feed_archiver",
        password="",
        dbname="feed_archiver"
    )

    conn.set_client_encoding("utf8")

    table = "chan_4chan_post"
    new_table = "chan2_4chan_post"

    print(table)

    # chan_name = table.split("_")[1]
    # chan = CHANS[chan_name]

    cur = conn.cursor()
    cur2 = conn.cursor()

    cur2.execute("""
    CREATE TABLE IF NOT EXISTS %s (
        id TEXT PRIMARY KEY NOT NULL,
		archived_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        data JSONB NOT NULL
    );
    """ % new_table)

    cur.execute("SELECT COUNT(*) FROM %s" % table)
    row_count = cur.fetchone()[0]

    cur.execute("DECLARE cur1 CURSOR FOR SELECT * FROM %s" % table)

    rows = pg_fetch_cursor_all(cur, name="cur1", batch_size=5000)


    @buffered(batch_size=1000)
    def pg_bulk_insert(rows):
        val_count = len(rows[0])

        cur2.execute(
            "INSERT INTO %s VALUES %s ON CONFLICT DO NOTHING" %
            (
                new_table,
                ", ".join(("(" + ",".join("%s" for _ in range(val_count)) + ")") for _ in rows)
            ),
            list(itertools.chain(*rows))
        )


    for row in tqdm(rows, total=row_count):
        id_, archived_on, data = row

        new_id = data["_board"] + str(data["no"])

        pg_bulk_insert([
            (new_id, archived_on, orjson.dumps(data).decode())
        ])
    pg_bulk_insert(None)
    conn.commit()
