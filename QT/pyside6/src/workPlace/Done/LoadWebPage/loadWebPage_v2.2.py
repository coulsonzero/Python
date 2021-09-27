"""
@author: coulson
@version: 2021/8/16  19:09
"""
import sys
import time
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QRect, QSize, QCoreApplication, QUrl, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtNetwork import QNetworkProxyFactory
# from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5.QtWidgets import QFrame, QPushButton, QLineEdit, QVBoxLayout, QApplication, QMainWindow, QWidget


class webview_main(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setObjectName("myWindow")
        self.resize(1200, 800)
        self.setMinimumSize(400, 100)
        self.setupUi()  # 初始化组件
        self.setWindow()  # 初始化窗口
        self.show()

    def setWindow(self):
        """
        界面初始化
        """

        # 隐藏设置系统窗口
        self.setWindowFlags(Qt.FramelessWindowHint)  # 关闭默认工具栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明

        # MinButton
        self.btn_min = QPushButton(self.topBar)
        self.btn_min.setObjectName("btn_min")
        self.btn_min.setGeometry(QRect(self.frame.width() - 150, 5, 30, 30))
        self.btn_min.setToolTip("最小化")
        self.btn_min.setIcon(QIcon("C:/TGYC2/src/Photos/webviewer/min.png"))
        self.btn_min.setIconSize(QSize(20, 20))
        self.btn_min.clicked.connect(self.minWindow)  # 最小化

        # MaxButton
        self.btn_max = QPushButton(self.topBar)
        self.btn_max.setObjectName("btn_max")
        self.btn_max.setGeometry(QRect(self.frame.width() - 110, 5, 30, 30))
        self.btn_max.setToolTip("最大化")
        self.btn_max.setIcon(QIcon("C:/TGYC2/src/Photos/webviewer/max.png"))
        self.btn_max.setIconSize(QSize(20, 20))
        self.btn_max.clicked.connect(self.maxWindow)  # 最大化

        # CloseButton
        self.btn_close = QPushButton(self.topBar)
        self.btn_close.setObjectName("C:/TGYC2/src/Photos/webviewer/btn_close")
        self.btn_close.setGeometry(QRect(self.frame.width() - 70, 5, 30, 30))
        self.btn_close.setToolTip("关闭")
        self.btn_close.setIcon(QIcon("C:/TGYC2/src/Photos/webviewer/close.png"))
        self.btn_close.setIconSize(QSize(20, 20))
        self.btn_close.clicked.connect(QCoreApplication.instance().quit)  # 关闭

        self.flag = False  # 拖动按钮不会报错
        # 鼠标移动初始化
        self.on = False
        self._initDrag()  # 设置鼠标跟踪判断扳机默认值
        self.setMouseTracking(True)  # 设置widget鼠标跟踪

        self.loadQss()  # 加载样式
        # 加载主页
        self.home_url = "https://cn.bing.com/"
        self.loadWebPage(True, self.home_url)

    def mouseDoubleClickEvent(self, event):  # 双击
        if event.button() == Qt.LeftButton and event.pos().x() in self._top_rect[0] and event.pos().y() in self._top_rect[1]:
            self.maxWindow()


    def minWindow(self):
        try:
            self.showMinimized()
        except:
            time.sleep(500)
            print("error")
            self.refreshPage(True)
            time.sleep(1)
            self.showMinimized()

    def maxWindow(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
        self.redraw()
        self.btn_search.show()


    def loadQss(self):
        '''
        with open("style.qss") as f:
            qss = f.read()
        self.setStyleSheet(qss)
        '''

        self.setStyleSheet(
 '''
 * {
    margin: 0;
    padding: 0;
}


#frame {
    /*background-color: mintcream;*/
    background-color: rgb(200, 200, 200);
    border-radius: 15px;
}


#topBar {
    background-color: #323232;
	border-radius: 15px;
}

QPushButton{
    border-radius: 15px;
}

QPushButton:hover {
    background-color: rgb(170, 170, 127);
    border: solid 5px rgb(0, 255, 255);
    background-color: qlineargradient(spread:pad,x1:1,y1:0,x2:0,y2:1,stop:0 lightCyan,stop:0.5  SkyBlue ,  stop:1 deepSkyBlue);
    border-radius: 15px;
}

QPushButton:pressed{
    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,
                      stop:0 pink,
                      /*stop:0.5 rgb(191, 101, 24),*/
                      stop:0.5  SkyBlue ,
                      stop:1 yellow
                      /*stop:0 rgb(255, 0, 255),*/
                      /*stop:0.5  SkyBlue ,*/
                      /*stop:1 rgb(85, 255, 127)*/
    );
}


/*#lineEdit_search {*/
/*    border-radius: 12%;*/
/*    background-color: antiquewhite;*/
/*    border 1px solid lightskyblue;*/
/*    color: black;*/
/*    font-family: "JetBrains Mono";*/
/*    font-size: 15px;*/
/*}*/

QLineEdit {
	background-color: antiquewhite;
	border-radius: 15%;
	/*border: 0 solid rgb(91, 101, 124);*/
    border: none;
	padding-left: 13px;
    /*font-family: "JetBrains Mono";*/
    font-size: 11pt;
    font-family: "Segoe UI";
	selection-color: rgb(255, 255, 255);
	selection-background-color: rgb(255, 121, 198);
}
QLineEdit:hover {
	border: 1px solid #323232;
}
QLineEdit:focus {
	border: 1px solid rgb(91, 101, 124);
}




 '''
        )



    def setupUi(self):
        # 底板
        self.frame = QFrame(self)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(0, 0, 1200, 800))

        # 顶部菜单条
        self.topBar = QFrame(self.frame)
        self.topBar.setObjectName("topBar")
        # self.topBar.setGeometry(QRect(10, 10, 980, 40))
        self.topBar.setGeometry(QRect(0, 0, 980, 40))
        self.topBar.setFixedHeight(40)


        # 浏览器
        self.browser = QWebEngineView(self.frame)
        self.browser.setObjectName("browser")
        self.browser.setGeometry(10, 60, self.frame.width() - 20, self.frame.height() - 70)
        QNetworkProxyFactory.setUseSystemConfiguration(False)  # 取消代理，加快网页加载速度

        ## 回退
        self.btn_back = QPushButton(self.topBar)
        self.btn_back.setObjectName("btn_back")
        self.btn_back.setGeometry(QRect(10, 5, 30, 30))
        self.btn_back.setIcon(QIcon("C:/TGYC2/src/Photos/webviewer/back.png"))
        self.btn_back.setIconSize(QSize(30, 30))  # 设置图标大小
        self.btn_back.setToolTip("后退")
        self.btn_back.clicked.connect(self.browser.back)
        ## 前进
        self.btn_goAhead = QPushButton(self.topBar)
        self.btn_goAhead.setObjectName("btn_goAhead")
        self.btn_goAhead.setGeometry(QRect(50, 5, 30, 30))
        self.btn_goAhead.setIcon(QIcon("C:/TGYC2/src/Photos/webviewer/go.png"))
        self.btn_goAhead.setIconSize(QSize(30, 30))
        self.btn_goAhead.setToolTip("前进")
        self.btn_goAhead.clicked.connect(self.browser.forward)

        ## 刷新按钮
        self.btn_refresh = QPushButton(self.topBar)
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.setGeometry(QRect(110, 5, 30, 30))
        self.btn_refresh.setIcon(QIcon("C:/TGYC2/src/Photos/webviewer/refresh.png"))
        self.btn_refresh.setIconSize(QSize(20, 20))
        self.refresh_flag = True  # 随时可刷新
        self.btn_refresh.clicked.connect(lambda: self.refreshPage(self.refresh_flag))
        # self.btn_refresh.clicked.connect(self.browser.reload)
        self.btn_refresh.setToolTip("重新加载此页")

        ## 主页按钮
        self.btn_home = QPushButton(self.topBar)
        self.btn_home.setObjectName("btn_search")
        self.btn_home.setGeometry(QRect(QRect(150, 5, 30, 30)))
        self.btn_home.setIcon(QIcon("C:/TGYC2/src/Photos/webviewer/home.png"))
        self.btn_home.setIconSize(QSize(24, 24))
        self.btn_home.setToolTip("主页")
        self.btn_home.clicked.connect(lambda: self.loadWebPage(True, "https://cn.bing.com/"))

        ## 清除缓存
        self.btn_clearCache = QPushButton(self.topBar)
        self.btn_clearCache.setObjectName("btn_clearCache")
        self.btn_clearCache.setGeometry(QRect(self.frame.width() - 210, 5, 30, 30))
        self.btn_clearCache.setIcon(QIcon("C:/TGYC2/src/Photos/webviewer/clearCache.png"))
        self.btn_clearCache.setIconSize(QSize(20, 20))
        self.btn_clearCache.setToolTip("清除缓存")
        self.btn_clearCache.clicked.connect(self.clearCache)


        ## 搜索按钮
        self.btn_search = QPushButton(self.topBar)
        self.btn_search.setObjectName("btn_search")
        self.btn_search.setGeometry(QRect(190, 5, 30, 30))
        self.btn_search.setIcon(QIcon("C:/TGYC2/src/Photos/webviewer/search.png"))
        self.btn_search.setIconSize(QSize(24, 24))
        self.btn_search.setToolTip("搜索")
        self.search_flag = True
        self.btn_search.clicked.connect(lambda: self.smoothSwitch(self.search_flag))
        # 搜索框
        self.lineEdit_search = QLineEdit(self.topBar)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.lineEdit_search.setPlaceholderText("  please enter a url like:   www.baidu.com")
        self.lineEdit_search.hide()

        # 界面布局
        self.vBox2 = QVBoxLayout(self.frame)
        self.vBox2.addWidget(self.topBar)
        self.vBox2.addWidget(self.browser)

        self.vBox = QVBoxLayout(self)
        self.vBox.addWidget(self.frame)
        self.setLayout(self.vBox)

    def redraw(self):
        """
        窗口大小变化时，topBar内的按钮位置重置
        """
        # self.frame.resize()
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


    def _initDrag(self):
        # 设置鼠标跟踪判断扳机默认值
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False

    def resizeEvent(self, event):

        self._right_rect = [list(range(self.frame.width() - 15, self.frame.width() + 15)),
                            list(range(self.frame.y() + 20, self.frame.height() - 30))]
        self._bottom_rect = [list(range(self.x() + 20, self.width() - 20)),
                             list(range(self.height()-10, self.height() + 10))]
        self._corner_rect = [list(range(self.frame.width() - 15, self.frame.width() + 20)),
                             list(range(self.frame.height() - 15, self.frame.height() + 15))]
        self._top_rect = [list(range(self.frame.x()+20, self.frame.width() - 20)),
                          list(range(self.frame.y(), self.frame.y() + 50))]



    def enterEvent(self, event):
        """
        鼠标进入界面边界，鼠标指针随之修改
        """
        self.on = True
        if self.on:
            # 右指针
            if event.pos().x() in self._right_rect[0] and event.pos().y() in self._right_rect[1]:
                self.setCursor(Qt.SizeHorCursor)
            # 下指针
            elif event.pos().x() in self._bottom_rect[0] and event.pos().y() in self._bottom_rect[1]:
                self.setCursor(Qt.SizeVerCursor)
            # 右下角指针
            elif event.pos().x() in self._corner_rect[0] and event.pos().y() in self._corner_rect[1]:
                self.setCursor(Qt.SizeFDiagCursor)
            # top
            elif event.pos().x() in self._top_rect[0] and event.pos().y() in self._top_rect[1]:
                self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改为移动窗口指针
            else:
                self.setCursor(QCursor(Qt.ArrowCursor))     # 常规指针


    def leaveEvent(self, event):
        self.on = False
        # 鼠标离开界面区域，就启动关闭搜索框动画

        if self.lineEdit_search.width() != 0:
            self.smoothSwitch2(True)




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
            self.move(QMouseEvent.globalPos() - self.move_DragPosition)
            QMouseEvent.accept()
        # 更改位置
        self.redraw()

    def mousePressEvent(self, event):
        try:
            # 重写鼠标点击的事件
            if (event.button() == Qt.LeftButton) and (
                    event.pos().x() in self._corner_rect[0] and event.pos().y() in self._corner_rect[1]):
                # 鼠标左键点击右下角边界区域
                self._corner_drag = True
                event.accept()
            elif (event.button() == Qt.LeftButton) and (
                    event.pos().x() in self._right_rect[0] and event.pos().y() in self._right_rect[1]):
                # 鼠标左键点击右侧边界区域
                self._right_drag = True
                event.accept()
            elif (event.button() == Qt.LeftButton) and (
                    event.pos().x() in self._bottom_rect[0] and event.pos().y() in self._bottom_rect[1]):
                # 鼠标左键点击下侧边界区域
                self._bottom_drag = True
                event.accept()
            elif (event.button() == Qt.LeftButton) and (event.y() < self.frame.height()):
                # 鼠标左键点击标题栏区域
                self._move_drag = True
                self.move_DragPosition = event.globalPos() - self.pos()
                event.accept()
            # 顶部移动
            if event.pos().x() in self._top_rect[0] and event.pos().y() in self._top_rect[1]:
                self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改为移动窗口指针

            if self.lineEdit_search.width() != 0:
                self.smoothSwitch2(True)  # 关闭搜索框

            # 移动窗口时，按钮位置随之变化
            self.redraw()
        except:
            print("error")
            self.refreshPage(True)


    def mouseReleaseEvent(self, QMouseEvent):
        # 鼠标释放后，各扳机复位
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False
        self.flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))



    def loadWebPage(self, enable, url="https://cn.bing.com/"):
        # 输入网址
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
            self.browser.urlChanged.connect(lambda: self.lineEdit_search.setText(self.browser.url().toDisplayString()))  # 获取当前网页网址，并显示到导航栏上

    def refreshPage(self, enable):
        # 刷新页面
        if enable and self.lineEdit_search.width() != 0:
            # QApplication.processEvents()
            self.smoothSwitch2(True)  # 关闭搜索框
            self.refresh_flag = False  # 点击刷新不再重复关闭搜索栏动画效果
        # self.loadWebPage(True)
        self.browser.reload()  # 刷新重载网页
        print("refresh ...")

    def clearCache(self):
        QWebEngineProfile.defaultProfile().cookieStore().deleteAllCookies()  # 清空缓存
        self.refreshPage(True)
        print("清除缓存中...")

    # 点击搜索按钮弹出搜索输入框：平滑切换效果, 隐藏搜索按钮，显示搜索框
    def smoothSwitch(self, enable):
        if enable:
            # ANIMATION
            print("开启搜索栏")
            # self.btn_search.hide()
            self.lineEdit_search.show()
            self.animation = QPropertyAnimation(self.lineEdit_search, b"geometry")  # 动画效果
            self.animation.setDuration(900)  # 设置动画运行时长0.9s
            self.animation.setStartValue(QRect(190, 5, 0, 30))
            self.animation.setEndValue(QRect(190, 5, self.frame.width() - 440, 30))
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
        self.refresh_flag = True  # 可点击刷新关闭搜索栏
        self.lineEdit_search.returnPressed.connect(lambda: self.loadWebPage(True))

    # 点击刷新关闭搜索栏
    def smoothSwitch2(self, enable):

        self.animation = QPropertyAnimation(self.lineEdit_search, b"geometry")  # 动画效果设置
        self.animation.setDuration(500)                                         # 设置动画运行时长
        self.animation.setStartValue(QRect(190, 5, self.frame.width() - 440, 30))
        self.animation.setEndValue(QRect(190, 5, 0, 30))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

        self.btn_search.show()

    def keyPressEvent(self, e):
        # 按“Esc”键退出程序！
        if e.key() == Qt.Key_Escape:
            self.close()

    """
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
    """


if __name__ == '__main__':
    # 适配2k等高分辨率屏幕,低分辨率屏幕可以缺省
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    w = webview_main()
    sys.exit(app.exec_())