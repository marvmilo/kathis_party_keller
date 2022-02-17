import time

#import other scripts
import LED

#start led thread function
def start_LED_Thread():
    LED_thread = LED.Thread()
    LED_thread.start()
    return LED_thread

#starting led thread
LED_thread = start_LED_Thread()

#main loop
try:
    while True:
        time.sleep(1)
        LED_thread.is_alive()
except KeyboardInterrupt:
    exit()