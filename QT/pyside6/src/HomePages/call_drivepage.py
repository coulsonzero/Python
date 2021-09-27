from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, Qt
from HomePages.ui_drivepage import Ui_DrivePage


class DrivePageWindow(QWidget, Ui_DrivePage):
    # 声明信号
    returnSignal = pyqtSignal()

    def __init__(self, parent=None):
        super(DrivePageWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setLayout(self.gridLayout)
        self.returnButton.clicked.connect(self.returnSignal)
