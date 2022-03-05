import dash
import dash_auth
from dash import html
import dash_bootstrap_components as dbc
import marvmiloTools as mmt

#declare vals
settings = mmt.json.load("./UI/settings.json")

#init app
app = dash.Dash(
    title = settings.name,
    meta_tags = [mmt.dash.mobile_optimization],
    external_stylesheets = [dbc.themes.DARKLY],
    update_title = False
)
auth = dash_auth.BasicAuth(app, mmt.dictionary.toDict(settings.creds))
app.layout = (html.Div("Hello world!"))

#run web application
app.run_server(
    debug = settings.debug, 
    host = "0.0.0.0",
    port = settings.port
)