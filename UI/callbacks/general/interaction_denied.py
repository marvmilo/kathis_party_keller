from dash.exceptions import PreventUpdate
import marvmiloTools as mmt

from flask import request
roles = {u["name"]:u["role"] for u in mmt.json.load("./credentials.json").values()}

def callback(n_shutdown, n_light, n_led, n_close, n_ok, is_open, init):
    if roles[request.authorization['username']] == "viewer":
        if init:
            return [not is_open, True]
        else:
            return [False, True]
    raise PreventUpdate