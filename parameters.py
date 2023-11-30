class Parameters:
    def __init__(self, check_time=1800):
        self.check_time = check_time
        
    def calculate_parameters(self, soil_moisture, air_humidity, temperature):
        if(temperature>30 and air_humidity<30):
            self.soil_moisture_limit = 35
        elif(temperature<18):
            self.soil_moisture_limit = 15
        else:
            self.soil_moisture_limit = 25