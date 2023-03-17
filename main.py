# DHT22 Sensor pins
# * DHT22 Pin 1 to 3V3
# * DHT22 Pin 2 to GP2
# * DHT22 Pin 3 to NC
# * DHT22 Pin 4 to GND

from machine import Pin, UART
from DHT22 import DHT22
import time
import json
import math

# Initialize DHT22
dht22 = DHT22(Pin(2,Pin.IN,Pin.PULL_UP))

#Initialize the onboard LED as output
led = machine.Pin(25,machine.Pin.OUT)

# init with given baudrate
# uart = UART(1, 9600)
# init with given parameters
# uart.init(9600, bits=8, parity=None, stop=1)

while True:
    led.value(1)
    T, H = dht22.read()
    temp = (T * 9/5) + 32;
    reading = {'temperature': temp, 'humidity': H, 'timestamp': int(math.floor(time.time()))}
    jsonReading = json.dumps(reading)
    # write output to console
    print(jsonReading + '\n')
    # uart.write(jsonReading + '\n')

    time.sleep_ms(500)
    led.value(0)

    # Wait for Five seconds. Then proceed to collect next sensor reading.
    time.sleep_ms(5000)

