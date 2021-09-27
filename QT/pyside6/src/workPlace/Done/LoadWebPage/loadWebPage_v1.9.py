"""
@author: coulson
@version: 2021/8/24  17:14
"""

import sys
import time
import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import QNetworkProxyFactory
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from icecream import ic


class myWindow(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("myWindow")
        self.resize(1200, 800)  # 去掉框布局
        self.setMinimumSize(500, 100)
        self.setupUi()  # 初始化组件
        self.setWindow()  # 初始化窗口
        self.show()

    def setupUi(self):
        ########### 底板 #################
        self.frame = QFrame(self)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(0, 0, 1200, 800))

        ########### 顶部菜单条 ############
        self.topBar = QFrame(self.frame)
        self.topBar.setObjectName("topBar")
        self.topBar.setGeometry(QRect(10, 10, self.frame.width() - 20, 40))
        self.topBar.setCursor(QCursor(Qt.ArrowCursor))
        self.topBar.setFixedHeight(40)

        ############ 浏览器 ##############
        self.browser = QWebEngineView(self.frame)
        self.browser.setObjectName("browser")
        self.browser.setGeometry(10, 60, self.frame.width() - 20, self.frame.height() - 70)
        QNetworkProxyFactory.setUseSystemConfiguration(False)  # 取消代理，加快网页加载速度

        # 回退
        self.btn_back = QPushButton(self.topBar)
        self.btn_back.setObjectName("btn_back")
        self.btn_back.setGeometry(QRect(10, 5, 30, 30))
        self.btn_back.setIcon(QIcon("back.png"))
        self.btn_back.setIconSize(QSize(30, 30))
        self.btn_back.setToolTip("后退")
        self.btn_back.clicked.connect(self.browser.back)
        # 前进
        self.btn_goAhead = QPushButton(self.topBar)
        self.btn_goAhead.setObjectName("btn_goAhead")
        self.btn_goAhead.setGeometry(QRect(50, 5, 30, 30))
        self.btn_goAhead.setIcon(QIcon("go.png"))
        self.btn_goAhead.setIconSize(QSize(30, 30))
        self.btn_goAhead.setToolTip("前进")
        self.btn_goAhead.clicked.connect(self.browser.forward)

        # 刷新按钮
        self.btn_refresh = QPushButton(self.topBar)
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.setGeometry(QRect(110, 5, 30, 30))
        self.btn_refresh.setIcon(QIcon("refresh.png"))
        self.btn_refresh.setIconSize(QSize(20, 20))
        self.refresh_flag = True  # 随时可刷新
        self.btn_refresh.clicked.connect(lambda: self.refreshPage(self.refresh_flag))
        self.btn_refresh.setToolTip("重新加载此页")

        # 清除缓存
        self.btn_clearCache = QPushButton(self.topBar)
        self.btn_clearCache.setObjectName("btn_clearCache")
        self.btn_clearCache.setGeometry(QRect(self.frame.width() - 210, 5, 30, 30))
        self.btn_clearCache.setIcon(QIcon("clearCache.png"))
        self.btn_clearCache.setIconSize(QSize(20, 20))
        self.btn_clearCache.setToolTip("清除缓存")
        self.btn_clearCache.clicked.connect(self.clearCache)

        # 主页按钮
        self.btn_home = QPushButton(self.topBar)
        self.btn_home.setObjectName("btn_search")
        self.btn_home.setGeometry(QRect(QRect(150, 5, 30, 30)))
        self.btn_home.setIcon(QIcon("home.png"))
        self.btn_home.setIconSize(QSize(24, 24))
        self.btn_home.setToolTip("主页")
        self.btn_home.clicked.connect(lambda: self.loadWebPage(True, "https://cn.bing.com/"))
        self.btn_home.setEnabled(False)
        self.btn_home.hide()

        # 搜索按钮
        self.btn_search = QPushButton(self.topBar)
        self.btn_search.setObjectName("btn_search")
        self.btn_search.setGeometry(QRect(190, 5, 30, 30))
        self.btn_search.setIcon(QIcon("search.png"))
        self.btn_search.setIconSize(QSize(24, 24))
        self.btn_search.setToolTip("搜索")
        self.search_flag = True
        self.btn_search.clicked.connect(lambda: self.smoothSwitch(self.search_flag))
        self.btn_search.setEnabled(False)
        self.btn_search.hide()
        # 搜索框
        self.lineEdit_search = QLineEdit(self.topBar)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.lineEdit_search.setPlaceholderText("  please enter a url like:   www.baidu.com")
        self.lineEdit_search.setEnabled(False)
        self.lineEdit_search.hide()

    def setWindow(self):
        """界面初始化"""
        self.setWindowFlags(Qt.FramelessWindowHint)  # 关闭默认工具栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明

        # MinButton
        self.btn_min = QPushButton(self.topBar)
        self.btn_min.setObjectName("btn_min")
        self.btn_min.setGeometry(QRect(self.frame.width() - 150, 5, 30, 30))
        self.btn_min.setToolTip("最小化")
        self.btn_min.setIcon(QIcon("min.png"))
        self.btn_min.setIconSize(QSize(20, 20))
        self.btn_min.clicked.connect(self.minWindow)

        # MaxButton
        self.btn_max = QPushButton(self.topBar)
        self.btn_max.setObjectName("btn_max")
        self.btn_max.setGeometry(QRect(self.frame.width() - 110, 5, 30, 30))
        self.btn_max.setToolTip("最大化")
        self.btn_max.setIcon(QIcon("max.png"))
        self.btn_max.setIconSize(QSize(20, 20))
        self.btn_max.clicked.connect(self.maxWindow)

        # CloseButton
        self.btn_close = QPushButton(self.topBar)
        self.btn_close.setObjectName("btn_close")
        self.btn_close.setGeometry(QRect(self.frame.width() - 70, 5, 30, 30))
        self.btn_close.setToolTip("关闭")
        self.btn_close.setIcon(QIcon("close.png"))
        self.btn_close.setIconSize(QSize(20, 20))
        self.btn_close.clicked.connect(QCoreApplication.instance().quit)  # 关闭

        ############# 记载qss样式 ###############
        self.loadQss()
        ############# 鼠标事件初始化 #############
        self.flag = False  # 拖动按钮不会报错
        self.on = False  # 鼠标移动初始化
        self._initDrag()  # 设置鼠标跟踪判断扳机默认值
        self.setMouseTracking(True)  # 设置widget鼠标跟踪

        ############# 加载主页 ##################
        # home_url = "https://cn.bing.com/"
        home_url = "http://task.tgyc.com/#/login?redirect=%2Findex"
        self.loadWebPage(True, home_url)

    def minWindow(self):
        """ 最小化 """
        try:
            self.showMinimized()
        except:
            time.sleep(500)
            print("error")
            self.refreshPage(True)
            time.sleep(1)
            self.showMinimized()

    def maxWindow(self):
        """ 最大化 """
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
            # self.frame.setGeometry(QRect(0, 0, self.width(), self.height()))
        self.redraw()

    def loadQss(self):
        """ 加载qss样式 """
        with open("style.qss") as f:
            qss = f.read()
        self.setStyleSheet(qss)

    def loadWebPage(self, enable, url="https://cn.bing.com/"):
        """ 加载网页 """

        # 搜索输入框网址处理
        input_url = self.lineEdit_search.text().strip()
        if input_url != "":
            if not (input_url.startswith("https://") or input_url.startswith("http://")):
                input_url = "http://" + input_url
            url = input_url
            print(f"正在进入该网址 -> {url}")

        # 点击主页按钮
        btn = self.sender()
        if btn == self.btn_home:
            url = "https://cn.bing.com/"
            print("Display home page ...")

        # 加载网页(主页/指定页面)
        if enable:
            self.browser.load(QUrl(url))
            self.browser.show()
            # 获取当前网页网址，并显示到导航栏上
            self.browser.urlChanged.connect(lambda: self.lineEdit_search.setText(self.browser.url().toDisplayString()))

    def refreshPage(self, enable):
        """
        刷新： 当搜索框隐藏后，点击刷新不再重复关闭搜索栏动画效果
        """
        if enable and self.lineEdit_search.width() != 0:
            # QApplication.processEvents()
            self.smoothSwitch2(True)  # 关闭搜索框
            self.refresh_flag = False  # 点击刷新不再重复关闭搜索栏动画效果
        self.browser.reload()  # 刷新重载网页
        print("refresh ...")

    def clearCache(self):
        """清空缓存"""
        QWebEngineProfile.defaultProfile().cookieStore().deleteAllCookies()
        self.refreshPage(True)  # 刷新
        print("clearCache...")

    def smoothSwitch(self, enable):
        """点击搜索按钮弹出搜索输入框：平滑切换效果, 隐藏搜索按钮，显示搜索框"""
        if enable:
            self.lineEdit_search.show()
            self.animation = QPropertyAnimation(self.lineEdit_search, b"geometry")
            self.animation.setDuration(900)
            self.animation.setStartValue(QRect(190, 5, 0, 30))
            self.animation.setEndValue(QRect(190, 5, self.frame.width() - 440, 30))
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
        self.refresh_flag = True  # 可点击刷新关闭搜索栏
        self.lineEdit_search.returnPressed.connect(lambda: self.loadWebPage(True))

    # 点击刷新关闭搜索栏
    def smoothSwitch2(self, enable):
        self.animation = QPropertyAnimation(self.lineEdit_search, b"geometry")
        self.animation.setDuration(500)
        self.animation.setStartValue(QRect(190, 5, self.frame.width() - 440, 30))
        self.animation.setEndValue(QRect(190, 5, 0, 30))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
        # self.btn_search.show()

    def redraw(self):
        """窗口大小变化时，topBar内的按钮位置重置"""
        # self.resize(self.width(), self.height())
        self.frame.setGeometry(QRect(0, 0, self.width(), self.height()))
        self.topBar.setGeometry(QRect(10, 10, self.frame.width() - 20, 40))
        self.browser.setGeometry(10, 60, self.frame.width() - 20, self.frame.height() - 70)
        self.btn_back.setGeometry(QRect(10, 5, 30, 30))
        self.btn_goAhead.setGeometry(QRect(50, 5, 30, 30))
        self.btn_refresh.setGeometry(QRect(110, 5, 30, 30))
        self.btn_home.setGeometry(QRect(QRect(150, 5, 30, 30)))
        self.btn_search.setGeometry(QRect(190, 5, 30, 30))
        self.lineEdit_search.setGeometry(QRect(190, 5, 0, 30))
        self.btn_clearCache.setGeometry(QRect(self.frame.width() - 210, 5, 30, 30))
        self.btn_min.setGeometry(QRect(self.frame.width() - 150, 5, 30, 30))
        self.btn_max.setGeometry(QRect(self.frame.width() - 110, 5, 30, 30))
        self.btn_close.setGeometry(QRect(self.frame.width() - 70, 5, 30, 30))

    def resizeEvent(self, event):
        self._right_rect = [list(range(self.frame.width() - 10, self.frame.width() + 25)),
                            list(range(self.frame.y() + 20, self.frame.height() - 30))]
        self._bottom_rect = [list(range(self.x() + 20, self.width() - 20)),
                             list(range(self.height() - 10, self.height() + 10))]
        self._corner_rect = [list(range(self.frame.width() - 15, self.frame.width() + 20)),
                             list(range(self.frame.height() - 15, self.frame.height() + 15))]
        self._top_rect = [list(range(self.frame.x() + 20, self.frame.width() - 20)),
                          list(range(self.frame.y(), self.frame.y() + 50))]


        self._left_rect = [list(range(self.frame.x()-30, self.frame.x()+20)), list(range(self.frame.y()+20, self.frame.height()-30))]


    def enterEvent(self, event):
        """ 鼠标进入界面区域拖动指针样式 """
        self.on = True
        right = event.pos().x() in self._right_rect[0] and event.pos().y() in self._right_rect[1]
        bottom = event.pos().x() in self._bottom_rect[0] and event.pos().y() in self._bottom_rect[1]
        corner = event.pos().x() in self._corner_rect[0] and event.pos().y() in self._corner_rect[1]
        top = event.pos().x() in self._top_rect[0] and event.pos().y() in self._top_rect[1]

        left = event.pos().x() in self._left_rect[0] and event.pos().y() in self._left_rect[1]

        if self.on:
            if left or right:
                self.setCursor(Qt.SizeHorCursor)
            elif bottom:
                self.setCursor(Qt.SizeVerCursor)
            elif corner:
                self.setCursor(Qt.SizeFDiagCursor)
            elif top:
                if not (self.isMaximized()):
                    self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改为移动窗口指针
            else:
                # 常规指针
                self.setCursor(QCursor(Qt.ArrowCursor))
                # self.unsetCursor()

    def leaveEvent(self, event):
        """鼠标离开界面区域"""
        self.on = False
        """
        if self.lineEdit_search.width() != 0:
            self.smoothSwitch2(True)
        """

    def mouseDoubleClickEvent(self, event):
        """双击全屏"""

        top = event.pos().x() in self._top_rect[0] and event.pos().y() in self._top_rect[1]
        if event.button() == Qt.LeftButton and top and not (self.isMaximized()):
            self.maxWindow()
        elif event.button() == Qt.LeftButton and top and self.isMaximized():
            self.showNormal()
            self.move(event.pos().x() - self.width() / 2, event.pos().y() - self.topBar.height() / 2 - 10)
            self.redraw()

    def _initDrag(self):
        """设置鼠标跟踪判断扳机默认值"""
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False
        self._left_drag = False

    def mouseMoveEvent(self, event):
        """鼠标移动事件"""
        right = event.pos().x() in self._right_rect[0] and event.pos().y() in self._right_rect[1]
        bottom = event.pos().x() in self._bottom_rect[0] and event.pos().y() in self._bottom_rect[1]
        corner = event.pos().x() in self._corner_rect[0] and event.pos().y() in self._corner_rect[1]
        top = event.pos().x() in self._top_rect[0] and event.pos().y() in self._top_rect[1]

        left = event.pos().x() in self._left_rect[0] and event.pos().y() in self._left_rect[1]

        if left or right:
            self.setCursor(Qt.SizeHorCursor)
        elif bottom:
            self.setCursor(Qt.SizeVerCursor)
        elif corner:
            self.setCursor(Qt.SizeFDiagCursor)

        # 当鼠标左键点击不放及满足点击区域的要求后，分别实现不同的窗口调整
        if Qt.LeftButton and self._right_drag:
            self.resize(event.pos().x(), self.height())
            event.accept()
        elif Qt.LeftButton and self._left_drag:
            self.resize((self.pos().x() + self.width()) - event.globalPos().x(), self.height())
            event.accept()
            self.move(event.globalPos().x(), self.pos().y())
        elif Qt.LeftButton and self._bottom_drag:
            self.resize(self.width(), event.pos().y())
            event.accept()
        elif Qt.LeftButton and self._corner_drag:
            self.resize(event.pos().x(), event.pos().y())
            event.accept()
        # elif Qt.LeftButton and self._move_drag and top:
        elif Qt.LeftButton and not (self.isMaximized()):
            # 标题栏拖放窗口位置
            self.move(event.globalPos() - self.move_DragPosition)
            self.redraw()
            event.accept()

        # 最大化窗口时按住恢复正常窗口大小，并可移动窗口
        elif Qt.LeftButton and self.isMaximized() and top:
            self.showNormal()
            # 移动窗口可拖动位置
            self.move(event.pos().x() - self.width() / 2, event.pos().y() - self.topBar.height() / 2 - 10)
            self.redraw()
            event.accept()
        # 更改位置
        self.redraw()
        event.accept()

    def mousePressEvent(self, event):
        """鼠标点击事件"""
        right = event.pos().x() in self._right_rect[0] and event.pos().y() in self._right_rect[1]
        bottom = event.pos().x() in self._bottom_rect[0] and event.pos().y() in self._bottom_rect[1]
        corner = event.pos().x() in self._corner_rect[0] and event.pos().y() in self._corner_rect[1]
        top = event.pos().x() in self._top_rect[0] and event.pos().y() in self._top_rect[1]

        left = event.pos().x() in self._left_rect[0] and event.pos().y() in self._left_rect[1]
        if (event.button() == Qt.LeftButton) and corner:
            self._corner_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and right:
            self._right_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and left:
            self._left_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and bottom:
            self._bottom_drag = True
            event.accept()

        elif (event.button() == Qt.LeftButton) and top:
            if not (self.isMaximized()):
                self._move_drag = True
                self.move_DragPosition = event.globalPos() - self.pos()
                # 更改为移动窗口指针
                self.topBar.setCursor(QCursor(Qt.OpenHandCursor))
                event.accept()

        # 关闭搜索框
        if self.lineEdit_search.width() != 0:
            self.smoothSwitch2(True)

    def mouseReleaseEvent(self, event):
        """鼠标释放"""
        # 鼠标释放后，各扳机复位
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False
        self.flag = False
        self._left_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
        self.topBar.unsetCursor()


if __name__ == '__main__':
    # 适配2k等高分辨率屏幕,低分辨率屏幕可以缺省
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    w = myWindow()
    # w.show()
    sys.exit(app.exec_())