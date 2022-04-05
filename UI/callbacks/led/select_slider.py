from urllib.parse import ParseResultBytes
from dash.exceptions import PreventUpdate
import marvmiloTools as mmt
import datetime as dt

from numpy import var

#values
led_input_file = "/home/pi/scripts/LED/input.json"
current_values = dict()
changes = dict()
change_ts = dict()

def callback(value, interval, variable):
    global current_values, changes, change_ts
    
    try:
        value = value/100
    except TypeError:
        current_values[variable] = mmt.json.load(led_input_file)[variable]
        changes[variable] = False
        change_ts[variable] = dt.datetime.now()
        return [current_values[variable]*100]
    
    if changes[variable]:
        if (dt.datetime.now() - change_ts[variable]).total_seconds() > 2:
            changes[variable] = False
    elif not current_values[variable] == value:
        current_values[variable] = value
        mmt.json.write(value, led_input_file, [variable])
        changes[variable] = True
        change_ts[variable] = dt.datetime.now()
    else:
        raise PreventUpdate
    
    return [current_values[variable]*100]