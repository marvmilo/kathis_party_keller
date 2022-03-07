import dash
import dash_auth
import dash_bootstrap_components as dbc
import marvmiloTools as mmt

#import other scripts
import layout
import callbacks

#declare vals
settings = mmt.json.load("./settings.json")

#init app
app = dash.Dash(
    title = settings.name,
    meta_tags = [mmt.dash.mobile_optimization],
    external_stylesheets = [dbc.themes.DARKLY],
    update_title = False
)
auth = dash_auth.BasicAuth(app, mmt.dictionary.toDict(settings.creds))
app.layout = (layout.structure(settings))
callbacks.init(app, layout)

#run web application
app.run_server(
    debug = settings.debug, 
    host = "0.0.0.0",
    port = settings.port
)