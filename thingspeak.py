import urequests

def send_data_to_thingspeak(api_key, temperature, air_humidity, soil_humidity):
    try:
        request = urequests.post(
            'http://api.thingspeak.com/update?api_key=' + api_key,
            json={"field1": temperature, "field2": air_humidity, "field3": soil_humidity},
            headers={"Content-Type": "application/json"}
        )
        print(f"Request #{request.text} sent")
        request.close()
    except Exception as e:
        print("Error sending data to ThingSpeak:", e)

def read_sensor_values(temperature_sensor, soil_moisture_sensor):
    temperature, air_humidity = temperature_sensor.read_temperature()
    soil_humidity = soil_moisture_sensor.read_moisture()
    return temperature, air_humidity, soil_humidity

def sensor_average(self):
    measured_array=[0] * 10
    for i in range 10:
        
    sum=0
    for i in range 10:
        sum+=measured_array[i]
    
    
    
