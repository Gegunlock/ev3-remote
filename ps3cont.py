#!/usr/bin/python

import sys
import dualshock3 as ds3
import ev3dev.ev3 as ev3

gamepad = ds3.Controller()
if not gamepad.connect():
    print "Could not connect to PS3 controller"
    sys.exit(1)




##Controller has usually 15 or -15 while sticks not moved
NOISEUP = 153.5
NOISEDWN = 102.5
motorA = ev3.LargeMotor('outA')
motorB = ev3.LargeMotor('outB')

for event in gamepad.read_loop():
    rawinput = event.raw_event.value
    if event.stick_moved(ds3.RT_STICK, ds3.Y_AXIS):
       # speed = event.get_speed()*-1
        if rawinput < NOISEDWN or rawinput > NOISEUP:
            motorA.run_forever(duty_cycle_sp=event.get_speed())
           # motorB.run_forever(duty_cycle_sp=speed)
            print "Right"
           # print int(speed)
	else:
	    motorA.run_forever(duty_cycle_sp=0)
           # motorB.run_forever(duty_cycle_sp=0)
    if event.stick_moved(ds3.LT_STICK, ds3.Y_AXIS):
       # speed = event.get_speed()*-1
       # if speed > NOISE or speed < (NOISE*-1):
	if rawinput < NOISEDWN or rawinput > NOISEUP:
            motorB.run_forever(duty_cycle_sp=event.get_speed())
            print "Left"
           # print int(speed)
        else:
            motorB.run_forever(duty_cycle_sp=0)    
#    elif event.stick_moved(ds3.RT_STICK, ds3.X_AXIS):
#        speed = event.get_speed()
#        if speed > NOISE:
#            motorA.run_forever(duty_cycle_sp=speed)
#            print "X-axjs"
#            print int(speed)
#    elif event.stick_moved(ds3.RT_STICK, ds3.X_AXIS):
#        speed = event.get_speed()
#        if speed < (NOISE*-1):
#            motorB.run_forever(duty_cycle_sp=speed)
#            print "X-axjs"
#            print int(speed)
    elif event.btn_down(ds3.BTN_X):
        print "SHUTTING DOWN"
        sys.exit(1)
