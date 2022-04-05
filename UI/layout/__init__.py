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
            dcc.Location(id = "url"),
            html.Div(
                children = [
                    html.Div(id = "home-trigger"),
                    html.Div(id = "led-trigger"),
                    html.H1(id = "home-polaroid-date"),
                    dbc.Carousel(id = "home-polaroid-carousel", items = []),
                    dbc.Carousel(id = "home-rules-carousel", items = []),
                    dcc.Interval(id = "home-polaroid-interval", disabled = True),
                    dcc.Interval(id = "led-interval", disabled = True),
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
                    dcc.Store(id = "led-current-mode"),
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