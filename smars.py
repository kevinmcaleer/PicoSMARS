# SMARS class

from vl53l0x import VL53L0X
from machine import Pin
from time import sleep

class SMARS():
    name = ""

    def __init__(self, i2c, name = None, in1=None, in2=None, in3=None, in4=None):
        if in1 or in2 or in3 or in4 == None:
            in1 = 3 # Motor A Direction Input 1 1423
            in2 = 2 # Motor A Speed Input 2
            in3 = 0 # Motor B Direction Input 3
            in4 = 1 # Motor B Speed Input 4
        # Set the motor inputs on the L293D Motor Driver board
        self.motor_A_forward = Pin(in1, Pin.OUT)
        self.motor_A_reverse = Pin(in2, Pin.OUT)
        self.motor_B_forward = Pin(in3, Pin.OUT)
        self.motor_B_reverse = Pin(in4, Pin.OUT)
        if not name:
            self.name = "PicoSMARS"
        else:
            self.name = name

        self.i2c = i2c  
        if self.i2c.scan() == []:
            
            raise RuntimeError("The Range Finder could not be found on the I2C bus, check your connections")
            pass
        self.range_finder = VL53L0X(i2c=i2c)
    
    def forward(self):
        # Make the robot go forward for half a second

        self.motor_A_forward.high()
        self.motor_A_reverse.low()
        self.motor_B_forward.low()
        self.motor_B_reverse.high()
        sleep(0.5)
        self.motor_A_forward.low()
        self.motor_A_reverse.low()
        self.motor_B_forward.low()
        self.motor_B_reverse.low()

    def backward(self):
        # Make the robot go backward for half a second

        self.motor_A_forward.low()
        self.motor_A_reverse.high()
        self.motor_B_forward.high()
        self.motor_B_reverse.low()
        sleep(0.5)
        self.motor_A_forward.low()
        self.motor_A_reverse.low()
        self.motor_B_forward.low()
        self.motor_B_reverse.low()

    def turnleft(self):
        # Make the robot turn left for half a second

        self.motor_A_forward.low()
        self.motor_A_reverse.high()
        self.motor_B_forward.low()
        self.motor_B_reverse.high()
        sleep(0.5)
        self.motor_A_forward.low()
        self.motor_A_reverse.low()
        self.motor_B_forward.low()
        self.motor_B_reverse.low()

    def turnright(self):
        # Make the robot turn right for half a second

        self.motor_A_forward.high()
        self.motor_A_reverse.low()
        self.motor_B_forward.high()
        self.motor_B_reverse.low()
        sleep(0.5)
        self.motor_A_forward.low()
        self.motor_A_reverse.low()
        self.motor_B_forward.low()
        self.motor_B_reverse.low()

    def stop(self):
        self.motor_A_forward.low()
        self.motor_A_reverse.low()
        self.motor_B_forward.low()
        self.motor_B_reverse.low()

    @property
    def distance(self):
        # Returns the distance in cmm
        distance_to_object = (self.range_finder.ping() / 10) - 5
        return distance_to_object



    