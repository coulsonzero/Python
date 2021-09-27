"""
@author: coulson
@version: 2021/7/28  10:49
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PySide6.QtGui import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)    # 窗口的位置和大小
        self.setWindowTitle('Icon')             # 窗口的标题
        self.setWindowIcon(QIcon('logo.ico'))   # 设窗口图标


        # self.usetWindowFlags(Qt.FramelessWindowHint)  # 去边框
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 窗口透明



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    w.show()
    sys.exit(app.exec_())