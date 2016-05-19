#!/usr/bin/python

import sys
import dualshock3 as ds3
import ev3dev.ev3 as ev3

gamepad = ds3.Controller()
if not gamepad.connect():
    print "Could not connect to PS3 controller"
    sys.exit(1)
    
NOISEUP = 153.5
NOISEDWN = 102.5
motorA = ev3.LargeMotor('outA')
motorB = ev3.LargeMotor('outB')

for event in gamepad.read_loop():
    rawinput = event.raw_event.value
    if event.stick_moved(ds3.RT_STICK, ds3.Y_AXIS):
        if rawinput < NOISEDWN or rawinput > NOISEUP:
            motorA.run_forever(duty_cycle_sp=event.get_speed())
        else:
            motorA.run_forever(duty_cycle_sp=0)
    if event.stick_moved(ds3.LT_STICK, ds3.Y_AXIS):
        if rawinput < NOISEDWN or rawinput > NOISEUP:
                motorB.run_forever(duty_cycle_sp=event.get_speed())
                print "Left"
        else:
            motorB.run_forever(duty_cycle_sp=0)
    elif event.btn_down(ds3.BTN_X):
        print "SHUTTING DOWN"
        sys.exit(1)
