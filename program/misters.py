# need to import sleep and GPIO
def mist_cycle(none):
    mist_log = open("mist_log", "w")
    blank = none
    count = 0
    try:
        while True:
            mist_log.write(f"mist cycle {count}")
            GPIO.output(2, GPIO.LOW) # TURN MIST ON
            sleep(5)
            GPIO.output(2, GPIO.HIGH) # TURN MIST OFF
            sleep(5)
            count += 1
    except KeyboardInterrupt:
        GPIO.cleanup()
