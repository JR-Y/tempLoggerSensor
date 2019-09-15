import Adafruit_DHT
import json
import time
from datetime import date

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        if humidity is not None and temperature is not None:
                with open('data.json', 'w', encoding='utf-8') as f:
                        data = {}
                        #data['date'] = time.strftime('%Y-%m-%d')
                        data['date'] = date.today().isoformat()
                        data['time'] = time.strftime('%H:%M')
                        data['temp'] = '{0:0.1f}'.format(temperature)
                        data['hum'] = '{0:0.1f}'.format(humidity)
                        json.dump(data, f, ensure_ascii=False, indent=4)
                        print(data)
        else:
                print("Failed to retrieve data from humidity sensor")

        time.sleep(5)



