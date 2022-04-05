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
    
    #set led mode
    @app.callback(
        [Output("led-single-select", "value"),
         Output("led-two_color-select", "value"),
         Output("led-pulse-select", "value"),
         Output("led-shoot-select", "value"),
         Output("led-rainbow-select", "value"),
         Output("led-audio_pegel-select", "value"),
         Output("led-audio_brightness-select", "value"),
         Output("led-audio_shoot-select", "value")],
        [Input("led-single-select", "value"),
         Input("led-two_color-select", "value"),
         Input("led-pulse-select", "value"),
         Input("led-shoot-select", "value"),
         Input("led-rainbow-select", "value"),
         Input("led-audio_pegel-select", "value"),
         Input("led-audio_brightness-select", "value"),
         Input("led-audio_shoot-select", "value"),
         Input("led-interval", "n_intervals")]
    )
    def callback4(v0, v1, v2, v3, v4, v5, v6, v7, interval):
        return led.select_mode.callback(v0, v1, v2, v3, v4, v5, v6, v7, interval)
    
    #set led color
    @app.callback(
        [Output("led_color_1_picker", "value"),
         Output("led_color_2_picker", "value")],
        [Input("led_color_1_picker", "value"),
         Input("led_color_2_picker", "value"),
         Input("led-interval", "n_intervals")]
    )
    def callback5(color_1_val, color_2_val, interval):
        return led.select_color.callback(color_1_val, color_2_val, interval)
    
    #set led blur factor
    @app.callback(
        [Output("led-blur_factor-slider", "value")],
        [Input("led-blur_factor-slider", "value"),
         Input("led-interval", "n_intervals")]
    )
    def callback6(value, interval):
        return led.select_slider.callback(value, interval, "blur_factor")
    
    #set led interval
    @app.callback(
        [Output("led-interval-slider", "value")],
        [Input("led-interval-slider", "value"),
         Input("led-interval", "n_intervals")]
    )
    def callback7(value, interval):
        return led.select_slider.callback(value, interval, "interval")
    
    #set led fade_out
    @app.callback(
        [Output("led-fade_out-slider", "value")],
        [Input("led-fade_out-slider", "value"),
         Input("led-interval", "n_intervals")]
    )
    def callback8(value, interval):
        return led.select_slider.callback(value, interval, "fade_out")