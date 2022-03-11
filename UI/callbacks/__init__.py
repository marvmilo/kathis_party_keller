import marvmiloTools as mmt
from dash.dependencies import Input, Output, State

#import other scirpts
from . import location
from . import c1
from . import c2

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
    
    #update polaroid date
    @app.callback(
        [Output("home-polaroid-date", "children"),
         Output("home-polaroid-interval", "disabled")],
        [Input("home-carousel", "active_index"),
         Input("home-polaroid-interval", "n_intervals")],
        [State("home-polaroid-date", "children"),
         State("home-carousel", "items")]
    )
    def callback2(active, interval, current_date, items):
        return c2.callback(active, interval, current_date, items)