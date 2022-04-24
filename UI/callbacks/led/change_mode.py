from dash.exceptions import PreventUpdate
import marvmiloTools as mmt

#values
led_input_file = "../LED/input.json"
current_active = mmt.json.load(led_input_file).mode

def callback(single_val, two_color_val, pulse_val, shoot_val, rainbow_val, audio_pegel_val, audio_brightness_val, audio_shoot_val, current_selected):
    global current_active
    
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
    
    if not any(mode_states.values()):
        mode_states[current_active] = True
        current_selected = current_active
    elif len([s for s in mode_states if mode_states[s]]) >= 2:
        mode_states[current_selected] = False
        current_selected = [s for s in mode_states if mode_states[s]][0]
        current_active = current_selected
    else:
        raise PreventUpdate
    
    mode_states = {k:(False if not v else True) for k,v in mode_states.items()}
    return [*list(mode_states.values()), current_selected]