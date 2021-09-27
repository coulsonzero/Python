import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

"""
class tipsWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
"""


class myWindow(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("myWindow")
        self.resize(447, 381)
        # self.setStyleSheet()
        self.setWindow()    # 初始化窗口
        self.setupUi()       # 初始化组件
        self.show()

    #############################################################################
    #                                隐藏外窗口                                  #
    #############################################################################
    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)  # 关闭默认工具栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明
        # self.loadQss()
        # # 自定义窗口按钮
        # self.btn_close.clicked.connect(QCoreApplication.instance().quit)  # 关闭
        # self.btn_min.clicked.connect(self.showMinimized)  # 最小化
        # self.btn_max.clicked.connect(self.btnClick)  # 最大化




    #############################################################################
    #                                窗体ui设计                                  #
    #############################################################################
    def setupUi(self):
        ######### 底部 #######
        self.frame = QFrame(self)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(80, 70, 280, 201))
        self.frame.setStyleSheet('''
                                #frame {
                                    background-color: white;
                                    border-radius: 10px;
                                } 
                                ''')

        ##################### 查看详情按钮 #####################
        self.btn_view = QPushButton(self.frame)
        self.btn_view.setObjectName("btn_view")
        self.btn_view.setText("查看详情>>")
        self.btn_view.setGeometry(QRect(100, 4, 75, 24))
        self.btn_view.setStyleSheet(
            ##e4e9ee
            """
            #btn_view{
                background-color:  white;
                border: 1px solid #e4e9ee;
                color: rgb(126, 126, 126);
            }
            #btn_view:hover{
                background-color: rgb(170, 170, 127);
                border: solid 5px rgb(0, 255, 255);
                background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, 
                                stop:0 lightCyan,
                                stop:0.5  SkyBlue ,
                                stop:1 deepSkyBlue
            );
            border-radius: 10px;
            }	
            #btn_view:pressed{
                color: red;
            }
            """
        )

        ##################### 关闭按钮 ######################
        self.btn_close = QPushButton(self.frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(251, 3, 21, 21))
        self.btn_close.clicked.connect(QCoreApplication.instance().quit)  # 关闭
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))  # 鼠标拖至此处时展示样式
        icon = QIcon()
        icon.addFile("C:/Users/Administrator/Desktop/images/close3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon)
        self.btn_close.setStyleSheet(
            """
            #btn_close{
                background-color: white;
                border: 1px solid white;
            }
             #btn_close:hover {
                background-color: rgb(170, 170, 127);
                border: solid 5px rgb(0, 255, 255);
                background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, 
                                            stop:0 lightCyan,
                                            stop:0.5  SkyBlue ,
                                            stop:1 deepSkyBlue
                );
                border-radius: 10px;
            }	
            #btn_close:pressed{
                background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1,
                                  stop:0 rgb(255, 0, 255),
                                  stop:0.5  SkyBlue ,
                                  stop:1 rgb(85, 255, 127)
            );}
            """
        )

    def btnClick(self):
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "btn_MaxShow":
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = myWindow()
    sys.exit(app.exec_())