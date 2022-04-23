from dash.exceptions import PreventUpdate
import marvmiloTools as mmt

from flask import request
roles = {u["name"]:u["role"] for u in mmt.json.load("/home/pi/scripts/UI/credentials.json").values()}

def callback(n_shutdown, n_close, n_yes, n_no):
    if roles[request.authorization['username']] == "admin":
        if n_shutdown:
            return [True, 0]
        else:
            return [False, 0]
    else:
        raise PreventUpdate