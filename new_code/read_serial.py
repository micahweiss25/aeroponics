import serial
import time
import logging
from datetime import datetime


last_time = time.time()
data = ""

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
while True:
    if time.time() - last_time > 15:
        last_time = time.time()
        f = open(r"./logs/sensor_data", "a")
        f.write(data)
        f.close()
        data = ""
    data += ser.readline().decode("utf-8").replace("#", ",").replace("\n", "") + "," +  datetime.now().strftime("%H:%M:%S") + "\n"
    time.sleep(1)
    

