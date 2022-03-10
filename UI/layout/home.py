from dash import html
import dash_bootstrap_components as dbc
import marvmiloTools as mmt

#page content
def content():
    return html.Div(
        children = [
            html.Br(),
            html.Div(
                html.H1(html.B("Kathis Party Keller")),
                style = mmt.dash.flex_style()
            ),
            html.Br(),
            html.Div(
                dbc.Carousel(
                    items = [
                        {"key": "1", "src": "/assets/loading_carousel.jpg"}
                    ],
                    id = "home-carousel",
                    indicators = False,
                    style = {
                        "width": "100%",
                        "maxWidth": "30rem"
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