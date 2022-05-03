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
val = 300.30


@app.route("/")
def getval():
    return "300.30"

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
                    weight = random.uniform(-.00399, -0.00001)

                    weight = val * weight
                    historychange.append(weight)
                    val = val + weight

            if direction == 1:
                    ##IF making a livestream, these numbers will have to be reduced down
                    weight = random.uniform(.00001, .00399)

                    weight = val * weight
                    historychange.append(weight)
                    val = val + weight

            return val

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, threaded=False)
