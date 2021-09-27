import sys
import time
import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import QNetworkProxyFactory
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile

class myWindow(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("myWindow")
        self.setupUi()      # 初始化组件
        self.setWindow()    # 初始化窗口
        self.show()

    def setupUi(self):
        # 底板
        self.frame = QFrame(self)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(10, 0, 1000, 600))


        # 顶部菜单条
        self.topBar = QFrame(self.frame)
        self.topBar.setObjectName("topBar")
        self.topBar.setGeometry(QRect(10, 10, 980, 40))
        ## 回退
        self.btn_back = QPushButton(self.topBar)
        self.btn_back.setObjectName("btn_back")
        self.btn_back.setGeometry(QRect(10, 5, 30, 30))
        self.btn_back.setIcon(QIcon("back.png"))
        self.btn_back.setIconSize(QSize(30, 30))  # 设置图标大小
        self.btn_back.setToolTip("后退")

        ## 前进
        self.btn_goAhead = QPushButton(self.topBar)
        self.btn_goAhead.setObjectName("btn_goAhead")
        self.btn_goAhead.setGeometry(QRect(50, 5, 30, 30))
        self.btn_goAhead.setIcon(QIcon("go.png"))
        self.btn_goAhead.setIconSize(QSize(30, 30))
        self.btn_goAhead.setToolTip("前进")
        self.btn_goAhead.clicked.connect(lambda :self.goAhead(True))

        ## 刷新按钮
        self.btn_refresh = QPushButton(self.topBar)
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.setGeometry(QRect(110, 5, 30, 30))
        self.btn_refresh.setIcon(QIcon("refresh.png"))
        self.btn_refresh.setIconSize(QSize(20, 20))
        self.refresh_flag = True  #随时可刷新
        self.btn_refresh.clicked.connect(lambda: self.refreshPage(self.refresh_flag))
        self.btn_refresh.setToolTip("重新加载此页")

        ## 主页按钮
        self.btn_home= QPushButton(self.topBar)
        self.btn_home.setObjectName("btn_search")
        self.btn_home.setGeometry(QRect(QRect(150, 5, 30, 30)))
        self.btn_home.setIcon(QIcon("home.png"))
        self.btn_home.setIconSize(QSize(24, 24))
        self.btn_home.setToolTip("主页")
        self.btn_home.clicked.connect(lambda: self.loadWebPage(True, "https://cn.bing.com/"))

        ## 清除缓存
        self.btn_clearCache = QPushButton(self.topBar)
        self.btn_clearCache.setObjectName("btn_clearCache")
        self.btn_clearCache.setGeometry(QRect(self.topBar.width()-100, 5, 30, 30))
        self.btn_clearCache.setIcon(QIcon("clearCache.png"))
        self.btn_clearCache.setIconSize(QSize(20, 20))
        self.btn_clearCache.setToolTip("清除缓存")
        self.btn_clearCache.clicked.connect(self.clearCache)




        # 搜索图标label
        # self.lab_search = QLabel(self.topBar)
        # self.lab_search.setObjectName("lab_search")
        # self.lab_search.setGeometry(QRect(160, 10, 30, 30))
        # self.lab_search.setPixmap(QPixmap('search.png'))
        # self.lab_search.setScaledContents(True) ## 设置图片自适应label大小

        ## 搜索按钮
        self.btn_search = QPushButton(self.topBar)
        self.btn_search.setObjectName("btn_search")
        self.btn_search.setGeometry(QRect(190, 5, 30, 30))
        self.btn_search.setIcon(QIcon("search.png"))
        self.btn_search.setIconSize(QSize(24, 24))
        self.btn_search.setToolTip("搜索")
        self.search_flag = True
        self.btn_search.clicked.connect(lambda: self.smoothSwitch(self.search_flag))
        # 搜索框
        self.lineEdit_search = QLineEdit(self.topBar)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.lineEdit_search.setPlaceholderText("  please enter a url like:   www.baidu.com")
        self.lineEdit_search.hide()

    def goAhead(self, flag):
        if flag:
            url = self.urlList[-1]
            self.loadWebPage(flag, url)


    def clearCache(self):
        QWebEngineProfile.defaultProfile().cookieStore().deleteAllCookies() # 清空缓存
        print("清除缓存成功")
        self.refreshPage(True)
        print("缓存后刷新")


    def loadWebPage(self, enable, url="https://cn.bing.com/"):
        # 如果输入了网址则进去输入的网址

        input_url = self.lineEdit_search.text().strip().replace("https://", "").replace("http://", "")
        if input_url != "":
            try:
                if not input_url.startswith("https://"):
                    input_url = "https://" + input_url
            except:
                if not input_url.startswith("http://"):
                    input_url = "http://" + input_url
            finally:
                self.urlList.append(input_url)
                # url = input_url
                url = self.urlList[-1]
        """

        input_url = self.lineEdit_search.text().strip()
        if not (input_url.startswith("https://") or input_url.startswith("http://")):
            input_url = "https://" + input_url
        self.urlList.append(input_url)
        # url = input_url
        url = self.urlList[-1]
        """

        # 如果点击主页则清除已输入的网址
        btn = self.sender()
        if btn == self.btn_home:
            self.lineEdit_search.clear()
            url = "https://cn.bing.com/"
        if enable:
            print("正在加载页面")
            self.browser = QWebEngineView(self.frame)
            self.browser.setObjectName("brower")
            self.browser.setGeometry(10, 60, self.frame.width()-20, self.frame.height()-70)
            QNetworkProxyFactory.setUseSystemConfiguration(False)  # 取消代理，加快网页加载速度
            self.browser.load(QUrl(url))
            print(url)

            self.browser.show()











    # 点击刷新
    def refreshPage(self, enable):
        """
        刷新页面
        """
        try:
            if enable and self.lineEdit_search.width() != 0:
                # QApplication.processEvents()
                self.smoothSwitch2(True)
                self.refresh_flag = False  #点击刷新不再开启关闭搜索栏动画效果
                print("关闭搜索栏")
                print("搜索输入框已清除")
        finally:
            self.loadWebPage(True)
            print("refresh ...")


    # 点击搜索按钮弹出搜索输入框：平滑切换效果, 隐藏搜索按钮，显示搜索框
    def smoothSwitch(self, enable):
        if enable:
            # ANIMATION
            print("开启搜索栏")
            self.btn_search.hide()
            self.lineEdit_search.show()
            self.animation = QPropertyAnimation(self.lineEdit_search, b"geometry")  # 动画效果
            self.animation.setDuration(900)  # 设置动画运行时长0.9s
            self.animation.setStartValue(QRect(190, 5, 0, 30))
            self.animation.setEndValue(QRect(190, 5, 600, 30))
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
            self.refresh_flag = True  # 可点击刷新关闭搜索栏
        self.lineEdit_search.returnPressed.connect(lambda :self.loadWebPage(True))


    # 点击刷新关闭搜索栏
    def smoothSwitch2(self, enable):
        # ANIMATION
        self.btn_search.show()
        # self.lineEdit_search.hide()
        self.animation = QPropertyAnimation(self.lineEdit_search, b"geometry")  # 动画效果
        self.animation.setDuration(700)  # 设置动画运行时长0.5s
        self.animation.setStartValue(QRect(190, 5, 600, 30))
        self.animation.setEndValue(QRect(190, 5, 0, 30))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()


    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)  # 关闭默认工具栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明
        # CloseButton
        self.btn_close = QPushButton(self.topBar)
        self.btn_close.setObjectName("btn_close")
        self.btn_close.setGeometry(QRect(self.frame.width() - 60, 5, 30, 30))
        self.btn_close.setToolTip("关闭")
        self.btn_close.setIcon(QIcon("close.png"))
        self.btn_close.setIconSize(QSize(20, 20))
        self.btn_close.clicked.connect(QCoreApplication.instance().quit)  # 关闭


        self.flag = False  # 拖动按钮不会报错
        self.loadQss()     # 加载样式
        # 加载主页
        self.urlList = ["https://cn.bing.com/"]
        url = "https://cn.bing.com/"
        self.loadWebPage(True, url)

    def loadQss(self):
        with open("style.qss") as f:
            qss = f.read()
        self.setStyleSheet(qss)


    # --------------自定义窗口移动方法----------
    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.flag = True
            self.m_Position = QMouseEvent.globalPos() - self.pos()
            QMouseEvent.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseReleaseEvent(self, QMouseEvent):
        self.flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()



    def keyPressEvent(self, e):
        # 按“Esc”键退出程序！
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = myWindow()
    sys.exit(app.exec_())