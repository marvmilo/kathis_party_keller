import time

#import other scripts
import LED

#starting led thread
LED_thread = LED.Thread()
LED_thread.start()

#main loop
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    exit()