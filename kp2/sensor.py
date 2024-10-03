class Sensor:  
    def __init__(self, sensor_id, location):   
        self.sensor_id = sensor_id 
        self.location = location

    def get_data(self):  

        return "Getting data from sensor."