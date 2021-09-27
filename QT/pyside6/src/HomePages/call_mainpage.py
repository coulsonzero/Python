from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from HomePages.ui_mainpage import Ui_MainPage
from PyQt5.QtCore import pyqtSignal, Qt


class MainPageWindow(QWidget, Ui_MainPage):
    # 定义点击信号
    chooseSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MainPageWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setLayout(self.gridLayout)
        self.cameraButton.clicked.connect(self.showDialog)
        self.rangingButton.clicked.connect(self.showDialog)
        self.driveButton.clicked.connect(self.showDialog)

    def showDialog(self):
        sender = self.sender()
        if sender == self.cameraButton:
            # 发射点击信号
            self.chooseSignal.emit('camera')
        elif sender == self.rangingButton:
            self.chooseSignal.emit('ranging')
        elif sender == self.driveButton:
            self.chooseSignal.emit('drive')
