import RPi.GPIO as GPIO

def set_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(3, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(17, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(18, GPIO.OUT, initial=GPIO.HIGH)
