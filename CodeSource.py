from microbit import *

time = 0
running = False

while True:

    if button_a.was_pressed():
   
        if running:
            running = False
      
        else:
            running = True
    
    if button_b.was_pressed():

        if running:
            time = 0

        else:
            time = 0

    if running:
        time += 1
    
    display.show(str(time))
    sleep(1000)