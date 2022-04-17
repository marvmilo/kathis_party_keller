import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

from . import change_mode
from . import set_behavior
from . import initial_load
from . import disable_input
from . import render_preview
from . import show_preview
from . import cleanup_preview

#mode loading
def mode_loading_content():
    return [
        dbc.Progress(
            label = "loading ...",
            value = 100,
            striped = True,
            animated = True,
            style = {"height": "2rem"}
        )
    ]

#preview interval
def preview_interval_disabled():
    return [
        dcc.Interval(
            id = "led-preview-interval",
            interval = 1000,
            disabled = True
        )
    ]
    
def preview_interval_enabled():
    return [
        html.Div(
            dcc.Interval(
                id = "led-preview-interval",
                interval = 1000,
                disabled = False
            ),
            id = "led-preview-interval-div-2"
        )
    ]
    
#for displaying Gif
def image(mode, id):
    if mode == "general":
        return html.Img(
            src = f"/assets/previews/{id}/{mode}",
            style = {
                "height": "2rem",
                "width": "100%",
                "maxWidth": "25rem",
                "minWidth": "15rem",
                "borderRadius": "0.25rem"
            }
        )
    else:
        return html.Img(
            src = f"/assets/previews/{id}/{mode}",
            style = {
                "height": "2rem",
                "width": "100%",
                "minWidth": "15rem",
                "borderRadius": "0.25rem"
            }
        )