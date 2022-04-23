import dash
import dash_auth
import dash_bootstrap_components as dbc
import marvmiloTools as mmt

#import other scripts
import layout
import callbacks
import rules

#declare vals
settings = mmt.json.load("/home/pi/scripts/UI/settings.json")
credentials = mmt.json.load("/home/pi/scripts/UI/credentials.json")
user_pw_dict = {u.name:u.pw for u in credentials.values()}

#init app
app = dash.Dash(
    title = settings.name,
    meta_tags = [mmt.dash.mobile_optimization],
    external_stylesheets = [
        dbc.themes.DARKLY,
        'https://fonts.googleapis.com/css2?family=Amatic+SC:wght@700&family=Permanent+Marker&display=swap'
    ],
    update_title = False
)
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
auth = dash_auth.BasicAuth(app, user_pw_dict)
app.layout = (layout.structure(settings))
callbacks.init(app, layout)
rules.init()

#run web application
app.run_server(
    debug = settings.debug, 
    host = "0.0.0.0",
    port = settings.port,
    dev_tools_hot_reload = False
)