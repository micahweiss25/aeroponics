from time import sleep
import RPi.GPIO as GPIO

print("set to BCM")
GPIO.setmode(GPIO.BCM)

def connect(var):
  print(f"connect to {var}")
  GPIO.setup(var, GPIO.OUT, initial=GPIO.HIGH)
  
# give test() the GPIO pin number and a boolean value (bool true = on, bool false = off) 
# to turn on and off a pin
def test(var,pos):
  if pos:
    print(f"{var} on")
    GPIO.output(var, GPIO.LOW)
  if not pos:
    print(f"{var} off")
    GPIO.output(var, GPIO.HIGH)

def print_connections():
  print(f"ACID = {ACID}\nBASE = {BASE}\nNUTRIENT = {NUTRIENT}\nWATER = {WATER}\nSOLENIOD = {SOLENIOD}")
