def mist_cycle(none):
    blank = none
    count = 0
    with open(f"mist_log_{datetime.datetime.now()}", "w")
        try:
            while True:
                mist_log.write(f"mist cycle {count}; time: {datetime.datetime.now()}")
                GPIO.output(2, GPIO.LOW) # TURN MIST ON
                sleep(5)
                GPIO.output(2, GPIO.HIGH) # TURN MIST OFF
                sleep(5)
                count += 1
        except KeyboardInterrupt:
            GPIO.cleanup()
