import sys
import time
import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import QNetworkProxyFactory
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from myQLabel import myQLabel
from icecream import ic

class myWindow(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("myWindow")
        self.setGeometry(QRect(100, 200, 1010, 600))
        self.setMinimumSize(100, 100)
        self.setupUi()  # 初始化组件
        self.setWindow()  # 初始化窗口
        """
        self._initDrag()  # 设置鼠标跟踪判断扳机默认值
        self.setMouseTracking(True)  # 设置widget鼠标跟踪
        """

        self.show()




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

        self.on = False
        # 加载主页
        home_url = "https://cn.bing.com/"
        self.loadWebPage(True, home_url)

    def loadQss(self):
        with open("style.qss") as f:
            qss = f.read()
        self.setStyleSheet(qss)

    def setupUi(self):
        # 底板
        self.frame = QFrame(self)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(10, 0, 1000, 600))


        # 顶部菜单条
        self.topBar = QFrame(self.frame)
        self.topBar.setObjectName("topBar")
        self.topBar.setGeometry(QRect(10, 10, 980, 40))

        # 浏览器
        self.browser = QWebEngineView(self.frame)
        self.browser.setObjectName("browser")
        self.browser.setGeometry(10, 60, self.frame.width() - 20, self.frame.height() - 70)
        QNetworkProxyFactory.setUseSystemConfiguration(False)  # 取消代理，加快网页加载速度

        ## 回退
        self.btn_back = QPushButton(self.topBar)
        self.btn_back.setObjectName("btn_back")
        self.btn_back.setGeometry(QRect(10, 5, 30, 30))
        self.btn_back.setIcon(QIcon("back.png"))
        self.btn_back.setIconSize(QSize(30, 30))  # 设置图标大小
        self.btn_back.setToolTip("后退")
        self.btn_back.clicked.connect(self.browser.back)
        ## 前进
        self.btn_goAhead = QPushButton(self.topBar)
        self.btn_goAhead.setObjectName("btn_goAhead")
        self.btn_goAhead.setGeometry(QRect(50, 5, 30, 30))
        self.btn_goAhead.setIcon(QIcon("go.png"))
        self.btn_goAhead.setIconSize(QSize(30, 30))
        self.btn_goAhead.setToolTip("前进")
        self.btn_goAhead.clicked.connect(self.browser.forward)

        ## 刷新按钮
        self.btn_refresh = QPushButton(self.topBar)
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.setGeometry(QRect(110, 5, 30, 30))
        self.btn_refresh.setIcon(QIcon("refresh.png"))
        self.btn_refresh.setIconSize(QSize(20, 20))
        self.refresh_flag = True  #随时可刷新
        self.btn_refresh.clicked.connect(lambda: self.refreshPage(self.refresh_flag))
        # self.btn_refresh.clicked.connect(self.browser.reload)
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

    """
    def _initDrag(self):
        # 设置鼠标跟踪判断扳机默认值
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False


    def resizeEvent(self, event):
        self._right_rect = [list(range(self.frame.width() - 10, self.frame.width() + 10)), list(range(self.frame.y()+20, self.frame.height()-30))]
        self._bottom_rect = [list(range(self.frame.x()+20, self.frame.width()-20)), list(range(self.frame.height() - 10, self.frame.height() + 10))]
        self._corner_rect = [list(range(self.frame.width()-15, self.frame.width()+15)), list(range(self.frame.height()-15, self.frame.height()+15))]

    def enterEvent(self, event):
        # if QMouseEvent.pos() in [self._corner_rect, self._bottom_rect, self._right_rect]:
        self.on = True
        # ic(self.on)
        if self.on:
            # print(event.pos())
            # ic(event.pos().x(), event.pos().y())
            # ic(range(self.frame.width() - 15, self.frame.width() + 15))
            # ic(range(self.frame.y()+20, self.frame.height()-20))
            # ic(event.pos().x() in self._right_rect[0])
            # ic(event.pos().y() in self._right_rect[1])
            # 右指针
            if event.pos().x() in self._right_rect[0] and event.pos().y() in self._right_rect[1]:
                self.setCursor(Qt.SizeHorCursor)
            # 下指针
            elif event.pos().x() in self._bottom_rect[0] and event.pos().y() in self._bottom_rect[1]:
                self.setCursor(Qt.SizeVerCursor)
            # 右下角指针
            elif event.pos().x() in self._corner_rect[0] and event.pos().y() in self._corner_rect[1]:
                self.setCursor(Qt.SizeFDiagCursor)


    def leaveEvent(self, event):
        # if QMouseEvent.pos() not in [self._corner_rect, self._bottom_rect, self._right_rect]:
        self.on = False
        # print(self.on)


    def mouseMoveEvent(self, QMouseEvent):
        # 右指针
        if QMouseEvent.pos().x() in self._right_rect[0] and QMouseEvent.pos().y() in self._right_rect[1]:
            self.setCursor(Qt.SizeHorCursor)
        # 下指针
        elif QMouseEvent.pos().x() in self._bottom_rect[0] and QMouseEvent.pos().y() in self._bottom_rect[1]:
            self.setCursor(Qt.SizeVerCursor)
        # 右下角指针
        elif QMouseEvent.pos().x() in self._corner_rect[0] and QMouseEvent.pos().y() in self._corner_rect[1]:
            self.setCursor(Qt.SizeFDiagCursor)
    
        # 当鼠标左键点击不放及满足点击区域的要求后，分别实现不同的窗口调整
        # 没有定义左方和上方相关的5个方向，主要是因为实现起来不难，但是效果很差，拖放的时候窗口闪烁，再研究研究是否有更好的实现
        if Qt.LeftButton and self._right_drag:
            # 右侧调整窗口宽度
            self.resize(QMouseEvent.pos().x(), self.height())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._bottom_drag:
            # 下侧调整窗口高度
            self.resize(self.width(), QMouseEvent.pos().y())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._corner_drag:
            #  由于我窗口设置了圆角,这个调整大小相当于没有用了
            # 右下角同时调整高度和宽度
            self.resize(QMouseEvent.pos().x(), QMouseEvent.pos().y())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._move_drag:
            # 标题栏拖放窗口位置
            self.frame.move(QMouseEvent.globalPos() - self.move_DragPosition)
            QMouseEvent.accept()



    def mousePressEvent(self, event):
        # 重写鼠标点击的事件
        if (event.button() == Qt.LeftButton) and (event.pos().x() in self._corner_rect[0] and event.pos().y() in self._corner_rect[1]):
            # 鼠标左键点击右下角边界区域
            self._corner_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos().x() in self._right_rect[0] and event.pos().y() in self._right_rect[1]):
            # 鼠标左键点击右侧边界区域
            self._right_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos().x() in self._bottom_rect[0] and event.pos().y() in self._bottom_rect[1]):
            # 鼠标左键点击下侧边界区域
            self._bottom_drag = True
            event.accept()
        # elif (event.button() == Qt.LeftButton) and (event.y() < self.frame.height()):
        #     # 鼠标左键点击标题栏区域
        #     self._move_drag = True
        #     self.move_DragPosition = event.globalPos() - self.pos()
        #     event.accept()




    def mouseReleaseEvent(self, QMouseEvent):
        # 鼠标释放后，各扳机复位
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False
    """








    def loadWebPage(self, enable, url="https://cn.bing.com/"):
        # 输入网址
        input_url = self.lineEdit_search.text().strip()
        if input_url != "":
            if not(input_url.startswith("https://") or input_url.startswith("http://")):
                input_url = "https://" + input_url
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
            self.browser.urlChanged.connect(lambda: self.lineEdit_search.setText(self.browser.url().toDisplayString()))  # 获取当前网页网址，并显示到导航栏上






    def refreshPage(self, enable):
        # 刷新页面
        if enable and self.lineEdit_search.width() != 0:
            # QApplication.processEvents()
            self.smoothSwitch2(True)   # 关闭搜索框
            self.refresh_flag = False  # 点击刷新不再重复关闭搜索栏动画效果
        # self.loadWebPage(True)
        self.browser.reload() # 刷新重载网页
        print("refresh ...")

    def clearCache(self):
        QWebEngineProfile.defaultProfile().cookieStore().deleteAllCookies() # 清空缓存
        self.refreshPage(True)
        print("清除缓存中...")

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

    def keyPressEvent(self, e):
        # 按“Esc”键退出程序！
        if e.key() == Qt.Key_Escape:
            self.close()



    # --------------自定义窗口移动方法----------
    def mousePressEvent(self, QMouseEvent):
        # 鼠标左键
        if QMouseEvent.button() == Qt.LeftButton:
            self.flag = True
            self.m_Position = QMouseEvent.globalPos() - self.pos()
            QMouseEvent.accept()                       # 启动移动窗口函数
            self.setCursor(QCursor(Qt.OpenHandCursor)) # 更改为移动窗口指针
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()
    def mouseReleaseEvent(self, QMouseEvent):
        self.flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))






if __name__ == '__main__':
    # 适配2k等高分辨率屏幕,低分辨率屏幕可以缺省
    # QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    w = myWindow()

    sys.exit(app.exec_())