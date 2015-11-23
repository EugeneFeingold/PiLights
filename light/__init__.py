import time

from neopixel import *



# LED strip configuration:
LED_COUNT      = 180      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)




class Light(object):
    def killme(self):
        self.isKilled = True


    def setAll(self, hexColor):
        self.isKilled = False
        for i in range(0, LED_COUNT):
            self.strip.setPixelColor(i, ColorStr(hexColor))
        self.strip.show()

    def rainbowCycle(self, wait_ms=20, iterations=5):
        self.isKilled = False
        while True:
            """Draw rainbow that uniformly distributes itself across all pixels."""
            for j in range(256*iterations):
                for i in range(self.strip.numPixels()):
                    self.strip.setPixelColor(i, self.wheel(((i * 256 / self.strip.numPixels()) + j) & 255))
                self.strip.show()
                if self.isKilled:
                    return
                time.sleep(wait_ms/1000.0)
                if self.isKilled:
                    return



    def wheel(self, pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)


    def __init__(self):
        # Create NeoPixel object with appropriate configuration.
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()
        for i in range(0, LED_COUNT):
            self.strip.setPixelColor(i, Color(0, 0, 0))
        self.strip.show()
        self.isKilled = False

