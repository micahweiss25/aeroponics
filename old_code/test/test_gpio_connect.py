import RPi.GPIO as GPIO
ACID = 3
BASE = 17
NUTRIENT = 27
WATER = 22
SOLENIOD = 23

# make connection
def mc():
    ## ACTIVE LOW! ##
    GPIO.setwarnings(False) # turn off warnings
    GPIO.setmode(GPIO.BCM) # use GPIO numbers to specify inputs
    GPIO.setup(ACID, GPIO.OUT, initial=GPIO.HIGH) # GPIO2 = ACID
    GPIO.setup(BASE, GPIO.OUT, initial=GPIO.HIGH) # GPIO3 = BASE
    GPIO.setup(NUTRIENT, GPIO.OUT, initial=GPIO.HIGH) # GPIO4 = NUTRIENT
    GPIO.setup(WATER, GPIO.OUT, initial=GPIO.HIGH) # GPIO17 = WATER
    GPIO.setup(SOLENIOD, GPIO.OUT, initial=GPIO.HIGH) # GPIO27 = SOLENIOD
    #GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW) # GPIO5 = water 
    #GPIO.setup(7, GPIO.IN) # GPIO7 = read whether big pump is on or not
    #GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # GPIO4 = temp sensor 
    # This one confuses me. IDK why it has to be GPIO4 to read this sensor.

