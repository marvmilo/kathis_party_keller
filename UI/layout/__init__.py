from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import marvmiloTools as mmt

#import other scripts
from . import home
from . import led

#main structure of page
def structure(settings):
    return html.Div(
        children = [
            navbar(settings.name, settings.style.logo),
            mmt.dash.content_div(
                width = "1000px",
                padding = "5%",
                children = [
                    html.Div(
                        html.Div(
                            dbc.Spinner(spinner_style = {"width": "3rem", "height": "3rem"}),
                            style = mmt.dash.flex_style({"height": "20rem"})
                        ),
                        id = "main-content"
                    )
                ]
            ),
            dcc.Location(id = "url", refresh = False),
            html.Div(
                children = [
                    html.Div(id = "home-trigger"),
                    html.Div(id = "led-trigger"),
                    html.Div(id = "led-color1-div"),
                    html.Div(id = "led-color2-div"),
                    html.Div(id = "led-blur_factor-div"),
                    html.Div(id = "led-interval-div"),
                    html.Div(id = "led-fade_out-div"),
                    html.Div(id = "led-single-select-preview"),
                    html.Div(id = "led-two_color-select-preview"),
                    html.Div(id = "led-pulse-select-preview"),
                    html.Div(id = "led-shoot-select-preview"),
                    html.Div(id = "led-rainbow-select-preview"),
                    html.Div(id = "led-audio_pegel-select-preview"),
                    html.Div(id = "led-audio_brightness-select-preview"),
                    html.Div(id = "led-audio_shoot-select-preview"),
                    html.Div(id = "led-single-gif-preview"),
                    html.Div(id = "led-two_color-gif-preview"),
                    html.Div(id = "led-pulse-gif-preview"),
                    html.Div(id = "led-shoot-gif-preview"),
                    html.Div(id = "led-rainbow-gif-preview"),
                    html.Div(id = "led-audio_pegel-gif-preview"),
                    html.Div(id = "led-audio_brightness-gif-preview"),
                    html.Div(id = "led-audio_shoot-gif-preview"),
                    html.Div(id = "led-gif-preview"),
                    html.Div(id = "led-preview"),
                    html.Div(id = "led-preview-interval-div-1"),
                    html.Div(id = "led-preview-interval-div-2"),
                    html.H1(id = "home-polaroid-date"),
                    dbc.Carousel(id = "home-polaroid-carousel", items = []),
                    dbc.Carousel(id = "home-rules-carousel", items = []),
                    dcc.Interval(id = "home-polaroid-interval", max_intervals = 0),
                    dcc.Interval(id = "led-preview-interval", max_intervals = 0),
                    dbc.Switch(id = "led-single-select"),
                    dbc.Switch(id = "led-two_color-select"),
                    dbc.Switch(id = "led-pulse-select"),
                    dbc.Switch(id = "led-shoot-select"),
                    dbc.Switch(id = "led-rainbow-select"),
                    dbc.Switch(id = "led-audio_pegel-select"),
                    dbc.Switch(id = "led-audio_brightness-select"),
                    dbc.Switch(id = "led-audio_shoot-select"),
                    dbc.Input(id = "led_color_1_picker"),
                    dbc.Input(id = "led_color_2_picker"),
                    dcc.Slider(0, 0, id = "led-blur_factor-slider"),
                    dcc.Slider(0, 0, id = "led-interval-slider"),
                    dcc.Slider(0, 0, id = "led-fade_out-slider"),
                    dbc.Button(id = "led-set-behavior"),
                    dbc.Button(id = "led-changed-behavior-modal-ok"),
                    dbc.Button(id = "led-changed-behavior-modal-close"),
                    dcc.Store(id = "led-current-mode"),
                    dcc.Store(id = "led-preview-id"),
                    dcc.Store(id = "led-preview-loaded"),
                    dcc.Store(id = "led-previous-preview"),
                    dbc.Modal(id = "led-changed-behavior-modal")
                ],
                style = {"display": "none"}
            )
        ]
    )

#navbar of page
def navbar(title, logo):
    return mmt.dash.nav.bar(
        logo = f"url({logo})",
        logo_style = {
            "width": "5rem", 
            "height": "5rem",
            "backgroundSize": "cover",
        },
        title = title,
            title_style = {
            "width": "10rem",
            "fontSize": "1.5rem"
        }, 
        expand = "lg",
        items = [
            mmt.dash.nav.item.href(
                "Home",
                href = "/"
            ),
            mmt.dash.nav.item.href(
                "LED",
                href = "/led"
            ),
            mmt.dash.nav.item.href(
                "Github",
                href = "https://github.com/marvmilo/kathis_party_keller",
                target = "_blank"
            ),
            mmt.dash.nav.item.normal(
                "Shutdown",
                id = "shutdown-button",
                color = "info"
            ),
        ]
    )

#not found page
def not_found():
    return html.Div(
        html.Div(
            children = [
                html.Div(
                    "404",
                    style = mmt.dash.flex_style({
                        "fontSize": "7rem",
                        "fontWeight": "bold"
                    })
                ),
                html.Div(
                    "Not Found!",
                    style = mmt.dash.flex_style({
                        "fontSize": "2rem",
                        "fontWeight": "bold"
                    })
                )
            ]
        ),
        style = mmt.dash.flex_style({"height": "30rem"})
    )