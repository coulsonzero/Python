import sys
import os
import traceback

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame, QLineEdit, QPushButton, QLabel


# 可拖动黑线
class myQLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.on = False
        self.setStyleSheet("QLabel{background-color: rgb(255,0,0)}")

    def setTypes(self, types):
        self.types = types
        if types == "up" or types == "down":
            self.setCursor(QtGui.QCursor(Qt.SizeVerCursor))
        elif types == "left" or types == "right":
            self.setCursor(QtGui.QCursor(Qt.SizeHorCursor))
        elif types == "leftup" or types == "rightdown":
            self.setCursor(QtGui.QCursor(Qt.SizeFDiagCursor))
        elif types == "leftdown" or types == "rightup":
            self.setCursor(QtGui.QCursor(Qt.SizeBDiagCursor))

    def __dir__(self):
        os._exit(0)
        # exit(0)

    def enterEvent(self, event):
        self.on = True

    def leaveEvent(self, event):
        self.on = False


class webview_main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("天工艺彩")
        self.setWindowIcon(QIcon("C:/TGYC2/src/Photos/mainsPhotos/iconServer.png"))
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗体透明控件不透明
        self.setWindowFlags(Qt.FramelessWindowHint)  # 关闭默认工具栏
        # ============================================
        self.miniWidth = 500  # 最小宽度
        self.miniHeight = 300  # 最小高度
        self.Widths = 1500
        self.Heights = 900
        self.resize(1500, 900)
        self.__m_drag = False  # 是否拖动窗口标志
        self.__clickNow = 0  # 0 无   1 左键   2 右键
        self.types = None  # 当前鼠标放在哪个的边缘
        self.LinesList = [None, None, None, None, None, None, None, None]  # object集合：上下左右四条线  四个角的按钮原点   用于拖拽放大缩小界面
        self.doubleClickData = []  # 双击放大缩小的缓存数据
        self.X = self.pos().x()
        self.Y = self.pos().y()
        # ============================================

        desktopObj = QtWidgets.QApplication.desktop().screenGeometry()
        self.desktopheight = desktopObj.height()
        self.desktopwidth = desktopObj.width()
        self.InitUI()

        # 读取缓存的界面位置与大小
        if os.path.exists('C:/TGYC2/src/FilesTemp/resolution2.a'):
            try:
                with open('C:/TGYC2/src/FilesTemp/resolution2.a', 'r') as f:
                    temp = f.read().split()
                x = int(temp[2])
                y = int(temp[3])
                self.Widths = int(temp[0])
                self.Heights = int(temp[1])
                self.reDraw()
                self.move(x, y)
                self.X = self.pos().x()
                self.Y = self.pos().y()
            except:
                pass

        self.show()

    def InitUI(self):
        self.LayOutFrame = QFrame(self)
        self.LayOutFrame.setGeometry(0, 0, self.size().width(), self.size().height())
        self.LayOutFrame.setObjectName("LayOutFrame")
        self.LayOutFrame.setStyleSheet("#LayOutFrame{background-color:rgb(200,200,200)}"
                                       "#LayOutFrame{border-radius:10px}")

        self.headFrame = QFrame(self.LayOutFrame)
        self.headFrame.setGeometry(10, 10, self.size().width() - 20, 40)
        self.headFrame.setObjectName("headFrame")
        self.headFrame.setStyleSheet("#headFrame{background-color:rgb(50,50,50)}"
                                     "#headFrame{border-radius:10px}")

        # ================================================================================
        ## 回退
        self.btn_back = QPushButton(self.headFrame)
        self.btn_back.setObjectName("btn_back")
        self.btn_back.setGeometry(10, 5, 30, 30)
        self.btn_back.setStyleSheet("QPushButton{border-image:url(C:/TGYC2/src/Photos/webviewer/back.png)}")
        self.btn_back.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.btn_back.setToolTip("后退")
        # self.btn_back.clicked.connect(self.browser.back)

        ## 前进
        self.btn_goAhead = QPushButton(self.headFrame)
        self.btn_goAhead.setObjectName("btn_goAhead")
        self.btn_goAhead.setGeometry(50, 5, 30, 30)
        self.btn_goAhead.setStyleSheet("QPushButton{border-image:url(C:/TGYC2/src/Photos/webviewer/go.png)}")
        self.btn_goAhead.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.btn_goAhead.setToolTip("前进")
        # self.btn_goAhead.clicked.connect(self.browser.forward)

        ## 刷新按钮
        self.btn_refresh = QPushButton(self.headFrame)
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.setGeometry(110, 5, 30, 30)
        self.btn_refresh.setStyleSheet("QPushButton{border-image:url(C:/TGYC2/src/Photos/webviewer/refresh.png)}")
        self.btn_refresh.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.btn_refresh.setToolTip("刷新")

        ## 主页按钮
        self.btn_home = QPushButton(self.headFrame)
        self.btn_home.setObjectName("btn_search")
        self.btn_home.setGeometry(150, 5, 30, 30)
        self.btn_home.setStyleSheet("QPushButton{border-image:url(C:/TGYC2/src/Photos/webviewer/home.png)}")
        self.btn_home.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.btn_home.setToolTip("主页")
        # self.btn_home.clicked.connect(lambda: self.loadWebPage(True, "https://cn.bing.com/"))

        ## 清除缓存
        self.btn_clearCache = QPushButton(self.headFrame)
        self.btn_clearCache.setObjectName("btn_clearCache")
        self.btn_clearCache.setGeometry(self.headFrame.width() - 200, 5, 30, 30)
        self.btn_clearCache.setStyleSheet("QPushButton{border-image:url(C:/TGYC2/src/Photos/webviewer/clearCache.png)}")
        self.btn_clearCache.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.btn_clearCache.setToolTip("清除缓存")
        # self.btn_clearCache.clicked.connect(self.clearCache)

        ## 搜索按钮
        self.btn_search = QPushButton(self.headFrame)
        self.btn_search.setObjectName("btn_search")
        self.btn_search.setGeometry(190, 5, 30, 30)
        self.btn_search.setStyleSheet("QPushButton{border-image:url(C:/TGYC2/src/Photos/webviewer/search.png)}")
        self.btn_search.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.btn_search.setToolTip("搜索")
        self.search_flag = True
        # self.btn_search.clicked.connect(lambda: self.smoothSwitch(self.search_flag))
        # 搜索框
        self.lineEdit_search = QLineEdit(self.headFrame)
        self.lineEdit_search.setGeometry(240, 5, self.headFrame.width() - 900, 30)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.lineEdit_search.setPlaceholderText("  please enter a url like:   www.baidu.com")
        self.lineEdit_search.setStyleSheet("QLineEdit{background-color:rgb(235,235,235)}"
                                           "QLineEdit{border-radius:10px}")
        # ================================================================================

        self.btn_min = QPushButton(self.headFrame)
        self.btn_min.setObjectName("btn_min")
        self.btn_min.setGeometry(self.headFrame.width() - 120, 5, 30, 30)
        self.btn_min.setToolTip("最小化")
        self.btn_min.setStyleSheet("QPushButton{border-image:url(C:/TGYC2/src/Photos/webviewer/min.png)}")
        self.btn_min.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        # self.btn_min.clicked.connect(self.minWindow)  # 最小化

        # MaxButton
        self.btn_max = QPushButton(self.headFrame)
        self.btn_max.setObjectName("btn_max")
        self.btn_max.setGeometry(self.headFrame.width() - 80, 5, 30, 30)
        self.btn_max.setToolTip("最大化")
        self.btn_max.setStyleSheet("QPushButton{border-image:url(C:/TGYC2/src/Photos/webviewer/max.png)}")
        self.btn_max.setCursor(QtGui.QCursor(Qt.PointingHandCursor))

        # CloseButton
        self.btn_close = QPushButton(self.headFrame)
        self.btn_close.setObjectName("C:/TGYC2/src/Photos/webviewer/btn_close")
        self.btn_close.setGeometry(self.headFrame.width() - 40, 5, 30, 30)
        self.btn_close.setToolTip("关闭")
        self.btn_close.setStyleSheet("QPushButton{border-image:url(C:/TGYC2/src/Photos/webviewer/close.png)}")
        self.btn_close.setCursor(QtGui.QCursor(Qt.PointingHandCursor))

        # ===============================================================================

        self.browser = QWebEngineView(self.LayOutFrame)
        self.browser.setGeometry(10, 60, self.size().width() - 20, self.size().height() - 70)
        self.browser.show()

        # ===================================================================================
        # -------------------------------------------------------------------------------------#
        self.LinesList[0] = myQLabel(self)
        self.LinesList[0].setTypes("up")
        self.LinesList[0].setGeometry(30, 0, self.Widths - 60, 5)

        self.LinesList[1] = myQLabel(self)
        self.LinesList[1].setTypes("down")
        self.LinesList[1].setGeometry(30, self.Heights - 5, self.Widths - 60, 5)

        self.LinesList[2] = myQLabel(self)
        self.LinesList[2].setTypes("left")
        self.LinesList[2].setGeometry(0, 30, 5, self.Heights - 60)

        self.LinesList[3] = myQLabel(self)
        self.LinesList[3].setTypes("right")
        self.LinesList[3].setGeometry(self.Widths - 5, 30, 5, self.Heights - 60)

        # 四角的拖动点
        self.LinesList[4] = myQLabel(self)
        self.LinesList[4].setTypes("leftup")
        self.LinesList[4].setGeometry(2, 2, 14, 14)
        self.LinesList[4].setStyleSheet("QLabel{border-radius:7px}"
                                        "QLabel{background-color: rgb(255,0,0)}")

        self.LinesList[5] = myQLabel(self)
        self.LinesList[5].setTypes("rightdown")
        self.LinesList[5].setGeometry(self.Widths - 16, self.Heights - 16, 14, 14)
        self.LinesList[5].setStyleSheet("QLabel{border-radius:7px}"
                                        "QLabel{background-color: rgb(255,0,0)}")

        self.LinesList[6] = myQLabel(self)
        self.LinesList[6].setTypes("leftdown")
        self.LinesList[6].setGeometry(5, self.Heights - 16, 14, 14)
        self.LinesList[6].setStyleSheet("QLabel{border-radius:7px}"
                                        "QLabel{background-color: rgb(255,0,0)}")

        self.LinesList[7] = myQLabel(self)
        self.LinesList[7].setTypes("rightup")
        self.LinesList[7].setGeometry(self.Widths - 16, 2, 14, 14)
        self.LinesList[7].setStyleSheet("QLabel{border-radius:7px}"
                                        "QLabel{background-color: rgb(255,0,0)}")

    def reDraw(self):
        self.move(self.X, self.Y)
        self.resize(self.Widths, self.Heights)

        self.LayOutFrame.setGeometry(0, 0, self.size().width(), self.size().height())
        self.headFrame.setGeometry(10, 10, self.size().width() - 20, 40)
        self.btn_min.setGeometry(self.headFrame.width() - 120, 5, 30, 30)
        self.btn_max.setGeometry(self.headFrame.width() - 80, 5, 30, 30)
        self.btn_close.setGeometry(self.headFrame.width() - 40, 5, 30, 30)
        self.browser.setGeometry(10, 60, self.size().width() - 20, self.size().height() - 70)
        self.btn_clearCache.setGeometry(self.headFrame.width() - 200, 5, 30, 30)

        self.LinesList[0].setGeometry(30, 0, self.Widths - 60, 5)
        self.LinesList[1].setGeometry(30, self.Heights - 5, self.Widths - 60, 5)
        self.LinesList[2].setGeometry(0, 30, 5, self.Heights - 60)
        self.LinesList[3].setGeometry(self.Widths - 5, 30, 5, self.Heights - 60)
        self.LinesList[4].setGeometry(2, 2, 14, 14)
        self.LinesList[5].setGeometry(self.Widths - 16, self.Heights - 16, 14, 14)
        self.LinesList[6].setGeometry(5, self.Heights - 16, 14, 14)
        self.LinesList[7].setGeometry(self.Widths - 16, 2, 14, 14)

    def start(self, url):
        self.browser.show()
        self.browser.load(QUrl(url))

    def end(self):
        self.browser.close()

    # 双击全屏
    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            if event.localPos().y() <= 40.0 and event.localPos().y() > 5.0:
                if self.doubleClickData == []:
                    self.doubleClickData = [self.X, self.Y, self.Widths, self.Heights]
                    nowX = event.globalPos().x()
                    if nowX < 0:
                        self.X = self.desktopwidth * -1
                        self.Y = 0
                    elif nowX >= 0 and nowX < self.desktopwidth:
                        self.X = self.Y = 0
                    elif nowX >= self.desktopwidth:
                        self.X = self.desktopwidth
                        self.Y = 0
                    self.Widths, self.Heights = self.desktopwidth, self.desktopheight - 30
                    self.reDraw()
                else:
                    self.X, self.Y, self.Widths, self.Heights = self.doubleClickData[0], self.doubleClickData[1], \
                                                                self.doubleClickData[2], self.doubleClickData[3]
                    self.reDraw()
                    self.doubleClickData = []
                with open('C:/TGYC2/src/FilesTemp/resolution2.a', 'w') as f:
                    f.write("%d %d %d %d" % (self.Widths, self.Heights, self.X, self.Y))

    def mousePressEvent(self, event):
        try:
            if event.button() == Qt.LeftButton:
                self.__clickNow = 1
                if event.localPos().y() <= 40.0 and event.localPos().y() > 5.0 and event.localPos().x() <= self.Widths - 50.0 and event.localPos().x() > 50.0:
                    self.__m_drag = True
                    self.m_DragPosition = event.globalPos() - self.pos()
                else:
                    for i in self.LinesList:
                        if i.on:
                            self.types = i.types
                            break
            elif event.button() == Qt.RightButton:
                self.__clickNow = 2
        except:
            traceback.print_exc()

    def mouseMoveEvent(self, QMouseEvent):
        try:
            if self.__clickNow == 1:
                if self.__m_drag:
                    self.move(QMouseEvent.globalPos() - self.m_DragPosition)
                    self.X = self.pos().x()
                    self.Y = self.pos().y()
                    QMouseEvent.accept()
                    return
                elif self.types == "up":
                    high = (self.pos().y() + self.height()) - QMouseEvent.globalPos().y()
                    if high > self.miniHeight:
                        self.Heights = high
                        self.Y = QMouseEvent.globalPos().y()
                elif self.types == "down":
                    if QMouseEvent.globalPos().y() < (self.desktopheight - 30):
                        high = QMouseEvent.globalPos().y() - self.pos().y()
                        if high > self.miniHeight:
                            self.Heights = high
                elif self.types == "left":
                    wid = (self.pos().x() + self.width()) - QMouseEvent.globalPos().x()
                    if wid > self.miniWidth:
                        self.Widths = wid
                        self.X = QMouseEvent.globalPos().x()
                elif self.types == "right":
                    wid = QMouseEvent.globalPos().x() - self.pos().x()
                    if wid > self.miniWidth:
                        self.Widths = wid

                elif self.types == "leftup":
                    high = (self.pos().y() + self.height()) - QMouseEvent.globalPos().y()
                    if high > self.miniHeight:
                        self.Heights = high
                        self.Y = QMouseEvent.globalPos().y()
                    wid = (self.pos().x() + self.width()) - QMouseEvent.globalPos().x()
                    if wid > self.miniWidth:
                        self.Widths = wid
                        self.X = QMouseEvent.globalPos().x()
                elif self.types == "rightdown":
                    wid = QMouseEvent.globalPos().x() - self.pos().x()
                    if wid > self.miniWidth:
                        self.Widths = wid
                    if QMouseEvent.globalPos().y() < (self.desktopheight - 30):
                        high = QMouseEvent.globalPos().y() - self.pos().y()
                        if high > self.miniHeight:
                            self.Heights = high
                elif self.types == "leftdown":
                    wid = (self.pos().x() + self.width()) - QMouseEvent.globalPos().x()
                    if wid > self.miniWidth:
                        self.Widths = wid
                        self.X = QMouseEvent.globalPos().x()
                    if QMouseEvent.globalPos().y() < (self.desktopheight - 30):
                        high = QMouseEvent.globalPos().y() - self.pos().y()
                        if high > self.miniHeight:
                            self.Heights = high
                elif self.types == "rightup":
                    wid = QMouseEvent.globalPos().x() - self.pos().x()
                    if wid > self.miniWidth:
                        self.Widths = wid
                    high = (self.pos().y() + self.height()) - QMouseEvent.globalPos().y()
                    if high > self.miniHeight:
                        self.Heights = high
                        self.Y = QMouseEvent.globalPos().y()
                if self.types is not None:
                    self.reDraw()
        except:
            traceback.print_exc()

    def mouseReleaseEvent(self, QMouseEvent):
        try:
            if self.__clickNow == 1 and self.types is not None:
                # 记住最后位置
                with open('C:/TGYC2/src/FilesTemp/resolution2.a', 'w') as f:
                    f.write("%d %d %d %d" % (self.Widths, self.Heights, self.X, self.Y))

            self.types = None
            self.__clickNow = 0
            if self.__m_drag:
                self.__m_drag = False
                with open('C:/TGYC2/src/FilesTemp/resolution2.a', 'w') as f:
                    f.write("%d %d %d %d" % (self.Widths, self.Heights, self.X, self.Y))
        except:
            traceback.print_exc()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = webview_main()
    w.end()
    w.start('http://www.baidu.com')
    # w.showMaximized()
    sys.exit(app.exec_())
