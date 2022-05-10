def make_connection():
    ## ACTIVE LOW! ##
    GPIO.setwarnings(False) # turn off warnings
    GPIO.setmode(GPIO.BCM) # use GPIO numbers to specify inputs
    GPIO.setup(2, GPIO.OUT, initial=GPIO.HIGH) # GPIO2 = soleniod
    GPIO.setup(3, GPIO.OUT, initial=GPIO.HIGH) # GPIO3 = base
    #GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW) # GPIO17 = nuterients 4th relay
    #GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW) # GPIO5 = water 
    #GPIO.setup(7, GPIO.IN) # GPIO7 = read whether big pump is on or not
    GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # GPIO27 = acid 
    # This one confuses me. IDK why it has to be GPIO4 to read this sensor.
    GPIO.setup(4, GPIO.OUT, initial=GPIO.HIGH) # GPIO4 = temp sensor
