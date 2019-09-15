# tempLoggerSensor

## What for
This package is an installation guide for a network temperature & humidity sensor unit. 
The unit can be implemented with a raspberry pi, pi zero works good because of the small size.
When installation is complete you'll have a temperature & humidity sensor on your network, that you can call by the ip & port and will respond with for example: { "date": "2019-09-15", "time": "13:53", "temp": "29.2", "hum": "18.5" }.
If required you can make many of these with different IP's & integrate them to your own smart home, etc. server.

## Installation

### Requirements
- A router that allows you to assign static local IP's to devices
- A raspberry pi connected to that network
- A DHT22 sensor, search ebay etc.

### Connecting sensor
- VCC to pin 1, 3V3 or pin 17
- DATA to GPIO4, (with small changes to code multible sensors could be connected to different gpio pins)
- GROUND to pin 6, or any groung pin
- 4.7Kohm resistor between VCC & DATA pins

### Raspberry installation
- Install NOOBS rasbian on your raspberry, see https://www.raspberrypi.org/
- It's recommended then to enable vnc & do the rest of the installation "headless", then you'll be able to also later connect to your raspberry remote if necessary.

### After rasbian installation
- sudo apt-get update
- sudo apt-get upgrade
- install latest LTS nodejs https://nodejs.org/en/download/ on pi zero use ARMv6 version, google instructions
run
- sudo npm install pm2 -g
- git should be installed on rasbian if not install git

### Then run following on command line:
- cd ~
- git clone https://github.com/JR-Y/tempLogger.git
- cd tempLoggerSensor
- sudo apt-get install build-essential python-dev python-openssl
--------------------------------------------------------------------
Run this
    - git clone https://github.com/adafruit/Adafruit_Python_DHT.git
    - cd Adafruit_Python_DHT
    - sudo python3 setup.py install
or run this `#Not tested`
- sudo pip3 install Adafruit_Python_DHT `#Not tested`
--------------------------------------------------------------------
- cd ~/tempLoggerSensor
- npm install
- pm2 start logger.py --interpreter python3
- pm2 start index.js
- pm2 save
- pm2 startup
-> copy resulted script on commandline & run script

### Test
On a browser with a computer on the same network go to: http://{the ip you assigned to your pi}:{the port assigned in index.js}, for example http://192.168.1.104:9467
On the raspberry you just configured open browser & go to: http://localhost:{the port assigned in index.js}, for example http://localhost:9467
If response looks like { "date": "2019-09-15", "time": "13:53", "temp": "29.2", "hum": "18.5" }, concrats you have a working network temperature & humidity sensor