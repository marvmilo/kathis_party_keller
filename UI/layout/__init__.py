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
                width = "1200px",
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
                    dbc.Carousel(id = "home-carousel", items = [])
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