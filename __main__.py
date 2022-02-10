import pyaudio
import numpy as np
import marvmiloTools as mmt

#values
settings = mmt.json.load("settings.json")
peak = mmt.dictionary.toObj({
    "value": None,
    "last": 0,
    "min": None,
    "max": None,
    "range": None,
    "perc": 0
})

#init pyaudio
p = pyaudio.PyAudio()
stream = p.open(
    format = pyaudio.paInt16,
    channels = settings.pyaudio.channels,
    rate = settings.pyaudio.rate,
    input = True,
    frames_per_buffer = settings.pyaudio.chunk
)

#main loop
try:
    while True:
        data = np.fromstring(stream.read(settings.pyaudio.chunk, exception_on_overflow = False), dtype = np.int16)
        
        #visualize
        peak.value = np.average(np.abs(data))**2
        if not peak.min and not peak.max:
            peak.min, peak.max = peak.value, peak.value
        elif peak.value < peak.min:
            peak.min = peak.value
        elif peak.value > peak.max:
            peak.max = peak.value
        peak.range = peak.max - peak.min
        peak.value = peak.value - peak.min
        
        #set behaviour
        max_decrease = peak.range * settings.behaviour.max_decrease_percentage/100
        if not peak.max - max_decrease < settings.behaviour.max_minimum:
            peak.max -= max_decrease
        else:
            peak.max = settings.behaviour.max_minimum
        peak_decrease = peak.range * settings.behaviour.peak_decrease_percentage/100
        if peak.last - peak_decrease > peak.value:
            peak.value = peak.last - peak_decrease
        
        #set values
        peak.last = peak.value
        peak.perc = peak.value / peak.range
        
        #display
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
        
except KeyboardInterrupt:
    stream.stop_stream()
    stream.close()
    p.terminate()