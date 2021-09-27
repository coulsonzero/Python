"""
@author: coulson
@version: 2021/7/23  11:15
"""
import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
                             QLabel, QApplication)
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        lbl = QLabel(self)
        lbl.setPixmap(QPixmap(r"C:\Users\Administrator\Desktop\img.jpg"))

        hbox = QHBoxLayout(self)
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())