from flask import Flask, Response
import os
import socket
import time
import random

app = Flask(__name__)

historychange = []
historyvalue = []
firstrun = True
direction = 0
weight = 0
val = 570.00


@app.route("/")
def getval():
    return val

##This will turn into a loop for running if we are just going to display a stream.
@app.route("/<float:val>")
def rngetf(val):

    if firstrun == True:
            return val
            firstrun = False

    else:   

        i = random.randint(1,8)

        if i != 0 and i <= 4:
            direction = -1

        if i != 0 and i > 4:
            direction = 1 

        if direction == -1:
                ##IF making a livestream, these numbers will have to be reduced down

                ##Crash Flag

                weight = random.uniform(-.01, -0.0015)

                weight = val * weight
                historychange.append(weight)
                val = val + weight

        if direction == 1:
                ##IF making a livestream, these numbers will have to be reduced down

                ##Rocket flag

                weight = random.uniform(.01, .00399)

                weight = val * weight
                historychange.append(weight)
                val = val + weight

        return val

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, threaded=False)
