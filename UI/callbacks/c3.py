import os
import random
from dash.exceptions import PreventUpdate

#declare vals
path = "./assets/rules"

#load inital rules carousel pictures
def callback(trigger):
    if trigger:
        items = []
        item = None
        pics = os.listdir(path)
        random.shuffle(pics)
        for i, pic in enumerate(pics):
            item = {
                "key": str(i), 
                "src": f"{path}/{pic}"
            }
            items.append(item)
        return [items]
    raise PreventUpdate