from dash.exceptions import PreventUpdate
import marvmiloTools as mmt

def callback(trigger):
    if trigger:
        mode = mmt.json.load("../LED/input.json").mode
        item = None
        mapping_dict = {
            0: ["single", "two_color"],
            1: ["pulse", "shoot", "rainbow"],
            2: ["audio_pegel", "audio_brightness", "audio_shoot"]
        }

        for key in mapping_dict:
            if mode in mapping_dict[key]:
                item = key
        
        if item:
            return [item]
    raise PreventUpdate
