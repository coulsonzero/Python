import sys
import time
import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import QNetworkProxyFactory
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from icecream import ic


class myWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('QProgressBar')
        self.resize(600, 400)
        self.setupUi()
        self.setStyleSheet(
            """
            QProgressBar{
            font: 9pt;
            text-align:center;
            border-radius: 12px;
            border: 2px solid #E8EDF2;
            background-color: white;
            border-color: rgb(180, 180, 180); 
            }
            QProgressBar:chunk{
            border-radius: 12px;
            background-color: rgb(122, 122, 182);
            border: 1px solid #E8EDF2;
            }
            """)
        self.show()

    def setupUi(self):
        ########### 底板 #################
        self.stylesheet = QFrame(self)
        self.stylesheet.setObjectName('stylesheet')
        self.stylesheet.setGeometry(QRect(0, 0, 600, 400))

        """进度条"""
        self.pbar = QProgressBar(self.stylesheet)
        self.pbar.setGeometry(200, 150, 300, 20)

        self.timer = QBasicTimer()
        self.step = 0

        """开始按钮"""
        self.btn = QPushButton(self.stylesheet)
        self.btn.setText("start")
        self.btn.setGeometry(500, 130, 40, 20)
        self.btn.clicked.connect(self.doAction)

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = myWindow()
    sys.exit(app.exec_())
