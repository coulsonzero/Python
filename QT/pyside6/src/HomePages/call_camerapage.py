"""
@author: coulson
@version: 2021/8/10  14:11
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, Qt
from HomePages.ui_camerapage import Ui_CameraPage


class CameraPageWindow(QWidget, Ui_CameraPage):
    # 声明信号
    returnSignal = pyqtSignal()

    def __init__(self, parent=None):
        super(CameraPageWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setLayout(self.gridLayout)
        self.returnButton.clicked.connect(self.returnSignal)
