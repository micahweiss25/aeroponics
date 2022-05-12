import time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

GPIO.setup(3, GPIO.OUT, initial=GPIO.HIGH) # GPIO3 = base
GPIO.setup(27, GPIO.OUT, initial=GPIO.HIGH) # GPIO27 = acid
while True:
    print("base ON")
    GPIO.output(3, GPIO.LOW)
    sleep(2)
    GPIO.output(3, GPIO.HIGH)
    print("acid ON")
    GPIO.output(27, GPIO.LOW)
    sleep(2)
    GPIO.output(27, GPIO.HIGH)
