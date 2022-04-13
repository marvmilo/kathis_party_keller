from click import progressbar
from dash.exceptions import PreventUpdate
import marvmiloTools as mmt
import colormap
import os

from . import previews

def callback(m1, m2, m3, m4, m5, m6, m7, m8, c1, c2, blur_factor, interval, fade_out):
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
    input_vals = mmt.dictionary.DictObject({
        "mode": mode,
        "color": [
            list(colormap.hex2rgb(c1)),
            list(colormap.hex2rgb(c2)),
        ],
        "blur_factor": blur_factor/100,
        "interval": interval/100,
        "fade_out": fade_out/100
    })
    
    #cleanoup old gifs
    path = "./assets/previews"
    for file in os.listdir("./assets/previews"):
        os.remove(f"{path}/{file}")
    
    return [
        previews.functions["single"](input_vals),
        previews.functions["two_color"](input_vals),
        previews.functions["pulse"](input_vals),
        previews.functions["shoot"](input_vals),
        previews.functions["rainbow"](input_vals),
        previews.functions["audio_pegel"](input_vals),
        previews.functions["audio_brightness"](input_vals),
        previews.functions["audio_shoot"](input_vals),
    ]
    
    raise PreventUpdate