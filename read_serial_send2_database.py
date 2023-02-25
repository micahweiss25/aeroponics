import serial
from time import sleep
import mysql.connector as mysql

HOST = '192.168.100.25'

DATABASE = 'aero'

USER = 'wei_pi'

PASSWORD = 'password'

db_connection = mysql.connector.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)

db_cursor = db_connection.cursor()

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
while True:
    # read data from serial port
    data = ser.readline().split
    print(f"{voltage: data[0]}, ph: {data[1]}, tds: {data[2]}, temp: {data[3]}")

    # I STILL NEED TO INTERPRET THE DATA BEFORE ENTERING INTO DATABASE

    # write data to database
    db_cursor.execute("INSERT INTO aero_data (volt, ph, tds, temp) VALUES (%s, %s, %s, %s)", (data[0],data[1],data[2],data[3]))
    db_connection.commit()
    print(db_connection.rowcount, "record inserted.")
    
    # I NEED TO FIGURE OUT IF FLUSH IS NEEDED

    #ser.fush()
    sleep(60)



