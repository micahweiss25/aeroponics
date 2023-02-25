from time import sleep
import serial
import datetime
import re
try:
    import multiprocessing as mp
except RuntimeError:
    print("multiprocessing failed to import")
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

    
## ACTIVE LOW! ##
GPIO.setwarnings(False) # turn off warnings
GPIO.setmode(GPIO.BCM) # use GPIO numbers to specify inputs
GPIO.setup(2, GPIO.OUT, initial=GPIO.HIGH) # GPIO2 = soleniod
GPIO.setup(3, GPIO.OUT, initial=GPIO.HIGH) # GPIO3 = acid
GPIO.setup(4, GPIO.OUT, initial=GPIO.HIGH) # GPIO4 = base
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW) # GPIO5 = water
GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW) # GPIO6 = nuterients
GPIO.setup(7, GPIO.IN) # GPIO7 = read whether big pump is on or not
def mist_cycle(none):
    mist_log = open("mist_log", "w")
    blank = none
    count = 0
    try:
        while True:
            mist_log.write(f"mist cycle {count}")
            GPIO.output(2, GPIO.LOW) # TURN MIST ON
            sleep(5)
            GPIO.output(2, GPIO.HIGH) # TURN MIST OFF
            sleep(5)
            count += 1
    except KeyboardInterrupt:
        GPIO.cleanup()
    
def res_maintain(none):
    # next, right ph to a file 
    ph_log = open("ph_log", "w")
    blank = none
    try:
        ser = serial.Serial('/dev/ttyACM0',9600)
    except:
        print("failed to find serial")
    s = [0]
    while True:
        read_serial = str(ser.readline()) ## find the format so you can just get numbers
        # or modify ph sketch 
        # Should I pipe data from this function to a different one?
        ##### FOR NOW #####

        try:
            if "pH" in read_serial:
                read_serial = read_serial.split("pH")[1]
                ph_balance = float(re.sub('[^0-9.]', '', read_serial))
                if ph_balance < 5.3:
                    ph_log.write(f"pH is too high; {read_serial}; {datetime.datetime.now()}")
                    print(f"pH is too high; {read_serial}; {datetime.datetime.now()}")
                    GPIO.output(3, GPIO.LOW)
                    sleep(5)
                    GPIO.output(3, GPIO.HIGH)
                    sleep(5)
                elif ph_balance > 6.3:
                    ph_log.write(f"pH is too low; {read_serial}; {datetime.datetime.now()}")
                    print(f"pH is too low; {read_serial}; {datetime.datetime.now()}")
                    GPIO.output(4, GPIO.LOW)
                    sleep(5)
                    GPIO.output(4, GPIO.HIGH)
                    sleep(5)
            else:
                pass
        except:
            print("pass")



if __name__ == '__main__':
    mist_cycle_process = mp.Process(target=mist_cycle, args=(None,))
    res_maintain_process = mp.Process(target=res_maintain, args=(None,))

    mist_cycle_process.start()
    res_maintain_process.start()
    mist_cycle_process.join()
    res_maintain_process.join()

