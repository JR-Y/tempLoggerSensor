import smbus2
import bme280
import json
import time

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
                        dataIn['id'] = str(data2.id)
                        dataIn['timestamp'] = str(data2.timestamp)#data.timestamp.strftime('%H:%M')
                        dataIn['temperature'] = data2.temperature
                        dataIn['pressure'] = data2.pressure
                        dataIn['humidity'] = data2.humidity
                        #Sensor out
                        dataOut = {}
                        dataOut['id'] = str(data.id)
                        dataOut['timestamp'] = str(data.timestamp)#data.timestamp.strftime('%H:%M')
                        dataOut['temperature'] = data.temperature
                        dataOut['pressure'] = data.pressure
                        dataOut['humidity'] = data.humidity
                        
                        dataobj['sensorIn'] = dataIn
                        dataobj['sensorOut'] = dataOut
                        json.dump(dataobj, f, ensure_ascii=False, indent=4)
                        #print(dataW)
        else:
                print("Failed to retrieve data from humidity sensor")

        time.sleep(15)

