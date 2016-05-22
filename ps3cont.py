#!/usr/bin/python
import threading
import sys
import dualshock3 as ds3
import ev3dev.ev3 as ev3


gamepad = ds3.Controller()
if not gamepad.connect():
    print "Could not connect to PS3 controller"
    sys.exit(1)


running = True
speedA = 0
speedB = 0
NOISEUP = 170
NOISEDWN = 90


class MotorThread(threading.Thread):
    motorA = ev3.LargeMotor('outA')
    motorB = ev3.LargeMotor('outB')
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print "Engine running!"
        while running:
                self.motorA.run_forever(duty_cycle_sp=speedA)
                self.motorB.run_forever(duty_cycle_sp=speedB)

        self.motorA.stop()
        self.motorB.stop()


motor_thread = MotorThread()
motor_thread.setDaemon(True)
motor_thread.start()


for event in gamepad.read_loop():
    rawinput = event.raw_event.value
    if event.stick_moved(ds3.RT_STICK, ds3.Y_AXIS):
        if rawinput < NOISEDWN or rawinput > NOISEUP:
            speedA = event.get_speed()
        else:
            speedA = 0
    elif event.stick_moved(ds3.LT_STICK, ds3.Y_AXIS):
        if rawinput < NOISEDWN or rawinput > NOISEUP:
            speedB = event.get_speed()
        else:
            speedB = 0
    elif event.btn_down(ds3.BTN_X):
        print "SHUTTING DOWN"
        running = False
        break
