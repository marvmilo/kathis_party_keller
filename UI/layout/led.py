from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import marvmiloTools as mmt

#mode select row
def mode_select_row(name, id):
    return dbc.Row(
        children = [
            dbc.Col(
                dbc.Switch(
                    id = id
                ),
                width = "auto"
            ),
            dbc.Col(
                html.H4(name),
                width = "auto"
            ),
            dbc.Col(
                dbc.Progress(
                    label = "loading ...",
                    value = 100,
                    striped = True,
                    animated = True,
                    style = {
                        "height": "2rem",
                        "width": "100%",
                        "maxWidth": "25rem",
                        "minWidth": "15rem"
                    }
                ),
                style = {
                    "display": "flex",
                    "justify-content": "flex-end"
                }
            )
        ],
        style = {
            "padding": "0.5rem"
        }
    )
    
#color picker
def color_picker(name, id):
    return html.Div(
        children = [
            html.Div(
                html.H2(name),
                style = mmt.dash.flex_style()
            ),
            html.Div(
                dbc.Input(
                    type = "color",
                    id = id,
                    style = {
                        "width": "10rem",
                        "height": "5rem"
                    }
                ),
                style = mmt.dash.flex_style()
            )
        ]
    )
    
#Slider
def slider(id):
    return dcc.Slider(0, 100, 1,
        id = id,
        marks={
            0: {'label': '0%'},
            25: {'label': '25%'},
            50: {'label': '50%'},
            75: {'label': '75%'},
            100: {'label': '100%'}
        },
        included = False
    )

#page content
def content():
    return html.Div(
        children = [
            html.H2("LED Modes:"),
            dbc.Accordion(
                children = [
                    dbc.AccordionItem(
                        [
                            mode_select_row("Single", "led-single-select"),
                            mode_select_row("Two Color", "led-two_color-select")
                        ],
                        title="Static",
                    ),
                    dbc.AccordionItem(
                        [
                            mode_select_row("Pulse", "led-pulse-select"),
                            mode_select_row("Shoot", "led-shoot-select"),
                            mode_select_row("Rainbow", "led-rainbow-select")
                        ],
                        title="Animation",
                    ),
                    dbc.AccordionItem(
                        [
                            mode_select_row("Pegel", "led-audio_pegel-select"),
                            mode_select_row("Brightness", "led-audio_brightness-select"),
                            mode_select_row("Shoot", "led-audio_shoot-select"),
                        ],
                        title="Audio",
                    ),
                ]
            ),
            dcc.Store(id='led-current-mode'),
            html.Br(),
            html.H2("Preview:"),
            dbc.Progress(
                label = "loading ...",
                value = 100,
                striped = True,
                animated = True,
                style = {"height": "2.5rem"}
            ),
            html.Br(),
            html.Br(),
            dbc.Row(
                children = [
                    dbc.Col(
                        color_picker("Color 1:", id = "led_color_1_picker")
                    ),
                    dbc.Col(
                        color_picker("Color 2:", id = "led_color_2_picker")
                    )
                ]
            ),
            html.Br(),
            html.Br(),
            html.H2("Blur Factor:"),
            slider("led-blur_factor-slider"),
            html.Br(),
            html.Br(),
            html.H2("Interval:"),
            slider("led-interval-slider"),
            html.Br(),
            html.Br(),
            html.H2("Fade Out:"),
            slider("led-fade_out-slider"),
            html.Br(),
            html.Br(),
            html.Div(
                dbc.Button(
                    "Set LED Behavior!",
                    id = "led-set-behavior",
                    style = {
                        "width": "20rem",
                        "height": "5rem",
                        "fontSize": "1.5rem"
                    }
                ),
                style = mmt.dash.flex_style()
            ),
            dbc.Modal(
                children = [
                    mmt.dash.modal_header_close(
                        title = "Updated LED!",
                        close_id = "modal-close",
                        color = "#222"
                    ),
                    dbc.ModalBody("This is modal body")
                ],
                id = "led-changed-behavior-modal",
                centered=True
            ),
            dcc.Interval(
                id = "led-interval"
            ),
            html.Div(
                "trigger",
                id = "led-trigger",
                style = {"display": "none"}
            )
        ]
    )