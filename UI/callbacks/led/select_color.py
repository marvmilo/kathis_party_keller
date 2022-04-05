from dash.exceptions import PreventUpdate
import marvmiloTools as mmt
import datetime as dt
import colormap

#values
led_input_file = "/home/pi/scripts/LED/input.json"
current_color_1 = mmt.json.load(led_input_file).color[0]
current_color_2 = mmt.json.load(led_input_file).color[1]
changes = [False, False]
change = False
change_ts = dt.datetime.now()

def callback(color_1_val, color_2_val, interval):
    global current_color_1, current_color_2, change, change_ts
    
    if color_1_val and color_2_val:
        color_states = [
            colormap.hex2rgb(color_1_val),
            colormap.hex2rgb(color_2_val)
        ]
        changes = [True if not list(c) in [current_color_1, current_color_2] else False for c in color_states]
    
    if change or not color_1_val or not color_2_val:
        color_states = [current_color_1, current_color_2]
        if (dt.datetime.now() - change_ts).total_seconds() > 2:
            change = False
    elif any(changes):
        current_color_1 = list(color_states[0])
        current_color_2 = list(color_states[1])
        mmt.json.write(color_states, led_input_file, ["color"])
        change = True
        change_ts = dt.datetime.now()
    else:
        raise PreventUpdate
    
    return [colormap.rgb2hex(*c) for c in color_states]
