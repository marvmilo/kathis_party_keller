from dash.exceptions import PreventUpdate
from requests import session
import rpi_ws281x as led
import os
import marvmiloTools as mmt

from flask import request
roles = {u["name"]:u["role"] for u in mmt.json.load("./credentials.json").values()}

# LED strip configuration:
LED_COUNT      = 175    # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

status = False
session_id = None

def callback(n_clicks, n_intervals, id):
    global status, session_id
    
    if roles[request.authorization['username']] == "admin":
        if n_clicks and not session_id == id:
            session_id = id
            if status:
                status = False
                os.system("sudo systemctl start kpk_led.service")
                return ["secondary", 0]
            else:
                status = True
                os.system("sudo systemctl stop kpk_led.service")
                strip = led.Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
                strip.begin()
                for i in range(strip.numPixels()):
                    strip.setPixelColor(i, led.Color(150,150,150))
                strip.show()
                del strip
                return ["light", 0]
        
        if id == session_id:
            session_id = None
        
        if n_intervals:
            if status:
                return ["light", 0]
            else:
                return ["secondary", 0]
        raise PreventUpdate
    else:
        raise PreventUpdate