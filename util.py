import logging
import sys
import traceback
from datetime import datetime
from logging import FileHandler, StreamHandler

import requests
from hexlib.misc import rate_limit
from urllib3 import disable_warnings

disable_warnings()

last_time_called = dict()

logger = logging.getLogger("default")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s %(levelname)-5s %(message)s')
for h in logger.handlers:
    logger.removeHandler(h)
logger.addHandler(StreamHandler(sys.stdout))


class Web:
    def __init__(self, monitoring, rps=1 / 2, proxy=None, get_method=None):
        self.session = requests.Session()
        if proxy:
            self.session.proxies = {"http": proxy, "https": proxy}
            self.session.verify = False
        self._rps = rps
        self.monitoring = monitoring
        self._get_method = get_method

        @rate_limit(self._rps)
        def _get(url, **kwargs):
            retries = 3

            while retries > 0:
                retries -= 1
                try:
                    if self._get_method:
                        return self._get_method(url, **kwargs)
                    return self.session.get(url, **kwargs)
                except KeyboardInterrupt as e:
                    raise e
                except Exception as e:
                    logger.warning("Error with request %s: %s" % (url, str(e)))
            raise Exception("Gave up request after maximum number of retries")

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
        except KeyboardInterrupt as e:
            raise e
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
