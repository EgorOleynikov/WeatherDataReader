import serial
from datetime import datetime
import csv

ser = serial.Serial('COM6')
ser.flushInput()

while 1:
    ser_bytes = ser.readline()
    print(ser_bytes)
    decoded_list_of_bytes = str(ser_bytes.decode("utf-8")).rstrip("\r\n")
    print(decoded_list_of_bytes)
    data_list = decoded_list_of_bytes.split(',')
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    date = now.strftime("%d.%m.%Y")
    filename = '%s.csv' % date
    print(filename)
    data_list = [dt_string] + data_list
    print(data_list)
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data_list)
