from temperature_sensor import TemperatureSensor  

class Pyrometer(TemperatureSensor):  
    def __init__(self, sensor_id, location, measurement_range, distance):  
        super().__init__(sensor_id, location, measurement_range)  
        self.distance = distance 

    def get_data(self):
        return f"Pyrometer reading from sensor {self.sensor_id} at {self.location}, " \
               f"distance: {self.distance} meters."