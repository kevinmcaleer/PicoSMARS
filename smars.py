# SMARS class

from vl53l0x import VL53L0X
from machine import Pin

class SMARS():
    name = ""

    def __init__(self, i2c, name = None, in1=None, in2=None, in3=None, in4=None):
        if in1 or in2 or in3 or in4 == None:
            in1 = Pin(2) # Motor Input 1
            in2 = Pin(3) # Motor Input 2
            in3 = Pin(4) # Motor Input 3
            in4 = Pin(5) # Motor Input 4
        else:
            # check the type is Pin
            if type(in1) == Pin and type(in2) == Pin and type(in3) == Pin and type(in4) == Pin:
                # Set the motor inputs on the L293D Motor Driver board
                self.in1 = in1
                self.in2 = in2
                self.in3 = in3
                self.in4 = in4
            else:
                raise RuntimeError("The motor pin values passed were not Type Pin. Please check your code")
        if not name:
            self.name = "PicoSMARS"
        else:
            self.name = name
        self.i2c = i2c  
        if self.i2c.scan() == []:
            # print('The range finder could not be found')
            raise RuntimeError("The Range Finder could not be found on the I2C bus, check your connections")
        self.range_finder = VL53L0X(i2c=i2c)

       

    
    def forward(self):
        # print('forward')

        in

    def backward(self):
        # print('backward')
        pass

    def turnleft(self):
        # print('turnleft')
        pass

    def turnright(self):
        # print('turnright')
        pass

    @property
    def distance(self):
        # Returns the distance in cmm
        distance_to_object = (self.range_finder.ping() / 10) - 5
        return distance_to_object



    