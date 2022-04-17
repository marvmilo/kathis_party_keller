from dash.exceptions import PreventUpdate
from dash import html
from PIL import Image
import PIL
import os

def callback(interval, id, loading, image):
    try:
        path = f"/home/pi/scripts/UI/assets/previews/{id}"
        loaded = {f.split("-")[0]: f for f in os.listdir(path)}
        modes = ["single", "two_color", "pulse", "shoot", "rainbow", "audio_pegel", "audio_brightness", "audio_shoot", "general"]
        all_loaded = True
        return_list = []
        
        for mode in modes:
            if mode in loaded.keys():
                try:
                    Image.open(f"{path}/{loaded[mode]}")
                    return_list.append(image(loaded[mode], id))
                except PIL.UnidentifiedImageError:
                    return_list.append(loading())
                    all_loaded = False
            else:
                return_list.append(loading())
                all_loaded = False
            
        if all_loaded:
            return_list.append(True)
        else:
            return_list.append(False)
        
        return return_list
    except FileNotFoundError:
        raise PreventUpdate