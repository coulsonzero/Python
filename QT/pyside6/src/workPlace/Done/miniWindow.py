

#############################################################################
#                                                                           #
#                                                                           #
#                              小窗口                                        #
#                                                                           #
#                                                                           #
#############################################################################



import sys
import time

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore


class Window(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setObjectName("Window")
        # self.resize(447, 381)

        self.setWindow()    # 初始化窗口
        self.setupUi()
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
        self.frame = QFrame(self)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(80, 70, 280, 201))
        self.frame.setStyleSheet(
            """
            #frame {
	            background-color: white;
	             border-radius: 10px;
            } 
            """
        )
        ########## 标题
        self.label_title = QLabel(self.frame)
        self.label_title.setObjectName("label_title")
        self.label_title.setGeometry(QRect(11, 5, 121, 21))
        self.label_title.setText("文件更新通知")
        self.label_title.setStyleSheet(
            """
            #label_title {
                color: rgb(162, 162, 243);
                font-weight: bold;
            }
            """
        )

        ##################### 关闭按钮 ######################
        self.btn_close = QPushButton(self.frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(251, 3, 21, 21))
        self.btn_close.clicked.connect(QCoreApplication.instance().quit)  # 关闭
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



        ####### 中间组件 ########
        self.Box = QFrame(self.frame)
        self.Box.setObjectName("Box")
        self.Box.setGeometry(QRect(-10, 30, 301, 153))
        self.Box.setStyleSheet(
            """
            #Box {
	         background-color: #e4e9ee;
	         border-radius: 10px;
            }
            """
        )
        self.Box.setFrameShape(QFrame.StyledPanel)
        self.Box.setFrameShadow(QFrame.Raised)

        ################ 中间左侧组件 #################
        self.leftBox = QFrame(self.Box)
        self.leftBox.setObjectName("leftBox")
        self.leftBox.setGeometry(QRect(22, -1, 61, 141))
        self.verticalLayout = QVBoxLayout(self.leftBox)
        self.verticalLayout.setObjectName("verticalLayout")


        # 任务
        self.label_1 = QLabel(self.leftBox)
        self.label_1.setObjectName("label_1")
        self.label_1.setText("任务:")
        self.verticalLayout.addWidget(self.label_1)

        # 节点
        self.label_2 = QLabel(self.leftBox)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("节点:")
        self.verticalLayout.addWidget(self.label_2)

        # 项目
        self.label_3 = QLabel(self.leftBox)
        self.label_3.setObjectName("label_3")
        self.label_3.setText("项目:")
        self.verticalLayout.addWidget(self.label_3)

        # 简介
        self.label_4 = QLabel(self.leftBox)
        self.label_4.setObjectName("label_4")
        self.label_4.setText("简介:")
        self.verticalLayout.addWidget(self.label_4)

        # 更新
        self.label_5 = QLabel(self.leftBox)
        self.label_5.setObjectName("label_5")
        self.label_5.setText("更新:")
        self.verticalLayout.addWidget(self.label_5)




        ############ 中间右侧组件 ##############
        self.rightBox = QFrame(self.Box)
        self.rightBox.setObjectName("rightBox")
        self.rightBox.setGeometry(QRect(62, 0, 221, 141))
        self.verticalLayout_2 = QVBoxLayout(self.rightBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # CH_A01_FANGhAN
        self.label_6 = QLabel(self.rightBox)
        self.label_6.setObjectName("label_6")
        self.label_6.setText("CH_A01_FANGhAN")
        self.label_6.setStyleSheet(
            """
            #label_6 {
                font-weight: bold;
            }
            """
        )
        self.verticalLayout_2.addWidget(self.label_6)

        # 绑定mo
        self.label_7 = QLabel(self.rightBox)
        self.label_7.setObjectName("label_7")
        self.label_7.setText("绑定mo")
        self.verticalLayout_2.addWidget(self.label_7)

        # 永生
        self.label_8 = QLabel(self.rightBox)
        self.label_8.setObjectName("label_8")
        self.label_8.setText("永生")
        self.verticalLayout_2.addWidget(self.label_8)

        # 更新衣服穿帮
        self.label_9 = QLabel(self.rightBox)
        self.label_9.setObjectName("label_9")
        self.label_9.setText("更新衣服穿帮")
        self.verticalLayout_2.addWidget(self.label_9)

        self.rightBottomBox = QFrame(self.rightBox)
        self.rightBottomBox.setObjectName("rightBottomBox")
        # name
        self.label_10 = QLabel(self.rightBottomBox)
        self.label_10.setObjectName("label_10")
        self.label_10.setGeometry(QRect(1, 1, 61, 16))
        self.label_10.setText("李白")

        # time
        self.label_11 = QLabel(self.rightBottomBox)
        self.label_11.setObjectName("label_11")
        self.label_11.setGeometry(QRect(61, 1, 151, 20))
        self.label_11.setText(time.strftime('%Y/%m/%d  %H:%M:%S'))
        self.verticalLayout_2.addWidget(self.rightBottomBox)








        ########## 底部按钮 ############
        self.frame_bottom = QFrame(self.frame)
        self.frame_bottom.setObjectName("frame_bottom")
        self.frame_bottom.setGeometry(QRect(0, 169, 280, 34))
        self.frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.frame_bottom.setStyleSheet(
            """
            #frame_bottom {
	            background-color: #e4e9ee;
	            border-radius: 10px;
            }
            """
        )

        ##################### 查看详情按钮 #####################
        self.btn_view = QPushButton(self.frame_bottom)
        self.btn_view.setObjectName("btn_view")
        self.btn_view.setText("查看详情>>")
        self.btn_view.setGeometry(QRect(100, 4, 75, 24))
        self.btn_view.setStyleSheet(
            """
            #btn_view{
	            background-color:  #e4e9ee;
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






    #############################################################################
    #                                功能模块                                    #
    #############################################################################

    # --------------自定义窗口移动方法----------
    def mousePressEvent(self, QMouseEvent):
        # 改为拖动按钮
        if QMouseEvent.button() == Qt.LeftButton:
            self.flag = True
            # 获取鼠标相对窗口的位置
            self.m_Position = QMouseEvent.globalPos() - self.pos()
            QMouseEvent.accept()
            # 更改鼠标图标
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        # 去掉此方法，则无法拖动
        if Qt.LeftButton and self.flag:
            # 更改窗口位置
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        # 设置后只能在顶部空白处才能拖动，组件位置不可拖动
        self.flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def keyPressEvent(self, e):
        # 按“Esc”键退出程序！
        if e.key() == Qt.Key_Escape:
            self.close()


    def regularRefreshPage(self):
        """
        定时执行刷新界面
        """
        self.timer = QTimer()
        self.timer.start(5)
        self.timer.timeout.connect(self.refreshPage)

    def refreshPage(self):
        """
        刷新页面
        """
        QApplication.processEvents()

    def resizeWindow(self, width, height):
        self.frame.width = width
        self.frame.height = height
        self.frame.resize(self.frame.width, self.frame.height)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())
