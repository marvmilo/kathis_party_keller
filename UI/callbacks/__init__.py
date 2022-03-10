import marvmiloTools as mmt
from dash.dependencies import Input, Output, State

#import other scirpts
from . import location
from . import c1

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
    
    #load carousel
    @app.callback(
        [Output("home-carousel", "items")],
        [Input("home-trigger", "children")]
    )
    def callback1(trigger):
        return c1.callback(trigger)