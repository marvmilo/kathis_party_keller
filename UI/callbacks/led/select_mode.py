from dash.exceptions import PreventUpdate
import marvmiloTools as mmt
import datetime as dt

#values
led_input_file = "/home/pi/scripts/LED/input.json"
current_active = mmt.json.load(led_input_file).mode
change = False
change_ts = None

def callback(single_val, two_color_val, pulse_val, shoot_val, rainbow_val, audio_pegel_val, audio_brightness_val, audio_shoot_val, interval):
    global current_active, change, change_ts
    
    mode_states = {
        "single": single_val,
        "two_color": two_color_val,
        "pulse": pulse_val,
        "shoot": shoot_val,
        "rainbow": rainbow_val,
        "audio_pegel": audio_pegel_val,
        "audio_brightness": audio_brightness_val,
        "audio_shoot": audio_shoot_val
    }
    if change:
        mode_states = {key: False for key in mode_states.keys()}
        mode_states[current_active] = True
        if (dt.datetime.now() - change_ts).total_seconds() > 2:
            change = False
    elif not any(mode_states.values()):
        mode_states[current_active] = True
    elif len([v for k, v in mode_states.items() if v]) > 1:
        mode_states[current_active] = False
        current_active = [k for k, v in mode_states.items() if v][0]
        mmt.json.write(current_active, led_input_file, ["mode"])
        change = True
        change_ts = dt.datetime.now()
    else:
        raise PreventUpdate
    
    return list(mode_states.values())