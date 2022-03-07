from rpi_ws281x import *
import threading
import time
import marvmiloTools as mmt

#import other scripts
import modes

#load vals
settings_file = "./LED/settings.json"
input_file = "./LED/input.json"
settings = mmt.json.load(settings_file)
last_input = dict()
updater_pipe = mmt.dictionary.toObj({"exit": False, "done": True})

#main loop
while True:
    #getting input
    input_vals = mmt.json.load(input_file)
    #check for change in input
    if not list(input_vals.values()) == list(last_input.values()):
        last_input = input_vals
        #start thread with current input
        updater_pipe.exit = True
        while not updater_pipe.done:
            time.sleep(1)
        updater_pipe.exit, updater_pipe.done = False, False
        function = getattr(modes, input_vals.mode)
        updater_thread = modes.Thread(function, input_vals, updater_pipe)
        updater_thread.start()
    time.sleep(1)