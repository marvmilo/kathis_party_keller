import dash_bootstrap_components as dbc
from dash import dcc

from . import change_mode
from . import set_behavior
from . import initial_load
from . import disable_input
from . import render_preview
from . import show_preview

#mode loading
def mode_loading_content():
    return [
        dbc.Progress(
            label = "loading ...",
            value = 100,
            striped = True,
            animated = True,
            style = {"height": "2rem"}
        ),
        dcc.Interval(
            id = "led-preview-interval",
            interval = 500
        )
    ]