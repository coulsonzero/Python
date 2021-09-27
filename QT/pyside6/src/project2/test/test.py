"""
@author: coulson
@version: 2021/7/27  14:22
"""


import sys

from PySide6.QtCore import *

from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtUiTools import QUiLoader


class Window(QWidget):

    def __init__(self, parent=None):
        # super这个用法是调用父类的构造函数
        # parent=None表示默认没有父Widget，如果指定父亲Widget，则调用之
        super(Window, self).__init__(parent)
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('显示')

        self.btn = QPushButton(self)
        self.btn.setText('标定')
        self.btn.move(150, 50)


# 下面的一部分是Qtdesigner的代码

class Ui_Form(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(624, 479)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(190, 130, 51, 31))
        self.label.setObjectName("label")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(330, 260, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QRect(280, 130, 151, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 =QLabel(self.centralwidget)
        self.label_2.setGeometry(QRect(190, 180, 51, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QRect(280, 190, 151, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QRect(200, 260, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 624, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "   长"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.label_2.setText(_translate("MainWindow", "   宽"))
        self.pushButton_2.setText(_translate("MainWindow", "取消"))


if __name__ == "__main__":
    app = QApplication([])
    win = QMainWindow()

    ui = Ui_Form()
    ui.setupUi(win)

    ex = Window()
    ex.show()
    ex.btn.clicked.connect(win.show)
    app.exec_()


