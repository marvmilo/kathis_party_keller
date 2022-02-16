import pyaudio
import numpy as np
import marvmiloTools as mmt
import threading

#values
settings = mmt.json.load("./LED/audio/settings.json")
peak = mmt.dictionary.toObj({
    "value": None,
    "last": 0,
    "min": None,
    "max": None,
    "range": None,
    "perc": 0
})
percentage = 0
fade_out = 0

#init pyaudio
p = pyaudio.PyAudio()
stream = p.open(
    format = pyaudio.paInt16,
    channels = settings.pyaudio.channels,
    rate = settings.pyaudio.rate,
    input = True,
    frames_per_buffer = settings.pyaudio.chunk
)

def main():
    global percentage

    while True:
        data = np.fromstring(stream.read(settings.pyaudio.chunk, exception_on_overflow = False), dtype = np.int16)
        
        #visualize
        peak.value = np.average(np.abs(data))**2
        if not peak.min and not peak.max:
            peak.min, peak.max = peak.value, peak.value
        if peak.value < peak.min:
            if peak.value > settings.behaviour.minimum:
                peak.min = peak.value
            else:
                peak.min = settings.behaviour.minimum
        if peak.value > peak.max:
            if peak.value > settings.behaviour.minimum:
                peak.max = peak.value
            else:
                peak.max = settings.behaviour.minimum
        peak.range = peak.max - peak.min
        peak.value = peak.value - peak.min
        if peak.value < 0:
            peak.value = 0
        
        # decrease max values
        max_decrease = peak.range * settings.behaviour.max_decrease_percentage
        peak.max -= max_decrease

        #flat led noise
        max_change_perc = settings.behaviour.max_change_percentage
        change_perc = abs(peak.last - peak.value)/peak.range
        if change_perc > settings.behaviour.skip_percentage:
            pass
        elif peak.value > peak.last:
            peak.value = peak.last * (1+max_change_perc)
        else:
            peak.value = peak.last * (1-max_change_perc)
        
        #set fade out
        fade_out_percentage = (settings.behaviour.max_peak_decrease_percentage - settings.behaviour.min_peak_decrease_percentage) * fade_out
        peak_decrease = peak.range * (settings.behaviour.max_peak_decrease_percentage - fade_out_percentage)
        if peak.last - peak_decrease > peak.value:
            peak.value = peak.last - peak_decrease
        
        #set values
        peak.last = peak.value
        peak.perc = peak.value / peak.range
        if peak.perc > 1:
            peak.perc = 1
        if peak.value < peak.min:
            peak.perc = 0
        
        #display
        if settings.debug.status:
            out_str = ""
            spacing = settings.debug.spacing
            rounding = settings.debug.rounding
            total_bars = settings.debug.bars
            out_str += f"MIN: {round(peak.min, rounding)}".ljust(spacing, " ")
            out_str += f"MAX: {round(peak.max, rounding)}".ljust(spacing, " ")
            out_str += f"VALUE: {round(peak.value, rounding)}".ljust(spacing, " ")
            out_str += f"Percentage: {round(peak.perc*100, rounding)}%".ljust(spacing, " ")
            if not np.isnan(peak.perc):
                bar_count = int(total_bars * peak.perc)
            else:
                bar_count = 0
            bars = bar_count * settings.debug.bar_symbol
            empty = (total_bars - bar_count) * " "
            out_str += f"|{bars}{empty}|".ljust(spacing, " ")
            print(out_str)
        percentage = peak.perc

#creating thread
class Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        main()