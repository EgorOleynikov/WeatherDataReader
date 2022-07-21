import ctypes
import os

import serial
import time
from datetime import datetime
import csv
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice, QDate
import webbrowser
from pathlib import Path
from PyQt5.QtWidgets import QMainWindow

app = QtWidgets.QApplication([])
ui = uic.loadUi("app.ui")
ui.setWindowTitle("Weather Catcher")

serial = QSerialPort()
serial.setBaudRate(9600)
portList = []
ports = QSerialPortInfo.availablePorts()
for port in ports:
    portList.append(port.portName())
portList.reverse()
ui.comL.addItems(portList)

now = datetime.now()
nowDate = now.strftime("%d.%m.%Y")
state = 0

clickCounter = 0
startTime = 0
ifFirst = 1


def onOpen():
    serial.setPortName(ui.comL.currentText())
    serial.open(QIODevice.ReadWrite)
    global state
    state = 1
    Refresh()
    ui.dial.setValue(77)
    #secret()


def onClose():
    serial.close()
    time.sleep(1)
    global state
    state = 0
    Refresh()
    ui.dial.setValue(25)


def onRead():
    rx = serial.readLine()
    rxs = str(rx, 'utf-8').strip()
    data = rxs.split(',')
    temp = data[0]
    hum = data[1]
    heatI = data[2]
    ui.tempLab.setText(temp)
    ui.humLab.setText(hum)
    ui.heatILab.setText(heatI)
    if ui.radioBE.isChecked() and not ui.radioBD.isChecked():
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        filename = '%s.csv' % nowDate
        data = [dt_string] + data
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    if temp == 'nan' or hum == 'nan':
        ctypes.windll.user32.MessageBoxW(0, 'Temperature module error', u"Error", 0)
        onClose()
    else:
        pass


def logOpen():
    p1 = ui.calendar.selectedDate()
    p1 = p1.toString("dd.MM.yyyy")
    f = '%s.csv' % p1
    yogurt = Path(f).resolve()
    os.system(f'start excel.exe "{yogurt}"')


def dateChange():
    if ui.calendar.clicked:
        p1 = ui.calendar.selectedDate()
        ui.dateEdit.setDate(p1)
    if ui.dateEdit.dateChanged:
        p1 = ui.dateEdit.date()
        ui.calendar.setSelectedDate(p1)
    Refresh()


def Refresh():
    date = ui.calendar.selectedDate().toString("dd.MM.yyyy")
    bs = ui.radioBE.isChecked()
    if state == 1 and bs and date == nowDate:
        ui.buttLog.setEnabled(False)
    else:
        ui.buttLog.setEnabled(True)


def secret1():
    global startTime
    global ifFirst
    global clickCounter
    print(startTime)
    ifEnd = 0
    if ifFirst == 1:
        ifFirst = 0
        startTime = datetime.now
        while datetime.now - startTime <= 5:
            if ui.openB.clicked():
                clickCounter += 1
                if clickCounter == 7:
                    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        ifFirst == 1
    else:
        pass


def secret1():
    clickCounter = 0
    startTime = datetime.now()
    while 1:
        if ui.openB.clicked():
            clickCounter += 1
            if clickCounter == 7:
                webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        time_delta = datetime.now() - startTime
        print(time_delta)
        if time_delta.total_seconds() >= 10:
            break


serial.readyRead.connect(onRead)
ui.openB.clicked.connect(onOpen)
ui.closeB.clicked.connect(onClose)
ui.buttLog.clicked.connect(logOpen)

ui.dateEdit.setDisplayFormat("dd.MM.yyyy")
ui.dateEdit.setDate(now)

ui.setWindowIcon(QtGui.QIcon('icon.jpg'))

#
print(clickCounter)
#

ui.calendar.clicked.connect(dateChange)
ui.dateEdit.dateChanged.connect(dateChange)
ui.radioBE.toggled.connect(Refresh)

ui.show()
app.exec()
