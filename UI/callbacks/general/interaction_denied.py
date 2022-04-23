from dash.exceptions import PreventUpdate

def callback(n_shutdown, n_close, is_open):
    print(n_shutdown)
    raise PreventUpdate