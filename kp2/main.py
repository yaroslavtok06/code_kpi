from pyrometer import Pyrometer  

def main():   
    pyrometer = Pyrometer(sensor_id="P001", location="Roof", measurement_range="50-1000°C", distance=5)  
    print(pyrometer.get_data())  

main()