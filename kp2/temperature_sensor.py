from sensor import Sensor  

class TemperatureSensor(Sensor):  
    def __init__(self, sensor_id, location, measurement_range):  

        super().__init__(sensor_id, location)  
        self.measurement_range = measurement_range  

    def get_data(self):  
        return f"Temperature data from sensor {self.sensor_id} at {self.location}."