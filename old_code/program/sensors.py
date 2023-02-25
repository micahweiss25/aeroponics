import csv

fields = ['pH', 'volt', 'ec', 'temp', 'time']

def sensor_data(none):
    inst_time = datetime.datetime.now()
    filename = f"ph_log_{inst_time}.csv"
    with open("filename", "w") as log:
        csvlog = csv.writer(log)
        csvlog.writerow(fields)
   
    blank = none
    try:
        ser = serial.Serial('/dev/ttyACM0',9600)
    except:
        print("failed to find serial")
        
    # the first readline sometimes only receives part of the sensor data line, so I just get rid of it
    toss = ser.readline()
    while True:
        read_serial = str(ser.readline(), 'UTF-8') # readline should hang until a new line is sent
        read_serial = read_serial.split("#")
        voltage = float(read_serial[0])
        ph_balance = float(read_serial[1])
        ec = float(read_serial[2])
        temp = float(read_serial[3])
        time = datetime.datetime.now()
        data = [ph_balance, voltage, ec, temp, time]
        with open("filename", "a") as log:
            log.writerow(data)
            #log.write(f"pH: {ph_balance}; voltage: {voltage}; ec: {ec}; temp: {temp}; time: {datetime.datetime.now()}")
        # This should be made into it's own process so the sleeps don't stop data collection

