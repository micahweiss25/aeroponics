from time import sleep
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT, initial=GPIO.HIGH) # GPIO2 = soleniod
while True:
  GPIO.output(2, GPIO.LOW) # TURN MIST ON
  sleep(3)
  GPIO.output(2, GPIO.HIGH) # TURN MIST OFF
  sleep(3)
