import serial
import time
import csv

ser = serial.Serial('COM6')
ser.flushInput()

while 1:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
        with open('cock_log.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([time.ctime(),decoded_bytes])
    except:
        print("Data Interrupt")
        break