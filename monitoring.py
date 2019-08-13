from influxdb import InfluxDBClient

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
    client.write_points(event)
