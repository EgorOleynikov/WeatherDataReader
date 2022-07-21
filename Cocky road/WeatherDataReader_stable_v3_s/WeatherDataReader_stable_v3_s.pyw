import ctypes
import os
import urllib
import urllib.request
import zipfile
from pygame import mixer

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


def ZIPunzip():
    file_name = 'data.zip'
    pswd = '142358679=0-'
    with zipfile.ZipFile(file_name, 'r') as file:
        file.extractall(pwd=bytes(pswd, 'utf-8'))


# ZIPunzip()

app = QtWidgets.QApplication([])
ui = uic.loadUi("app.ui")
uiShrek = uic.loadUi("appS.ui")
corn = uic.loadUi("corn.ui")
ui.setWindowTitle("Weather Catcher")
corn.setWindowTitle("NIGGERS")

serial = QSerialPort()
serial.setBaudRate(9600)
portList = []
ports = QSerialPortInfo.availablePorts()
for port in ports:
    portList.append(port.portName())
portList.reverse()
# print(portList)
ui.comL.addItems(portList)
dirtyList = ['Suck some dicks']
now = datetime.now()
nowDate = now.strftime("%d.%m.%Y")
state = 0


def onOpen():
    serial.setPortName(ui.comL.currentText())
    serial.open(QIODevice.ReadWrite)
    global state
    state = 1
    Refresh()
    ui.dial.setValue(77)


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
    # print(data)
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


def logOpen():
    p1 = ui.calendar.selectedDate()
    p1 = p1.toString("dd.MM.yyyy")
    f = '%s.csv' % p1
    yogurt = Path(f).resolve()
    os.system(f'start excel.exe "{yogurt}"')


def fYou():
    for x in (dirtyList * 5):
        ctypes.windll.user32.MessageBoxW(0, x, u"Nigger", 0)
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


def passGranted():
    uiShrek.close()
    ui.show()


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


def niggers():
    corn.show()
    mixer.init()
    mixer.music.load('corm.mp3')
    mixer.music.play()


ui.setWindowIcon(QtGui.QIcon('5c0fc.jpg'))

uiShrek.buttY.clicked.connect(fYou)
uiShrek.buttN.clicked.connect(passGranted)

serial.readyRead.connect(onRead)
ui.openB.clicked.connect(onOpen)
ui.closeB.clicked.connect(onClose)
ui.buttLog.clicked.connect(logOpen)
ui.niggers.clicked.connect(niggers)

ui.movie = QMovie('tenor.gif')
ui.label_5.setMovie(ui.movie)
ui.movie.start()

ui.dateEdit.setDisplayFormat("dd.MM.yyyy")
ui.dateEdit.setDate(now)

ui.calendar.clicked.connect(dateChange)
ui.dateEdit.dateChanged.connect(dateChange)
ui.radioBE.toggled.connect(Refresh)

uiShrek.show()
app.exec()
