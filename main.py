from soil_moisture_sensor import SoilMoistureSensor
from temperature_sensor import TemperatureSensor
from oled_display import OLEDDisplay
from relay import Relay
from wifi_connection import connect_wifi, disconnect_wifi
from thingspeak import send_data_to_thingspeak, read_sensor_values
from time import sleep

moisture_sensor = SoilMoistureSensor(36)
temperature_sensor = TemperatureSensor(22, 21, 0x5c)
oled = OLEDDisplay(128, 64, (22, 21), 0x3c)
relay = Relay(3)

WIFI_SSID = "UREL-SC661-V-2.4G"
WIFI_PSWD = "TomFryza"
THINGSPEAK_API_KEY = "MX7Z5X5MA96ZOIZW"  #We need to check this again

connect_wifi(WIFI_SSID, WIFI_PSWD)

try:
    while True:
        temperature1, humidity1, soil_humidity = read_sensor_values(temperature_sensor, moisture_sensor)
        temperature= float(temperature1)
        humidity= float(humidity1)
        
        display_data_Soil = f"Mois: {soil_humidity:.1f}% "
        display_data_Temp = f"Temp: {temperature}C"
        display_data_Hum =  f"Humi: {humidity}% "

        print(display_data_Soil, display_data_Temp, display_data_Hum)  # Print data to console
        
        oled.clear_screen()
        oled.show_message(display_data_Soil, display_data_Temp, display_data_Hum)  # Show data on OLED

            # We need to calculate threshold value
        if soil_humidity < 100:  #instead of soil_humidity we can create a mix of all three values from sensors threshold_value
            relay.control_relay(True, 1000)  # calculate the time for relay opening instead of 1s or keep 1s and it will keep opening for 1s till values are above threshold

        send_data_to_thingspeak(THINGSPEAK_API_KEY, temperature, humidity, soil_humidity)

        sleep(15)  # Delay between readings 1m maybe 1800 for 30m

except KeyboardInterrupt:
    disconnect_wifi()
    print("Execution stopped.")