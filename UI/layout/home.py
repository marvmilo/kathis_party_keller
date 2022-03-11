from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import marvmiloTools as mmt

#page content
def content():
    return html.Div(
        children = [
            html.Div(
                html.H1(html.B("Kathis Party Keller")),
                style = mmt.dash.flex_style()
            ),
            html.Br(),
            html.Div(
                html.Div(
                    children = [
                        dbc.Carousel(
                            items = [
                                {"key": "1", "src": "/assets/loading_carousel.jpg"}
                            ],
                            id = "home-carousel",
                            indicators = False,
                            style = {
                                "width": "100%",
                                "maxWidth": "30rem",
                                "padding": "1rem"
                            }
                        ),
                        html.Div(
                            html.H1(
                                "-",
                                id = "home-polaroid-date"
                            ),
                            style = mmt.dash.flex_style(
                                {
                                    "color": "black",
                                    "padding-bottom": "1rem",
                                    "fontFamily": "'Permanent Marker', cursive"
                                }
                            )
                        ),
                        dcc.Interval(
                            id = "home-polaroid-interval"
                        )
                    ],
                    style = {
                        "backgroundColor": "white",
                        "box-shadow": "10px 10px 5px #111111"
                    }
                ),
                style = mmt.dash.flex_style()
            ),
            html.Div(
                True,
                id = "home-trigger",
                style = {"display": "none"}
            )
        ]
    )