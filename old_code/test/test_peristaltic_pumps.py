import time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
from test_gpio_connect import *
make_connection()
while True:
    print("acid ON")
    GPIO.output(ACID, GPIO.LOW)
    sleep(2)
    GPIO.output(ACID, GPIO.HIGH)
    print("base ON")
    GPIO.output(BASE, GPIO.LOW)
    sleep(2)
    GPIO.output(BASE, GPIO.HIGH)

    print("nutrient ON")
    GPIO.output(NUTRIENT, GPIO.LOW)
    sleep(2)
    GPIO.output(NUTRIENT, GPIO.HIGH)
    print("water ON")
    GPIO.output(WATER, GPIO.LOW)
    sleep(2)
    GPIO.output(WATER, GPIO.HIGH)
