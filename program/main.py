try:
    import multiprocessing as mp
except RuntimeError:
    print("multiprocessing failed to import")
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
from time import sleep
import serial
import datetime
from sensors import ph_balance, sensor_data
from misters import mist_cycle
from ph import ph_cycle
from connect_gpio import *


connect_gpio.make_connection()
   
if __name__ == '__main__':
    mist_cycle_process = mp.Process(target=misters.mist_cycle, args=(None,))
    sensor_process = mp.Process(target=sensors.sensor_data, args=(None,))
    ph_cycle_process = mp.Process(target=ph.ph_cycle, args=(None,))

    mist_cycle_process.start()
    sensor_process.start()
    ph_cycle_process.start()
    mist_cycle_process.join()
    sensor_process.join()
    ph_cycle_process.join()
