import json
import marvmiloTools as mmt
from dash.exceptions import PreventUpdate

def callback(active, interval, current_date, items):
    items = mmt.dictionary.toObj(items)
    if current_date == "-" and not items[0].src.endswith("loading_carousel.jpg"):
        return [items[0].src[:-4].strip()[-10:], True]
    elif current_date != "-" and len(items):
        return [items[active].src[:-4].strip()[-10:], True]
    raise PreventUpdate