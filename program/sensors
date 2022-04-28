def res_maintain(none):
    # next, right ph to a file 
    ph_log = open("ph_log", "w")
    blank = none
    try:
        ser = serial.Serial('/dev/ttyACM0',9600)
    except:
        print("failed to find serial")
    s = [0]
    while True:
        read_serial = str(ser.readline()) ## find the format so you can just get numbers
        # or modify ph sketch 
        # Should I pipe data from this function to a different one?
        ##### FOR NOW #####
        if "pH" in read_serial:
            read_serial = read_serial.split("#")
            ph_balance = float(re.sub('[^0-9.]', '', read_serial[1]))
            voltage = float(re.sub('[0-9.]', '', read_serial[0]))
            if ph_balance > 6.3:
                ph_log.write(f"pH is too high; pH: {ph_balance}; voltage: {voltage}; {datetime.datetime.now()}")
                GPIO.output(3, GPIO.LOW)
                sleep(5)
                GPIO.output(3, GPIO.HIGH)
                sleep(5)
            elif ph_balance < 5.3:
                ph_log.write(f"pH is too low; pH: {ph_balance}; voltage: {voltage}; {datetime.datetime.now()}")
                GPIO.output(4, GPIO.LOW)
                sleep(5)
                GPIO.output(4, GPIO.HIGH)
                sleep(5)
        else:
            pass
