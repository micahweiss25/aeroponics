import serial

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
while True:
    print(ser.readline())
