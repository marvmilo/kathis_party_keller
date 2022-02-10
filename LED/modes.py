import threading
import time
import rpi_ws281x as led

# LED strip configuration:
LED_COUNT      = 150      # Number of LED pixels.
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
    print("single")
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
    print("two_color")
    #values
    blur_max = 150
    blur = int(blur_max * input_vals.blur_factor)
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
    print("pulse")
    
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

        #reset interval
        # if i > ticks:
        #     i = 0
        
        # #set color
        # if i <= steps:
        #     color = [int(c*(i/steps)) for c in input_vals.color[0]]
        # else:
        #     color = [int(c*(1 - ((i - steps)/steps))) for c in input_vals.color[0]]
        # for p in range(strip.numPixels()):
        #     strip.setPixelColor(p, led.Color(*color))
        # strip.show()
            
        # i += 1
        #check for end of thread
        if pipe.exit:
            pipe.done = True
            break

# shoot mode function
def shoot(input_vals, pipe):
    print("shoot")
    #values
    i = 0
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
    i = 0
    
    while True:
        print("rainbow", i)
        i += 1
        
        time.sleep(1)
        #check for end of thread
        if pipe.exit:
            pipe.done = True
            break

# audio_pegel mode function
def audio_pegel(input_vals, pipe):
    i = 0
    
    while True:
        print("audio_pegel", i)
        i += 1
        
        time.sleep(1)
        #check for end of thread
        if pipe.exit:
            pipe.done = True
            break

# audio_shoot mode function
def audio_shoot(input_vals, pipe):
    i = 0
    
    while True:
        print("audio_shoot", i)
        i += 1
        
        time.sleep(1)
        #check for end of thread
        if pipe.exit:
            pipe.done = True
            break

# audio_brightness mode function
def audio_brightness(input_vals, pipe):
    i = 0
    
    while True:
        print("audio_brightness", i)
        i += 1
        
        time.sleep(1)
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