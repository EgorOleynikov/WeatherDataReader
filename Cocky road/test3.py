import sys

import serial
import time
from datetime import datetime
import csv
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Close Window")
        self.b1 = QPushButton("Let's Close this Window")
        self.b1.clicked.connect(lambda: self.close())  # function binded to the button self.b1
        self.setCentralWidget(self.b1)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
