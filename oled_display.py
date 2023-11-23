from machine import I2C
from sh1106 import SH1106_I2C
from machine import Pin

class OLEDDisplay:
    def __init__(self, width, height, pins, address):
        self.i2c = I2C(0, scl=Pin(pins[0]), sda=Pin(pins[1]), freq=100000)
        self.oled = SH1106_I2C(width, height, self.i2c, addr=address, rotate=180)
        self.oled.sleep(False)
        self.oled.contrast(50)

    def show_message(self, display_data_Soil, display_data_Temp, display_data_Hum):
        self.oled.text(display_data_Soil, x=0, y=0)
        self.oled.text(display_data_Temp, x=0, y=10)
        self.oled.text(display_data_Hum, x=0, y=20)
        self.oled.show()
    
    def clear_screen(self):
        self.oled.fill(0)
        self.oled.show()
