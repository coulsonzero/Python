"""
@author: coulson
@version: 2021/8/6  13:41
"""

from PySide6.QtGui import Qt
from PySide6.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
    def initUI(self):
        self.resize(500, 400)
        self.move(700, 210)
        self.setWindowTitle("测试窗口")

        self.frame = QFrame(self)
        self.vBox = QVBoxLayout(self.frame)
        self.btn_MaxShow = QPushButton(self.frame)
        self.btn_MaxShow.setObjectName("btn_MaxShow")
        self.btn_MaxShow.setText("最大化")
        self.btn_MaxShow.clicked.connect(self.btnClick)

        self.btn_min = QPushButton(self.frame)
        self.btn_min.setObjectName("btn_min")
        self.btn_min.setText("最小化")
        # self.btn_min.setIcon(QIcon("button.png"))
        self.btn_min.clicked.connect(self.showNormal)
        self.vBox.addWidget(self.btn_MaxShow)
        self.vBox.addWidget(self.btn_min)





    def btnClick(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_MaxShow":
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()


if __name__ == '__main__':
    app = QApplication([])
    w = Window()
    app.exec()


