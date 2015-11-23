from flask import Flask
from light import Light
import threading

app = Flask(__name__)


thread = None
light = Light()



@app.route("/")
def main():
    return "Hello World!"


@app.route("/color/<hex_color>")
def handleColor(hex_color):
    global thread
    light.killme()

    thread = threading.Thread(target = light.setAll, args = [hex_color])
    thread.start()

    return "ok"


@app.route("/rainbow")
@app.route("/rainbow/<int:msDelay>")
def handleRainbow(msDelay = 20):
    global thread
    light.killme()

    thread = threading.Thread(target = light.rainbowCycle, args = [msDelay])
    thread.start()

    return "ok"



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)