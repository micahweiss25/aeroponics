import serial
import time
import logging
from datetime import datetime

f = open(r"./logs/sensor_data", "a")


ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
while True:
    data = ser.readline().decode("utf-8").replace("#", ",").replace("\n", "") + "," +  datetime.now().strftime("%H:%M:%S") + "\n"
    f.write(data)
    #logging.info(data)
    time.sleep(60)
    

