import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class myWindow(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("myWindow")


        self.setupUi()  # 初始化组件
        self.setWindow()  # 初始化窗口
        self.loadQss()
        self.show()

    def setupUi(self):
        # 底板
        self.frame = QFrame(self)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(80, 70, 400, 300))


















#############################################################################
#                                隐藏外窗口                                  #
#############################################################################
    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)  # 关闭默认工具栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明

        # CloseButton
        self.btn_close = QPushButton(self.frame)
        self.btn_close.setObjectName("btn_close")
        self.btn_close.setGeometry(QRect(self.frame.width() - 30, 10, 21, 21))
        self.btn_close.setToolTip("关闭")
        self.btn_close.setIcon(QIcon("close.png"))

        # MaxButton
        self.btn_max = QPushButton(self.frame)
        self.btn_max.setObjectName("btn_max")
        self.btn_max.setGeometry(QRect(self.frame.width() - 60, 10, 21, 21))
        self.btn_max.setToolTip("最大化")
        self.btn_max.setIcon(QIcon("max.png"))

        # MinButton
        self.btn_min = QPushButton(self.frame)
        self.btn_min.setObjectName("btn_min")
        self.btn_min.setGeometry(QRect(self.frame.width() - 90, 10, 21, 21))
        self.btn_min.setToolTip("最小化")
        self.btn_min.setIcon(QIcon("min.png"))

        ## 信号处理
        self.btn_close.clicked.connect(QCoreApplication.instance().quit)  # 关闭
        self.getScreenSize()  # 最大化窗口需获取窗口分辨率
        self.btn_max.clicked.connect(self.maxWindow)                      # 最大化
        self.btn_min.clicked.connect(self.showMinimized)                  # 最小化


    def getScreenSize(self):
        # 最大化窗口获取屏幕分辨率
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()
        self.resize(self.width, self.height)

    @pyqtSlot()
    def maxWindow(self):
        if self.isMaximized():
            self.showNormal()
        else:
            # self.showMaximized()
            self.frame.setGeometry(0, 0, self.width, self.height)
            self.btn_close.setGeometry(QRect(self.frame.width() - 30, 10, 21, 21))
            self.btn_max.setGeometry(QRect(self.frame.width() - 60, 10, 21, 21))
            self.btn_min.setGeometry(QRect(self.frame.width() - 90, 10, 21, 21))

    def loadQss(self):
        """
        加载css样式
        """
        with open("style.qss") as f:
            qss = f.read()
        self.setStyleSheet(qss)


    #############################################################################
    #                                功能模块                                    #
    #############################################################################

    # --------------自定义窗口移动方法----------
    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.flag = True
            self.m_Position = QMouseEvent.globalPos() - self.pos()
            QMouseEvent.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))


    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()


    def mouseReleaseEvent(self, QMouseEvent):
        self.flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def keyPressEvent(self, e):
        # 按“Esc”键退出程序！
        if e.key() == Qt.Key_Escape:
            self.close()
    """
    def redraw(self, width, height):
        self.width = width
        self.height = height
        self.resize(self.width, self.height)
    """


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = myWindow()
    sys.exit(app.exec_())