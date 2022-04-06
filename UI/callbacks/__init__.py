import marvmiloTools as mmt
from dash.dependencies import Input, Output, State

#import other scirpts
from . import general
from . import home
from . import led

def init(app, layout):
    #navbar toggler callback
    @app.callback(*mmt.dash.nav.callback_args)
    def cn(n, is_open):
        return mmt.dash.nav.callback_function(n, is_open)

    #page location callback
    @app.callback(
        Output("main-content", "children"),
        Input("url", "pathname")
    )
    def cl(path):
        return general.location.callback(path, layout)
    
    #load home carousel
    @app.callback(
        [Output("home-polaroid-carousel", "items")],
        [Input("home-trigger", "children")]
    )
    def callback1(trigger):
        return home.load_polaroid_pics.callback(trigger)
    
    #update polaroid date
    @app.callback(
        [Output("home-polaroid-date", "children"),
         Output("home-polaroid-interval", "disabled")],
        [Input("home-polaroid-carousel", "active_index"),
         Input("home-polaroid-interval", "n_intervals")],
        [State("home-polaroid-date", "children"),
         State("home-polaroid-carousel", "items")]
    )
    def callback2(active, interval, current_date, items):
        return home.load_polaroid_dates.callback(active, interval, current_date, items)
    
    #load home rules carousel
    @app.callback(
        [Output("home-rules-carousel", "items")],
        [Input("home-trigger", "children")]
    )
    def callback3(trigger):
        return home.load_rules_svgs.callback(trigger)
    
    #change led mode
    @app.callback(
        [Output("led-single-select", "value"),
         Output("led-two_color-select", "value"),
         Output("led-pulse-select", "value"),
         Output("led-shoot-select", "value"),
         Output("led-rainbow-select", "value"),
         Output("led-audio_pegel-select", "value"),
         Output("led-audio_brightness-select", "value"),
         Output("led-audio_shoot-select", "value"),
         Output("led-current-mode", "data")],
        [Input("led-single-select", "value"),
         Input("led-two_color-select", "value"),
         Input("led-pulse-select", "value"),
         Input("led-shoot-select", "value"),
         Input("led-rainbow-select", "value"),
         Input("led-audio_pegel-select", "value"),
         Input("led-audio_brightness-select", "value"),
         Input("led-audio_shoot-select", "value")],
        [State("led-current-mode", "data")]
    )
    def callback4(v0, v1, v2, v3, v4, v5, v6, v7, current):
        return led.change_mode.callback(v0, v1, v2, v3, v4, v5, v6, v7, current)
    
    #load current values
    @app.callback(
        [Output("led_color_1_picker", "value"),
         Output("led_color_2_picker", "value"),
         Output("led-blur_factor-slider", "value"),
         Output("led-interval-slider", "value"),
         Output("led-fade_out-slider", "value")],
        [Input("led-trigger", "children")]
    )
    def callback5(trigger):
        return led.initial_load.callback(trigger)
    
    #set led behavior
    @app.callback(
        [Output("led-changed-behavior-modal", "is_open"),
         Output("led-set-behavior", "n_clicks")],
        [Input("led-set-behavior", "n_clicks"),
         Input("led-changed-behavior-modal-close", "n_clicks"),
         Input("led-changed-behavior-modal-ok", "n_clicks")],
        [State("led-single-select", "value"),
         State("led-two_color-select", "value"),
         State("led-pulse-select", "value"),
         State("led-shoot-select", "value"),
         State("led-rainbow-select", "value"),
         State("led-audio_pegel-select", "value"),
         State("led-audio_brightness-select", "value"),
         State("led-audio_shoot-select", "value"),
         State("led_color_1_picker", "value"),
         State("led_color_2_picker", "value"),
         State("led-blur_factor-slider", "value"),
         State("led-interval-slider", "value"),
         State("led-fade_out-slider", "value")]
    )
    def callback6(n_set, n_close, n_ok, v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12):
        return led.set_behavior.callback(n_set, n_close, n_ok, v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12)

    #block input for specific mode
    @app.callback(
        [Output("led-color1-div", "style"),
         Output("led-color2-div", "style"),
         Output("led-blur_factor-div", "style"),
         Output("led-interval-div", "style"),
         Output("led-fade_out-div", "style"),],
        [Input("led-single-select", "value"),
         Input("led-two_color-select", "value"),
         Input("led-pulse-select", "value"),
         Input("led-shoot-select", "value"),
         Input("led-rainbow-select", "value"),
         Input("led-audio_pegel-select", "value"),
         Input("led-audio_brightness-select", "value"),
         Input("led-audio_shoot-select", "value"),
         Input("led-trigger", "children")]
    )
    def callback7(v0, v1, v2, v3, v4, v5, v6, v7, trigger):
        return led.disable_input.callback(v0, v1, v2, v3, v4, v5, v6, v7, trigger)
    
    #rende previews
    @app.callback(
        [Output("led-single-select-preview", "children"),
         Output("led-two_color-select-preview", "children"),
         Output("led-pulse-select-preview", "children"),
         Output("led-shoot-select-preview", "children"),
         Output("led-rainbow-select-preview", "children"),
         Output("led-audio_pegel-select-preview", "children"),
         Output("led-audio_brightness-select-preview", "children"),
         Output("led-audio_shoot-select-preview", "children")],
        [Input("led-single-select", "value"),
         Input("led-two_color-select", "value"),
         Input("led-pulse-select", "value"),
         Input("led-shoot-select", "value"),
         Input("led-rainbow-select", "value"),
         Input("led-audio_pegel-select", "value"),
         Input("led-audio_brightness-select", "value"),
         Input("led-audio_shoot-select", "value"),
         Input("led_color_1_picker", "value"),
         Input("led_color_2_picker", "value"),
         Input("led-blur_factor-slider", "value"),
         Input("led-interval-slider", "value"),
         Input("led-fade_out-slider", "value"),
         Input("led-interval", "n_intervals")]
    )
    def callback8(v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, interval):
        return led.show_preview.callback(v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, interval)