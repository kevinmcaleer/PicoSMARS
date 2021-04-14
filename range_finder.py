from machine import Pin
from time import sleep_us, ticks_us

class Range_Finder():

    duration = 0
    distance = 0

    def __init__(self, echo_pin, trigger_pin):
        # Initialise the Range Finder
        self.__echo.pin = Pin(echo_pin, Pin.IN)
        self.__trigger_pin = Pin(trigger_pin, Pin.OUT)

    def ping(self):
        self.__trigger_pin.low()
        sleep_us(2)

        self.__trigger_pin.high()
        sleep_us(5)
        self.__trigger_pin.low()
        signalon = 0
        signaloff = 0
        while self.__echo_pin.value() == 0:
            signaloff = ticks_us()
        while self.__echo_pin.value() == 1:
            signalon = ticks_us()
        elapsed_micros = signalon - signaloff
        self.duration = elapsed_micros
        self.distance = (elapsed_micros * 0.343) / 2
        return self.distance

