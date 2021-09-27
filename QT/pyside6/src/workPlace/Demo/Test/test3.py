# -*- coding: utf-8 -*-
"""
@Author: coulson
@Version: python3.9
@DateTime: 2021/9/1  13:43
"""
import sys
import time

import psutil

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Demo.ProcessBar import sysInfo


class myWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(600, 300)
        self.setup()  # 初始化组件
        self.loadQss()
        self.show()


    def setup(self):
        # 底板
        self.frame = QFrame(self)
        self.frame.setObjectName("frame")

        self.pbar = QProgressBar(self.frame)
        self.pbar.setGeometry(150, 80, 300, 10)
        # self.timer = QBasicTimer()
        # self.step = 0

        """开始按钮"""
        self.btn = QPushButton(self.frame)
        self.btn.setText("start")
        self.btn.setGeometry(70, 80, 40, 20)
        # self.btn.clicked.connect(self.btnClick)
        self.btn.clicked.connect(self.getCPU)


    def btnClick(self):
        self.my_thread = MyThread()
        self.my_thread.my_signal.connect(self.setP)
        self.my_thread.start()
        self.updateProcessBar()

    def updateProcessBar(self):
        self.val = self.getCPU()
        self.pbar.setValue(self.val)

    def setP(self, p):
        self.persent = p

    def getCPU(self):
        return psutil.cpu_percent(interval=1)

    def loadQss(self):
        self.setStyleSheet(
            '''
            /* 外框 */
QProgressBar{
font: 9pt;
text-align:center;


border-radius: 5px;
border: 1px solid #E8EDF2;
background-color: white; /* 容器颜色 */
border-color: rgb(180, 180, 180); /* 边框颜色 */
}
/* 加载条 */
QProgressBar:chunk{
border-radius: 3px;
background-color: rgb(122, 122, 182);
}
            '''
        )



class MyThread(QThread):
    def __init__(self, parent=None):
        super(MyThread, self).__init__(parent)
    def run(self):
        p = myWindow.getCPU()
        print(p)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = myWindow()

    sys.exit(app.exec_())