from click import progressbar
from dash.exceptions import PreventUpdate
import marvmiloTools as mmt
import colormap

from . import previews

def callback(m1, m2, m3, m4, m5, m6, m7, m8, c1, c2, blur_factor, interval, fade_out, i):
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
    
    max_frames = 30
    try:
        i = i % max_frames
    except TypeError:
        raise PreventUpdate
    
    return [
        previews.functions["single"](input_vals, i, max_frames),
        previews.functions["two_color"](input_vals, i, max_frames),
        previews.functions["pulse"](input_vals, i, max_frames),
        None,
        None,
        None,
        None,
        None
    ]
    
    raise PreventUpdate