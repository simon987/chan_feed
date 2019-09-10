import logging
import sys
import time
import traceback
from datetime import datetime
from logging import FileHandler, StreamHandler

import requests

last_time_called = dict()

logger = logging.getLogger("default")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s %(levelname)-5s %(message)s')
file_handler = FileHandler("chan_feed.log")
file_handler.setFormatter(formatter)
for h in logger.handlers:
    logger.removeHandler(h)
logger.addHandler(file_handler)
logger.addHandler(StreamHandler(sys.stdout))


def rate_limit(per_second):
    min_interval = 1.0 / float(per_second)

    def decorate(func):
        last_time_called[func] = 0

        def wrapper(*args, **kwargs):
            elapsed = time.perf_counter() - last_time_called[func]
            wait_time = min_interval - elapsed
            if wait_time > 0:
                time.sleep(wait_time)

            last_time_called[func] = time.perf_counter()
            return func(*args, **kwargs)

        return wrapper

    return decorate


class Web:
    def __init__(self, monitoring, rps=1/2):
        self.session = requests.Session()
        self._rps = rps
        self.monitoring = monitoring

        @rate_limit(self._rps)
        def _get(url, **kwargs):
            return self.session.get(url, **kwargs)

        self._get = _get

    def get(self, url, **kwargs):
        try:
            r = self._get(url, **kwargs)

            logger.debug("GET %s <%d>" % (url, r.status_code))
            if self.monitoring:
                self.monitoring.log([{
                    "measurement": "web",
                    "time": str(datetime.utcnow()),
                    "fields": {
                        "status_code": r.status_code,
                        "size": len(r.content),
                    },
                    "tags": {
                        "ok": r.status_code == 200
                    },
                }])
            return r
        except Exception as e:
            logger.error(str(e) + traceback.format_exc())
            if self.monitoring:
                self.monitoring.log([{
                    "measurement": "web",
                    "time": str(datetime.utcnow()),
                    "fields": {
                        "status_code": 0,
                        "size": 0,
                    },
                    "tags": {
                        "ok": False
                    },
                }])
                return None
