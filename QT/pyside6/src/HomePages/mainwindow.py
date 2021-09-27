from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from call_mainpage import MainPageWindow
from call_camerapage import CameraPageWindow
from call_drivepage import DrivePageWindow
from call_rangingpage import RangingPageWindow


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(480, 320)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.Stack = QStackedWidget()
        self.layout.addWidget(self.Stack)
        self.mainPageUi = MainPageWindow()
        self.cameraPageUi = CameraPageWindow()
        self.drivePageUi = DrivePageWindow()
        self.rangingPageUi = RangingPageWindow()

        self.Stack.addWidget(self.mainPageUi)
        self.Stack.addWidget(self.cameraPageUi)
        self.Stack.addWidget(self.drivePageUi)
        self.Stack.addWidget(self.rangingPageUi)

        self.mainPageUi.chooseSignal.connect(self.showDialog)

        self.cameraPageUi.returnSignal.connect(self.returnDialog)
        self.drivePageUi.returnSignal.connect(self.returnDialog)
        self.rangingPageUi.returnSignal.connect(self.returnDialog)

    def showDialog(self, msg):
        print(0)
        if msg == 'camera':
            self.Stack.setCurrentIndex(1)
            print(1)
        elif msg == 'ranging':
            self.Stack.setCurrentIndex(2)
            print(2)
        elif msg == 'drive':
            self.Stack.setCurrentIndex(3)
            print(3)

    def returnDialog(self):
        self.Stack.setCurrentIndex(0)
