from dash.exceptions import PreventUpdate
import shutil

def callback(state, id):
    if state:
        path = f"/home/pi/scripts/UI/assets/previews/{id}"
        shutil.rmtree(path)
    raise PreventUpdate