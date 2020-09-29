#!/usr/bin/env pybricks-micropython

# Own imports
from common import *

# Motor ports
motor_angle = Motor(Port.B)
motor_missile = Motor(Port.A)

l1down = False
r1down = False
l2down = False
r2down = False

# Event handler, called from common.py
def on_event(event):
    global l1down, r1down, l2down, r2down

    # Adjusting rotation & hammer motor voltage based on analog stick input
    if event.type == EVENT_ANALOG:
        #if event.code == ANALOG_LEFT_HORIZONTAL: 
            
        if event.code == ANALOG_LEFT_VERTICAL:    #shooter
           # print(event.value)
            if  event.value < 125:
                motor_angle.track_target(((event.value - 125)/125)*150)
            else:
                motor_angle.track_target(0)
        elif event.code == ANALOG_RIGHT_HORIZONTAL:
            motor_missile.dc(scale(event.value))

    if event.type == EVENT_BUTTON:
        print(event.value)
        
       
# _Cleanup function, called from common.py
def on_cleanup():
    motor_missile.dc(0)

# Entering main loop, defined in common.py
main_loop(on_event, on_cleanup)