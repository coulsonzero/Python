"""
@author: coulson
@version: 2021/7/23  11:05

进度条
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QBasicTimer


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.lab2 = QLabel("lab2", self)
        self.lab2.setGeometry(30, 40, 300, 40)
        self.lab1 = QLabel("lab1", self)
        self.lab1.setGeometry(30, 40, 200, 40)



        self.lab1.setStyleSheet(
            "QLabel {background-color: green}"
            "QLabel {border-radius: 10px}"
            "QLabel {}"
        )
        self.lab2.setStyleSheet(
            "QLabel {background-color: red}"
            "QLabel {border-radius: 10px}"
        )


        # self.pbar = QProgressBar(self)
        # self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        # self.btn.clicked.connect(self.doAction)

        # self.btn.setstyleSheet(
        #     "QPushButton{background-color:rgb(111,180,219)}"  # 按键背景色
        #     "QPushButton:hover{color:green}"  # 光标移动到上面后的前景色
        #     "QPushButton{border-radius:6px}"  # 圆角半径
        #     "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        # )

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 5
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Continue')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())