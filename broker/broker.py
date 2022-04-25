import logging
import os
from redis import Redis
import requests
import time

DEBUG = os.environ.get("DEBUG", "").lower().startswith("y")

log = logging.getLogger(__name__)
if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("requests").setLevel(logging.WARNING)

redis = Redis("redis")

def getrngetf():
    val = requests.get(http://rngetf/")
    ret = requests.get("http://rngetf/", val=val)
    return ret.content

def getrngtech():
    val = requests.get(http://rngtech/")
    ret = requests.get("http://rngtech/", val=val)
    return ret.content

def getrngcrypto():
    val = requests.get(http://rngcrypto/")
    ret = requests.get("http://rngcrypto/", val=val)
    return ret.content

def loop(int = 1):
    term = 0
    iter = 0
    while True:
        if time.time() > term:
           log.info("{} updates completes".format(iter))
           term = time.time() + int
        solo()
        iter = iter + 1
        

def solo():
    log.debug("Solo run commencing")
    time.sleep(0.1)
    etf = getrngetf()
    tech = getrngtech()
    crypto = getrngcrypto()
    log.info("Price updated for all stocks")
    redis.hset("etf", etf)
    redis.hset("tech", tech)
    redis.hset("crypto", crypto) 
    log.info("New values: " + redis.hgetall())


if __name__ == "__main__":
    while True:
        try:
            loop()
        except:
            log.exception("In Loop Already:")
            log.error("Attempting to reboot")
            time.sleep(5)
