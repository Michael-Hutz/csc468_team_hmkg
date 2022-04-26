import logging
import os
from redis import Redis
import requests
import time

DEBUG = os.environ.get("DEBUG", "").lower().startswith("y")

tally = 0

log = logging.getLogger(__name__)
if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("requests").setLevel(logging.WARNING)

redis = Redis("redis")

def getrngetf():
    val = requests.get("http://rngetf/")
    ret = requests.get("http://rngetf/val/")
    return val.content

def getrngtech():
    val = requests.get("http://rngtech/")
    ret = requests.get("http://rngtech/val/")
    return val.content

def getrngcrypto():
    val = requests.get("http://rngcrypto/")
    ret = requests.get("http://rngcrypto/val/)
    return val.content

def loop(int = 1):
    term = 0
    iter = 0
    while True:
        if time.time() > term:
           log.info("{} updates completes".format(iter))
           term = time.time() + int
        time.sleep(3)
        solo()
        iter = iter + 1
        

def solo():
    log.debug("Solo run commencing")
    time.sleep(0.1)
    etf = getrngetf()
    tech = getrngtech()
    crypto = getrngcrypto()
    log.info("Price updated for all stocks")
    redis.hset("etf", etf, 1)
    redis.hset("tech", tech, 1)
    redis.hset("crypto", crypto, 1) 
    etflog = redis.hgetall("etf")
    techlog = redis.hgetall("tech")
    cryptolog = redis.hgetall("crypto")
    log.info("ETF Values {}".format(etflog))
    log.info("Tech Values {}".format(techlog))
    log.info("Crypto Values {}".format(cryptolog))


if __name__ == "__main__":
    while True:
        try:
            loop()
        except:
            log.exception("In Loop Already:")
            log.error("Attempting to reboot")
            time.sleep(5)
