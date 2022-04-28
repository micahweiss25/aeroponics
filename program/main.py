from time import sleep
import serial
import datetime
import re
from sensors import *
from misters import *
from connect_gpio import *
try:
    import multiprocessing as mp
except RuntimeError:
    print("multiprocessing failed to import")
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

connect_gpio.make_connection()
   
if __name__ == '__main__':
    mist_cycle_process = mp.Process(target=misters.mist_cycle, args=(None,))
    res_maintain_process = mp.Process(target=sensors.res_maintain, args=(None,))

    mist_cycle_process.start()
    res_maintain_process.start()
    mist_cycle_process.join()
    res_maintain_process.join()
