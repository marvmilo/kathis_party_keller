from dash.exceptions import PreventUpdate
import shutil
import time

def callback(state, id, interval):
    if state:
        time.sleep(1)
        try:
            path = f"/home/pi/scripts/UI/assets/previews/{id}"
            shutil.rmtree(path)
            return [interval()]
        except FileNotFoundError:
            pass
    raise PreventUpdate