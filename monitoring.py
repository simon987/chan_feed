import traceback

from influxdb import InfluxDBClient

from util import logger

client = InfluxDBClient("localhost", 8086, "root", "root", "chan_feed")


def init():
    db_exists = False
    for db in client.get_list_database():
        if db["name"] == "chan_feed":
            db_exists = True
            break

    if not db_exists:
        client.create_database("chan_feed")


def log(event):
    try:
        client.write_points(event)
    except Exception as e:
        logger.debug(traceback.format_exc())
        logger.error(str(e))
