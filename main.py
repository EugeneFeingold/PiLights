#!/usr/bin/env python

from flask import Flask
from light import Light
from multiprocessing import Process

app = Flask(__name__)


process = None
light = Light()



@app.route("/")
def main():
    return "Hello World!"


def startLight(target, args):
    global process
    light.killme()
    if not process is None:
        process.terminate()

    process = Process(target = target, args = args)
    process.daemon = True
    process.start()

    return "Started " + target


@app.route("/color/<hex_color>")
def handleColor(hex_color):
    return startLight(light.setAll, [hex_color])


@app.route("/rainbow")
@app.route("/rainbow/<int:msDelay>")
def handleRainbow(msDelay = 20):
    return startLight(light.rainbowCycle, [msDelay])


@app.route("/rainbowAll")
@app.route("/rainbowAll/<int:msDelay>")
def handleRainbowAll(msDelay = 20):
    return startLight(light.rainbowCycleAll, [msDelay])


@app.route("/chaser")
@app.route("/chaser/<int:msDelay>")
def handleChaser(msDelay = 20):
    return startLight(light.chaser, [msDelay])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
