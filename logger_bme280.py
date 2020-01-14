import smbus2
import bme280
import json
import time
from datetime import date

port = 1
port2 = 4
address = 0x76
bus = smbus2.SMBus(port)
bus2 = smbus2.SMBus(port2)


calibration_params = bme280.load_calibration_params(bus, address)
calibration_params2 = bme280.load_calibration_params(bus2, address)

# the sample method will take a single reading and return a
# compensated_reading object
# there is a handy string representation too
while True:
        data = bme280.sample(bus, address, calibration_params)
        data2 = bme280.sample(bus2, address, calibration_params2)

        # the compensated_reading class has the following attributes
        #print(data.id)
        #print(data.timestamp)
        #print(data.temperature)
        #print(data.pressure)
        #print(data.humidity)
        #print(data)
        #print(data2)

        if data is not None:
                with open('data_bme280.json', 'w', encoding='utf-8') as f:
                        dataobj = {}
                        #Sensor in
                        dataIn = {}
                        dataIn['name'] = "sensorIn"
                        dataIn['temp'] = data2.temperature
                        dataIn['pres'] = data2.pressure
                        dataIn['hum'] = data2.humidity
                        #Sensor out
                        dataOut = {}
                        dataOut['name'] = "sensorOut"
                        dataOut['temp'] = data.temperature
                        dataOut['pres'] = data.pressure
                        dataOut['hum'] = data.humidity
                        
                        dataobj['ts'] = date.today().isoformat()
                        dataobj['sensors'] = [dataIn, dataOut]
                        json.dump(dataobj, f, ensure_ascii=False, indent=4)
                        #print(dataW)
        else:
                print("Failed to retrieve data from humidity sensor")

        time.sleep(15)

