# PicoSMARS
# A MircoPython version of the SMARS robot, also for the SMARS Mini

from machine import Pin, PWM, I2C
from smars import SMARS
from time import sleep

# I2C
sda = Pin(26)
scl = Pin(27)
id = 1

# create the i2c object
i2c = I2C(id=id, sda=sda, scl=scl) 

robot = SMARS(i2c=i2c)

def avoid():
    while True:
        print("I'm working")
        if robot.distance >= 5:
            robot.forward()
            print('forward',robot.distance)
        else:
            robot.backward()
            robot.turnright()
            print('backward',robot.distance)

def motor_test():
    while True:
        print("Testing left")
        robot.turnleft()
        sleep(0.25)
        print("Testing right")
        robot.turnright()
        sleep(0.25)
        print("Testing forward")
        robot.forward()
        sleep(0.25)
        print("Testing backward")
        robot.backward()
        sleep(0.25)

def motor_stop():
    robot.stop()

# motor_test()
avoid()
# motor_stop()
