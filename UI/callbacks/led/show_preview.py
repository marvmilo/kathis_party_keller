from dash.exceptions import PreventUpdate
from dash import html
import os

path = "/home/pi/scripts/UI/assets/previews"
preview_style= {
    "height": "2rem",
    "width": "100%",
    "maxWidth": "25rem",
    "minWidth": "15rem",
    "borderRadius": "0.25rem"
}

def image(file_name):
    return html.Img(
        src = f"/assets/previews/{file_name}",
        style = preview_style
    )

def callback(interval, loading):
    loaded = {f.split("-")[0]: f for f in os.listdir(path)}
    modes = ["single", "two_color", "pulse", "shoot", "rainbow", "audio_pegel", "audio_brightness", "audio_shoot"]
    return_list = []
    
    for mode in modes:
        print(mode)
        if mode in loaded.keys():
            return_list.append(image(loaded[mode]))
        else:
            return_list.append(loading())
    
    return return_list