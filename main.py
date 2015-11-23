from flask import Flask
from light import Light
from multiprocessing import Process

app = Flask(__name__)


process = None
light = Light()



@app.route("/")
def main():
    return "Hello World!"


@app.route("/color/<hex_color>")
def handleColor(hex_color):
    global process
    light.killme()
    if not process is None:
        process.terminate()

    process = Process(target = light.setAll, args = [hex_color])
    process.daemon = True
    process.start()

    return "ok"


@app.route("/rainbow")
@app.route("/rainbow/<int:msDelay>")
def handleRainbow(msDelay = 20):
    global process
    light.killme()
    if not process is None:
        process.terminate()

    process = Process(target = light.rainbowCycle, args = [msDelay])
    process.daemon = True
    process.start()

    return "ok"



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)