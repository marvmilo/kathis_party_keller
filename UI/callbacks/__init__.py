import marvmiloTools as mmt
from dash.dependencies import Input, Output, State
import shutil
import os

#import other scirpts
from . import general
from . import home
from . import led

def init(app, layout):
    #cleanup old files
    preview_folder = "./assets/previews"
    try:    
        shutil.rmtree(preview_folder)
    except FileNotFoundError:
        pass
    os.mkdir(preview_folder)
    
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
    
    #render previews
    @app.callback(
        [Output("led-single-select-preview", "children"),
         Output("led-two_color-select-preview", "children"),
         Output("led-pulse-select-preview", "children"),
         Output("led-shoot-select-preview", "children"),
         Output("led-rainbow-select-preview", "children"),
         Output("led-audio_pegel-select-preview", "children"),
         Output("led-audio_brightness-select-preview", "children"),
         Output("led-audio_shoot-select-preview", "children"),
         Output("led-preview", "children"),
         Output("led-previous-preview", "data"),
         Output("led-preview-interval-div-2", "children")],
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
         Input("led-fade_out-slider", "value")],
        [State("led-preview-id", "data"),
         State("led-previous-preview", "data")]
    )
    def callback8(v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, id, last):
        return led.render_preview.callback(v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, id, last, led.mode_loading_content, led.preview_interval_enabled, led.image)
    
    #show previews
    @app.callback(
        [Output("led-single-gif-preview", "children"),
         Output("led-two_color-gif-preview", "children"),
         Output("led-pulse-gif-preview", "children"),
         Output("led-shoot-gif-preview", "children"),
         Output("led-rainbow-gif-preview", "children"),
         Output("led-audio_pegel-gif-preview", "children"),
         Output("led-audio_brightness-gif-preview", "children"),
         Output("led-audio_shoot-gif-preview", "children"),
         Output("led-gif-preview", "children"),
         Output("led-preview-loaded", "data")],
        [Input("led-preview-interval", "n_intervals")],
        [State("led-preview-id", "data")]
    )
    def callback9(interval, id):
        return led.show_preview.callback(interval, id, led.mode_loading_content, led.image)
    
    #cleanup preview loading
    @app.callback(
        [Output("led-preview-interval-div-1", "children")],
        [Input("led-preview-loaded", "data")],
        [State("led-preview-id", "data")]
    )
    def callback10(data, id):
        return led.cleanup_preview.callback(data, id, led.preview_interval_disabled)
    
    #pop up shutdown modal
    @app.callback(
        [Output("shutdown-modal", "is_open"),
         Output("shutdown-button", "n_clicks")],
        [Input("shutdown-button", "n_clicks"),
         Input("shutdown-modal-close", "n_clicks"),
         Input("shutdown-modal-yes", "n_clicks"),
         Input("shutdown-modal-no", "n_clicks")]
    )
    def callback11(n_shutdown, n_close, n_yes, n_no):
        return general.shutdown_modal.callback(n_shutdown, n_close, n_yes, n_no)
    
    #pop up shutting down modal
    @app.callback(
        [Output("shutting-down-modal", "is_open")],
        [Input("shutdown-modal-yes", "n_clicks")]
    )
    def callback12(n_clicks):
        return general.shutting_down_modal.callback(n_clicks)
    
    #shutdown
    @app.callback(
        [Output("shutdown-dummy", "children")],
        [Input("shutting-down-modal", "is_open")]
    )
    def callback13(is_open):
        return general.shutdown.callback(is_open)
    
    #turn on/off light
    @app.callback(
        [Output("light-button", "color"),
         Output("light-button", "n_clicks")],
        [Input("light-button", "n_clicks"),
         Input("light-interval", "n_intervals"),
         Input("session-id", "data")]
    )
    def callback14(n_clicks, n_intervals, id):
        return general.light.callback(n_clicks, n_intervals, id)

    #init accordion item
    @app.callback(
        [Output("led-accordion", "active_item")],
        [Input("led-trigger", "children")]
    )
    def callback15(trigger):
        return led.accordion_init.callback(trigger)
    
    #pop up interaction denied modal
    @app.callback(
        [Output("interaction-denied-modal", "is_open"),
         Output("interaction-denied-modal-init", "data")],
        [Input("shutdown-button", "n_clicks"),
         Input("light-button", "n_clicks"),
         Input("led-set-behavior", "n_clicks"),
         Input("interaction-denied-modal-close", "n_clicks"),
         Input("interaction-denied-modal-ok", "n_clicks")],
        [State("interaction-denied-modal", "is_open"),
         State("interaction-denied-modal-init", "data")]
    )
    def callback16(n_shutdown, n_light, n_led, n_close, n_ok, is_open, init):
        return general.interaction_denied.callback(n_shutdown, n_light, n_led, n_close, n_ok, is_open, init)
