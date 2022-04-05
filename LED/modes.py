import threading
import time
import rpi_ws281x as led

# import sys
# sys.setrecursionlimit(100)

#import other scripts
import audio

# LED strip configuration:
LED_COUNT      = 125      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

#init LED strip
strip = led.Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

# single mode function
def single(input_vals, pipe):
    #set color
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, led.Color(*input_vals.color[0]))
    strip.show()
    
    #check for end of thread
    while True:
        time.sleep(1)
        if pipe.exit:
            pipe.done = True
            break
    
# two color mode function
def two_color(input_vals, pipe):
    #values
    blur_max = strip.numPixels()
    blur = int(blur_max * input_vals.blur_factor)
    if not blur:
        blur = 0.1
    static_area = int((blur_max - blur) / 2)
    
    #set colors
    for i in range(strip.numPixels()):
        if i < static_area:
            strip.setPixelColor(i, led.Color(*input_vals.color[0]))
        elif i < strip.numPixels() - static_area:
            color1 = [int((c * (1- ((i - static_area) / blur)))/2) for c in input_vals.color[0]]
            color2 = [int((c * ((i - static_area) / blur))/2) for c in input_vals.color[1]]
            color = [c1 + c2 for c1, c2 in zip(color1, color2)]
            strip.setPixelColor(i, led.Color(*color))
        else:
            strip.setPixelColor(i, led.Color(*input_vals.color[1]))
    strip.show()
    
    #check for end of thread
    while True:
        time.sleep(1)
        if pipe.exit:
            pipe.done = True
            break

# pulse mode function
def pulse(input_vals, pipe):
    #values
    i = 0
    interval_min = 0.1
    interval_max = 10
    interval = ((interval_max - interval_min) * input_vals.interval) + interval_min
    interval_last = time.time()
    color1 = input_vals.color[0]
    color2 = input_vals.color[1]
    
    while True:
        interval_current = time.time() - interval_last
        if interval_current < interval/2:
            factor = interval_current / (interval/2)
            color = [int(abs(c1*factor + (c2*(1-factor)))) for c1, c2 in zip(color1, color2)]
            #set color
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, led.Color(*color))
            strip.show()
        else:
            interval_last = time.time()
            color1, color2 = color2, color1

        #check for end of thread
        if pipe.exit:
            pipe.done = True
            break

# shoot mode function
def shoot(input_vals, pipe):
    #values
    colors = [input_vals.color[1] for i in range(strip.numPixels())]
    color = input_vals.color[0]
    blur_color = input_vals.color[1]
    interval_min = 0.1
    interval_max = 5
    interval = ((interval_max - interval_min) * input_vals.interval) + interval_min
    interval_last = time.time()
    fade_out_min = 0.25
    fade_out_max = 15
    fade_out = ((fade_out_max - fade_out_min) * (input_vals.fade_out)) + fade_out_min
    time_per_pixel = fade_out / strip.numPixels()
    move_last = time.time()
    move_interval = 0
    blur_time = interval * input_vals.blur_factor / 2
    
    while True:
        #change color at interval
        if (time.time() - interval_last) >= (interval / 2):
            if color ==  input_vals.color[0]:
                color = input_vals.color[1]
                blur_color = input_vals.color[0]
            else:
                color = input_vals.color[0]
                blur_color = input_vals.color[1]
            interval_last = time.time()
        
        #insert color
        move_interval += time.time() - move_last
        move_last = time.time()
        move_leds = int(move_interval / time_per_pixel)
        move_interval = move_interval % time_per_pixel
        for l in range(move_leds):
            current_intervall = time.time() - interval_last
            blured_color = color
            if current_intervall < blur_time:
                #print(current_intervall)
                try:
                    blur_factor = current_intervall / blur_time
                except ZeroDivisionError:
                    blur_factor = 0
                blured_color = [int(abs(c1*blur_factor + (c2*(1-blur_factor)))) for c1, c2 in zip(color, blur_color)]
            colors.insert(0, blured_color)
            del colors[-1]
        
        #set colors
        for p, c in enumerate(colors):
            strip.setPixelColor(p, led.Color(*c))
        strip.show()
        
        #check for end of thread
        if pipe.exit:
            pipe.done = True
            break
    
# rainbow mode function
def rainbow(input_vals, pipe):
    #values
    interval_min = 1
    interval_max = 30
    interval = (((interval_max - interval_min) * input_vals.interval) + interval_min)/256
    interval_last = time.time()

    #rainbowwheel
    def wheel(pos):
        if pos < 85:
            return led.Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return led.Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return led.Color(0, pos * 3, 255 - pos * 3)
    
    while True:
        #set colors
        for j in range(256):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
            strip.show()
            while True:
                current_interval = time.time() - interval_last
                if current_interval >= interval:
                    interval_last = time.time()
                    break
        
            #check for end of thread
            if pipe.exit:
                pipe.done = True
                break
        #check for end of thread
        if pipe.exit:
            pipe.done = True
            break

# audio_pegel mode function
def audio_pegel(input_vals, pipe):
    #declared values
    max_blur = 100
    blur = int(input_vals.blur_factor * max_blur)

    #prepare audio
    audio.fade_out = input_vals.fade_out

    while True:
        try:
            leds = int((strip.numPixels() + blur) * audio.percentage)
        except ValueError:
            leds = 0

        #set color
        for i in range(-blur, strip.numPixels()):
            if i >= 0:
                if i < (leds - blur):
                    strip.setPixelColor(i, led.Color(*input_vals.color[0]))
                elif i < (leds):
                    blur_factor = (leds - i)/blur
                    color = [int(abs(c1*blur_factor + (c2*(1-blur_factor)))) for c1, c2 in zip(input_vals.color[0], input_vals.color[1])]
                    strip.setPixelColor(i, led.Color(*color))
                else:
                    strip.setPixelColor(i, led.Color(*input_vals.color[1]))
        strip.show()

        #check for end of thread
        if pipe.exit:
            pipe.done = True
            break

# audio_shoot mode function
def audio_shoot(input_vals, pipe):
    #values
    colors = [input_vals.color[1] for i in range(strip.numPixels())]
    color = input_vals.color[0]
    blur_color = input_vals.color[1]
    interval_min = 0.1
    interval_max = 2
    interval = ((interval_max - interval_min) * input_vals.interval) + interval_min
    interval_last = time.time()
    fade_out_min = 0.25
    fade_out_max = 7.5
    fade_out = ((fade_out_max - fade_out_min) * (input_vals.fade_out)) + fade_out_min
    time_per_pixel = fade_out / strip.numPixels()
    move_last = time.time()
    move_interval = 0
    blur_time = interval * input_vals.blur_factor / 2

    while True:
        audio_perc = audio.percentage

        #check for shoot
        try:
            if audio_perc >= last_audio_perc + 0.25:
                color = [int(abs(c1*audio_perc + (c2*(1-audio_perc)))) for c1, c2 in zip(input_vals.color[0], input_vals.color[1])]
                blur_color = input_vals.color[1]
                interval_last = time.time()
        except NameError:
            pass
        last_audio_perc = audio_perc


        #change color at interval
        if (time.time() - interval_last) >= (interval / 2):
            color = input_vals.color[1]
            blur_color = [int(abs(c1*audio_perc + (c2*(1-audio_perc)))) for c1, c2 in zip(input_vals.color[0], input_vals.color[1])]
        
        #insert color
        move_interval += time.time() - move_last
        move_last = time.time()
        move_leds = int(move_interval / time_per_pixel)
        move_interval = move_interval % time_per_pixel
        for l in range(move_leds):
            current_intervall = time.time() - interval_last
            blured_color = color
            if current_intervall < blur_time:
                #print(current_intervall)
                try:
                    blur_factor = current_intervall / blur_time
                except ZeroDivisionError:
                    blur_factor = 0
                blured_color = [int(abs(c1*(1-blur_factor) + (c2*blur_factor))) for c1, c2 in zip(color, blur_color)]
            colors.insert(0, blured_color)
            del colors[-1]
        
        #set colors
        for p, c in enumerate(colors):
            strip.setPixelColor(p, led.Color(*c))
        strip.show()

        #check for end of thread
        if pipe.exit:
            pipe.done = True
            break

# audio_brightness mode function
def audio_brightness(input_vals, pipe):
    #prepare audio
    audio.fade_out = input_vals.fade_out

    while True:
        audio_perc = audio.percentage
        color = [int(abs(c1*audio_perc + (c2*(1-audio_perc)))) for c1, c2 in zip(input_vals.color[0], input_vals.color[1])]
        #set color
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, led.Color(*color))
        strip.show()

        #check for end of thread
        if pipe.exit:
            pipe.done = True
            break
    
# thread for running modes
class Thread(threading.Thread):
    def __init__(self, function, input_vals, pipe):
        threading.Thread.__init__(self)
        self.function = function
        self.input_vals = input_vals
        self.pipe = pipe
    def run(self):
        self.function(self.input_vals, self.pipe)