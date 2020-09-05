from flask import Flask
from flask import request
from lib.janken import Hand, Rock, Paper, Scissor
import random

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return {"res": "Hello, world!", "response": 200}


@app.route("/fizbuz", methods=["POST"])
def fizbuz():
    res = ""
    if request.method == "POST":
        n = int(request.json["num"])
    else:
        return {
            "response": 500
        }

    if n % 6 == 0:
        res = "fizbuz"
    elif n % 3 == 0:
        res = "fiz"
    elif n % 2 == 0:
        res = "buz"
    else:
        res = n

    return {
        "response": 200,
        "result": str(res)
    }


@app.route("/janken", methods=["POST"])
def janken():
    # {"hand": "グー"} とか
    your_hand = random.choice([Rock(), Paper(), Scissor()])
    if request.method == "POST":
        my_hand = Hand(request.json["hand"]).hand
    else:
        return {
            "response": 500
        }

    if my_hand > your_hand:
        return {
            "response": 200,
            "result": "WIN"
        }
    elif my_hand < your_hand:
        return {
            "response": 200,
            "result": "LOSE"
        }
    elif my_hand == your_hand:
        return {
            "response": 200,
            "result": "EVEN"
        }


# We only need this for local development.
if __name__ == '__main__':
    app.run()
