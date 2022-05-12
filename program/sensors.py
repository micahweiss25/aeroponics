def sensor_data(none):
    inst_time = datetime.datetime.now()
    blank = none
    try:
        ser = serial.Serial('/dev/ttyACM0',9600)
    except:
        print("failed to find serial")
    while True:
        read_serial = str(ser.readline(), 'UTF-8') # readline should hang until a new line is sent
        read_serial = read_serial.split("#")
        voltage = float(read_serial[0])
        ph_balance = float(read_serial[1])
        ec = float(read_serial[2])
        with open(f"ph_log_{inst_time}", "w") as log:
            log.write(f"pH: {ph_balance}; voltage: {voltage}; ec: {ec}; time: {datetime.datetime.now()}")
        # This should be made into it's own process so the sleeps don't stop data collection
        if ph_balance > 6.3:
            print("ph high")
            GPIO.output(3, GPIO.LOW)
            sleep(5)
            GPIO.output(3, GPIO.HIGH)
            sleep(5)
        elif ph_balance < 5.3:
            print("ph low")
            GPIO.output(4, GPIO.LOW)
            sleep(5)
            GPIO.output(4, GPIO.HIGH)
            sleep(5)
