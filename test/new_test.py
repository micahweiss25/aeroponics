from time import sleep
import RPi.GPIO as GPIO
try:
  from test_gpio_connect import *
except:
  print("failed to import gpio_connect")
make_connection()
def acid_on():
  # include the portion where you set up the GPIO because I'm hearing weird noises and I can't pin down what part is causing it
  print("acid on")
  GPIO.output(ACID, GPIO.LOW)
  print("acid off")
  GPIO.output(ACID, GPIO.HIGH)
