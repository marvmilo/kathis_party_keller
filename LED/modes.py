import threading
import time

# single mode function
def single(input_vals, pipe):
    print("single")
    
    #check for end of thread
    while True:
        time.sleep(1)
        if pipe.exit:
            pipe.done = True
            break
    
# two color mode function
def two_color(input_vals, pipe):
    print("two_color")
    
    #check for end of thread
    while True:
        time.sleep(1)
        if pipe.exit:
            pipe.done = True
            break

# pulse mode function
def pulse(input_vals, pipe):
    i = 0
    
    while True:
        print("pulse", i)
        i += 1
        
        time.sleep(1)
        #check for end of thread
        if pipe.exit:
            pipe.done = True
            break

# shoot mode function
def shoot(input_vals, pipe):
    i = 0
    
    while True:
        print("shoot", i)
        i += 1
        
        time.sleep(1)
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