def make_connection():
    ## ACTIVE LOW! ##
    ACID = 27
    BASE = 3
    SOLENIOD = 2
    GPIO.setwarnings(False) # turn off warnings
    GPIO.setmode(GPIO.BCM) # use GPIO numbers to specify inputs
    GPIO.setup(SOLENIOD, GPIO.OUT, initial=GPIO.HIGH) # GPIO2 = soleniod
    GPIO.setup(BASE, GPIO.OUT, initial=GPIO.HIGH) # GPIO3 = base
    #GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW) # GPIO17 = nuterients 4th relay
    #GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW) # GPIO5 = water 
    #GPIO.setup(7, GPIO.IN) # GPIO7 = read whether big pump is on or not
    #GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # GPIO4 = temp sensor 
    # This one confuses me. IDK why it has to be GPIO4 to read this sensor.
    GPIO.setup(ACID, GPIO.OUT, initial=GPIO.HIGH) # GPIO27 = acid
