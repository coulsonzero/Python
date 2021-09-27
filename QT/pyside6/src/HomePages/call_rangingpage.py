from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, Qt
from HomePages.ui_rangingpage import Ui_RangingPage


class RangingPageWindow(QWidget, Ui_RangingPage):
    # 声明信号
    returnSignal = pyqtSignal()

    def __init__(self, parent=None):
        super(RangingPageWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setLayout(self.gridLayout)
        self.returnButton.clicked.connect(self.returnSignal)
