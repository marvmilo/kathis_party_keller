from click import progressbar
from dash.exceptions import PreventUpdate
import marvmiloTools as mmt
import colormap
import os

from . import previews

def callback(m1, m2, m3, m4, m5, m6, m7, m8, c1, c2, blur_factor, interval, fade_out, id, loading):
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
    path = f"./assets/previews/{id}"
    try:
        os.mkdir(path)
    except FileExistsError:
        pass
    for file in os.listdir(path):
        os.remove(f"{path}/{file}")
    
    previews.input_vals = input_vals
    
    return [
        previews.apply("single", loading, id),
        previews.apply("two_color", loading, id),
        previews.apply("pulse", loading, id),
        previews.apply("shoot", loading, id),
        previews.apply("rainbow", loading, id),
        previews.apply("audio_pegel", loading, id),
        previews.apply("audio_brightness", loading, id),
        previews.apply("audio_shoot", loading, id),
    ]
    
    raise PreventUpdate