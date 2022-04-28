from time import sleep
import serial
import datetime
import re
import sensors
import misters
import connect_gpio
try:
    import multiprocessing as mp
except RuntimeError:
    print("multiprocessing failed to import")
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

   
if __name__ == '__main__':
    mist_cycle_process = mp.Process(target=mist_cycle, args=(None,))
    res_maintain_process = mp.Process(target=res_maintain, args=(None,))

    mist_cycle_process.start()
    res_maintain_process.start()
    mist_cycle_process.join()
    res_maintain_process.join()
