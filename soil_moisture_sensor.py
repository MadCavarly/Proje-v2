from machine import ADC
from machine import Pin

class SoilMoistureSensor:
    def __init__(self, pin_number):
        self.sensor_pin = ADC(Pin(pin_number))

    def read_moisture(self):
        moisture_value = self.sensor_pin.read()  # Reading the sensor pin value
        #moisture_percentage = (moisture_value / 1023.0) * 100.0  # Calculating moisture percentage
        moisture_percentage = moisture_value
        return moisture_percentage
