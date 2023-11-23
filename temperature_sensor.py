from machine import I2C
from machine import Pin

class TemperatureSensor:
    def __init__(self, scl_pin, sda_pin, address):
        self.i2c = I2C(0, scl=Pin(scl_pin), sda=Pin(sda_pin), freq=100000)
        self.address = address

    def read_temperature(self):
        val = self.i2c.readfrom_mem(self.address, 0, 4)
        temperature = f"{val[2]}.{val[3]}"
        humidity = f"{val[0]}.{val[1]}"
        return temperature, humidity
