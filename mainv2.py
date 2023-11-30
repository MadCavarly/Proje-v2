from soil_moisture_sensor import SoilMoistureSensor
from temperature_sensor import TemperatureSensor
from oled_display import OLEDDisplay
from relay import Relay
from wifi_connection import connect_wifi, disconnect_wifi
from thingspeak import send_data_to_thingspeak, read_sensor_values
from parameters import Parameters as params
from time import sleep

moisture_sensor = SoilMoistureSensor(36)
temperature_sensor = TemperatureSensor(22, 21, 0x5c)
oled = OLEDDisplay(128, 64, (22, 21), 0x3c)
relay = Relay(3)


WIFI_SSID = "UREL-SC661-V-2.4G"
WIFI_PSWD = "TomFryza"
THINGSPEAK_API_KEY = "MX7Z5X5MA96ZOIZW"  #We need to check this again


try:
    while True:
        connect_wifi(WIFI_SSID, WIFI_PSWD) #connecting to wifi
        temperature1, humidity1, soil_moisture = read_sensor_values(temperature_sensor, moisture_sensor) #reading values from sensors
        temperature= float(temperature1) #converting values to float
        humidity= float(humidity1)       #converting values to float
        params.calculate_parameters(soil_moisture, humidity, temperature) #calculating the soil_moisture limit with given sensor values
        
        
        display_data_Soil = f"Mois: {soil_moisture:.1f}% " #create string from sensor values to print
        display_data_Temp = f"Temp: {temperature}C"        #create string from sensor values to print
        display_data_Hum =  f"Humi: {humidity}% "          #create string from sensor values to print

        print(display_data_Soil, display_data_Temp, display_data_Hum)  # Print data to console
        
        oled.clear_screen() #clearing screen for new message
        oled.show_message(display_data_Soil, display_data_Temp, display_data_Hum)  # Show data on OLED

            # We need to calculate threshold value
        if soil_moisture < params.soil_moisture_limit:  #checking if measured moisture is under the limit
            relay.control_relay(True, 1000) # starts watering for 1m if soil moisture is under the limit
            params.check_time = 60          # sets sleep time to 1m to check if watering was enought
        else:
            params.check_time = 1800        #if watering was enought sets check time back to 30m
            
        
        send_data_to_thingspeak(THINGSPEAK_API_KEY, temperature, humidity, soil_moisture) #send data to thingspeak
        disconnect_wifi() #disconnect from wifi
        
        sleep(params.check_time)  # sleep according to check time till next measurement
        

except KeyboardInterrupt:
    
    print("Execution stopped.")