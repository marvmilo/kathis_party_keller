import dash
import dash_auth
from dash import html
import dash_bootstrap_components as dbc
import marvmiloTools as mmt

#import other scripts
import LED

#start led thread function
def start_LED_Thread():
    LED_thread = LED.Thread()
    LED_thread.start()
    return LED_thread

#starting led thread
LED_thread = start_LED_Thread()