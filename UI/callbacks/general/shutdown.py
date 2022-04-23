from dash.exceptions import PreventUpdate
import os

def callback(is_open):
    if is_open:
        os.system("sudo shutdown now")
    raise PreventUpdate