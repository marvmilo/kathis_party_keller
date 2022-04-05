from dash.exceptions import PreventUpdate
import marvmiloTools as mmt
import colormap

def callback(trigger):
    #values
    led_input_file = "/home/pi/scripts/LED/input.json"
    current_led_settings = mmt.json.load(led_input_file)
    
    return [
        colormap.rgb2hex(*current_led_settings.color[0]),
        colormap.rgb2hex(*current_led_settings.color[1]),
        current_led_settings.blur_factor*100,
        current_led_settings.interval*100,
        current_led_settings.fade_out*100
    ]
    