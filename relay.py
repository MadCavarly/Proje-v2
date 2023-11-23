from machine import Pin
from time import sleep_ms

class Relay:
    def __init__(self, pin_number):
        self.relay_pin = Pin(pin_number, Pin.OUT)

    def activate_relay(self):
        self.relay_pin.on()

    def deactivate_relay(self):
        self.relay_pin.off()

    def control_relay(self, condition, duration):
        if condition:
            self.activate_relay()
            sleep_ms(duration)
            self.deactivate_relay()
