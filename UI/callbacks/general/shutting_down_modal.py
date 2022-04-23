from dash.exceptions import PreventUpdate
import os

def callback(n_clicks):
    if n_clicks:
        return [True]
    raise PreventUpdate