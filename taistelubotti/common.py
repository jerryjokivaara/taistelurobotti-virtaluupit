#!/usr/bin/env pybricks-micropython

# Pybricks imports
from pybricks.hubs import EV3Brick

ev3 = EV3Brick()
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 )
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase

# Own imports
from gamepad import *

# Converting from range (0,255) to (-100,100)
def scale(val):
    return 200 * float(val/255) - 100

# Converting from range (130,255) to (0,90))
def scale1(val):
    if val >= 130:
        return  90 * float(val/255) - 45

# Function playing beep sound
def beep():
    ev3.speaker.beep()

# Main loop, called from alaosa.py or ylaosa.py
def main_loop(on_event, on_cleanup):
  
    # Creating gamepad handler
    gamepad = Gamepad()

    # Beeping when ready
    ev3.speaker.play_notes(['E4/4', 'D4/4', 'C4/4', 'G4/4'])

    # Reading first event & entering event loop
    event = gamepad.next()
    while event:

        # Handling exit & connection test
        if event.type == EVENT_BUTTON and event.value == BUTTON_PRESS:
            
            # Exiting if options button is pressed
            if event.code == BUTTON_OPTIONS:
                break
            
            # Playing beep if share button is pressed
            elif event.code == BUTTON_SHARE:
              beep()
        
        # Running project specific event code
        on_event(event)
        
        # Reading next event
        event = gamepad.next()

    # Running project specific cleanup code
    on_cleanup()

    # Cleaning up gamepad
    gamepad.cleanup()

    # Beeping on shutdown
    ev3.speaker.play_notes(['C4/4', 'G4/4'])