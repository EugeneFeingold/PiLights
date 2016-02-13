#!/usr/bin/env python

from flask import Flask, render_template
from light import Light
from multiprocessing import Process

app = Flask(__name__)


process = None
light = Light()

currentState = {}



@app.route("/")
def main():
    return render_template('index.html',
                           hex_color = currentState.color
                           )


def startLight(target, args):
    global process
    if not light is None:
        light.killme()
    if not process is None:
        try:
            process.terminate()
        except:
            print "error terminating process"

    process = Process(target = target, args = args)
    process.daemon = True
    process.start()

    return "Started " + target


@app.route("/color/<hex_color>")
def handleColor(hex_color):
    currentState.color = hex_color
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
