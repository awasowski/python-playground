import time
from threading import Timer

def create_timer_callback(message):
    def timer_callback():
        print(f"Timer finished with message: {message}")
    return timer_callback


# Create timers with different messages
timer1 = Timer(2, create_timer_callback("Hello from Timer 1!"))
timer2 = Timer(4, create_timer_callback("Hello from Timer 2!"))

# Start the timers
timer1.start()
timer2.start()

# Wait for the timers to finish
time.sleep(5)
