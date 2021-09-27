"""
@author: coulson
@version: 2021/7/28  10:54
"""
"""
切换窗口
"""

import sys
from PyQt5.QtWidgets import *
from PySide6.QtCore import Qt


class First(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Event sender')
        self.initUI()


    def initUI(self):
        self.btn = QPushButton("Button", self)
        self.btn.move(30, 50)



class Secend(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # self.usetWindowFlags(Qt.FramelessWindowHint)  # 去边框
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 窗口透明

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = First()
    a.show()
    b = Secend()
    a.btn.clicked.connect(b.show)  # 关键：点击按钮跳转到另一个窗口
    sys.exit(app.exec_())