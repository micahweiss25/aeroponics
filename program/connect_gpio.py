def make_connection():
    ## ACTIVE LOW! ##
    GPIO.setwarnings(False) # turn off warnings
    GPIO.setmode(GPIO.BCM) # use GPIO numbers to specify inputs
    GPIO.setup(2, GPIO.OUT, initial=GPIO.HIGH) # GPIO2 = soleniod
    GPIO.setup(3, GPIO.OUT, initial=GPIO.HIGH) # GPIO3 = acid
    GPIO.setup(4, GPIO.OUT, initial=GPIO.HIGH) # GPIO4 = base
    GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW) # GPIO5 = water
    GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW) # GPIO6 = nuterients
    GPIO.setup(7, GPIO.IN) # GPIO7 = read whether big pump is on or not
