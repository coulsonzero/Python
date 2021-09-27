# -*- coding: utf-8 -*-
"""
@Author: coulson
@Version: python3.9
@DateTime: 2021/9/2  18:22
"""
# HospitalRegSys0045.py
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_Window import Ui_MainWindow
import decimal

class mwindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mwindow, self).__init__()
        self.setupUi(self)

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    mshow=mwindow()
    mshow.show()
    sys.exit(app.exec_())