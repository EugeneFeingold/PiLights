from flask import Flask
from light import Light
import threading

app = Flask(__name__)


thread = None
light = Light()



@app.route("/")
def main():
    return "Hello World!"


@app.route("/color/<hexColor>")
def handleColor(hexColor):
    global thread
    light.killme()

    thread = threading.Thread(target = light.setAll, args = hexColor)

    return "ok"











if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)