# PicoSMARS
# A MircoPython version of the SMARS robot, also for the SMARS Mini

from machine import Pin, PWM, I2C
from smars import SMARS


# I2C
sda = Pin(0)
scl = Pin(1)
id = 0

# create the i2c object
i2c = I2C(id=0, sda=sda, scl=scl) 

robot = SMARS(i2c=i2c)

def avoid():
    while True:
        if robot.distance >= 5:
            robot.forward()
            print('forward',robot.distance)
        else:
            robot.backward()
            robot.turnright()
            print('backward',robot.distance)

def motor_test():
    while True:
        robot.forward()