from dash.exceptions import PreventUpdate
import marvmiloTools as mmt
import colormap

def callback(n_set, n_close, n_ok, m1, m2, m3, m4, m5, m6, m7, m8, c1, c2, blur_factor, interval, fade_out):
    if n_set:
        mode_states = {
            "single": m1,
            "two_color": m2,
            "pulse": m3,
            "shoot": m4,
            "rainbow": m5,
            "audio_pegel": m6,
            "audio_brightness": m7,
            "audio_shoot": m8
        }
        mode = [s for s in mode_states if mode_states[s]][0]
        
        input_file = {
            "mode": mode,
            "color": [
                list(colormap.hex2rgb(c1)),
                list(colormap.hex2rgb(c2)),
            ],
            "blur_factor": blur_factor/100,
            "interval": interval/100,
            "fade_out": fade_out/100
        }
        mmt.json.save(input_file, filename = "/home/pi/scripts/LED/input.json")
        
        return [True, 0]
    else:
        return [False, 0]