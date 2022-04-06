from dash.exceptions import PreventUpdate
import marvmiloTools as mmt

#values
led_settings = mmt.json.load("/home/pi/scripts/LED/settings.json")

def callback(single_val, two_color_val, pulse_val, shoot_val, rainbow_val, audio_pegel_val, audio_brightness_val, audio_shoot_val, trigger):
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
    
    current_mode = [s for s in mode_states if mode_states[s]][0]
    current_disabled = mmt.dictionary.DictObject({k: not bool(v) for k, v in led_settings[current_mode].items()})
    current_style = {k: {"display": "none"} if v else dict() for k, v in current_disabled.items()}
    
    return [
        current_style["color1"],
        current_style["color2"],
        current_style["blur_factor"],
        current_style["interval"],
        current_style["fade_out"]
    ]