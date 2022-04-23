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
                html.Div(
                    style = {
                        "display": "flex",
                        "justifyContent": "flex-end"
                    },
                    id = f"{id}-preview"
                )
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
                        "width": "9.5rem",
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
                        item_id = 0
                    ),
                    dbc.AccordionItem(
                        [
                            mode_select_row("Pulse", "led-pulse-select"),
                            mode_select_row("Shoot", "led-shoot-select"),
                            mode_select_row("Rainbow", "led-rainbow-select")
                        ],
                        title="Animation",
                        item_id = 1
                    ),
                    dbc.AccordionItem(
                        [
                            mode_select_row("Pegel", "led-audio_pegel-select"),
                            mode_select_row("Brightness", "led-audio_brightness-select"),
                            mode_select_row("Shoot", "led-audio_shoot-select"),
                        ],
                        title="Audio",
                        item_id = 2
                    ),
                ],
                id = "led-accordion"
            ),
            dcc.Store(id='led-current-mode'),
            html.Br(),
            html.H2("Preview:"),
            html.Div(
                style = {
                    "display": "flex",
                    "justifyContent": "flex-end"
                },
                id = f"led-preview"
            ),
            dbc.Row(
                children = [
                    dbc.Col(
                        children = [
                            html.Br(),
                            html.Br(),
                            color_picker("Color 1:", id = "led_color_1_picker"),
                        ],
                        id = "led-color1-div",
                        style = {"display": "none"}
                    ),
                    dbc.Col(
                        children = [
                            html.Br(),
                            html.Br(),
                            color_picker("Color 2:", id = "led_color_2_picker"),
                        ],
                        id = "led-color2-div",
                        style = {"display": "none"}
                    )
                ]
            ),
            html.Br(),
            html.Br(),
            html.Div(
                children = [
                    html.H2("Blur Factor:"),
                    slider("led-blur_factor-slider"),
                    html.Br(),
                    html.Br(),
                ],
                id = "led-blur_factor-div",
                style = {"display": "none"}
            ),
            html.Div(
                children = [
                    html.H2("Interval:"),
                    slider("led-interval-slider"),
                    html.Br(),
                    html.Br(),
                ],
                id = "led-interval-div",
                style = {"display": "none"}
            ),
            html.Div(
                children = [
                    html.H2("Fade Out:"),
                    slider("led-fade_out-slider"),
                    html.Br(),
                    html.Br(),
                ],
                id = "led-fade_out-div",
                style = {"display": "none"}
            ),
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
            html.Br(),
            html.Br(),
            dbc.Modal(
                children = [
                    mmt.dash.modal_header_close(
                        title = "Updated LED!",
                        close_id = "led-changed-behavior-modal-close",
                        color = "#222"
                    ),
                    dbc.ModalBody(
                        children = [
                            html.Br(),
                            html.Div(
                                "Set LED Behavior to current Input Settings.",
                                style = mmt.dash.flex_style({"textAlign": "center"})
                            ),
                            html.Br(),
                            html.Div(
                                dbc.Button(
                                    "OK",
                                    id = "led-changed-behavior-modal-ok",
                                    style = {
                                        "width": "10rem",
                                        "height": "3rem"
                                    }
                                ),
                                style = mmt.dash.flex_style()
                            ),
                            html.Br()
                        ]
                    )
                ],
                id = "led-changed-behavior-modal",
                centered=True
            ),
            html.Div(
                id = "led-preview-interval-div-1",
                style = {"display": "none"}    
            ),
            dcc.Store(
                id = "led-preview-id",
                data = mmt.dash.random_ID(32)
            ),
            dcc.Store(
                id = "led-previous-preview"
            ),
            dcc.Store(
                id = "led-preview-loaded",
                data = False
            ),
            html.Div(
                "trigger",
                id = "led-trigger",
                style = {"display": "none"}
            )
        ]
    )