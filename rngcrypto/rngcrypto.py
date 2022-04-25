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
val = 5640.00

@app.route("/")
def getval():
    return str(val)

##This will turn into a loop for running if we are just going to display a stream.
@app.route("/<str:val>")
def rngetf(float(val)):
    
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
                weight = random.uniform(-.05, -0.009)
                weight = val * weight
                historychange.append(weight)
                val = val + weight

        if direction == 1:
                ##IF making a livestream, these numbers will have to be reduced down
                weight = random.uniform(.05, .009)

                weight = val * weight
                historychange.append(weight)
                val = val + weight

        return str(val)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, threaded=False)
