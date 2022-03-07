import marvmiloTools as mmt
from dash.dependencies import Input, Output, State

#import other scirpts
from . import location

def init(app, layout):
    #navbar toggler callback
    @app.callback(*mmt.dash.nav.callback_args)
    def cn(n, is_open):
        return mmt.dash.nav.callback_function(n, is_open)

    #page location callback
    @app.callback(
        Output("main-content", "children"),
        Input("url", "pathname")
    )
    def cl(path):
        return location.callback(path, layout)