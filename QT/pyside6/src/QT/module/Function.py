"""
@author: coulson
@version: 2021/8/9  10:37
"""
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from custom_grips import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('../ui/mainWindow.ui', self)
        self.setUI()
        self.setWindow()
        self.loadQss()

    def setUI(self):
        pass

    def setWindow(self):
        # ----------- 隐藏外窗口 -----------
        self.setWindowFlags(Qt.FramelessWindowHint)  # 关闭默认工具栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明

        # 自定义窗口按钮
        self.btn_close.clicked.connect(QCoreApplication.instance().quit)  # 关闭
        self.btn_min.clicked.connect(self.showMinimized)  # 最小化
        self.btn_max.clicked.connect(self.btnClick)  # 最大化

        self.flag = False  # 拖动按钮不会报错
        self.loadQss()  # 加载样式

    def loadQss(self):
        """
        加载css样式
        """
        with open("../resourse/style.qss") as f:
            qss = f.read()
        self.setStyleSheet(qss)

    def loadWebPage(self, enable):
        ##### 调用搜索引擎
        if enable:
            self.browser = QWebEngineView(self.frame)
            self.browser.setObjectName("brower")
            self.browser.setGeometry(10, 60, self.frame.width()-20, self.frame.height()-70)

            # get_url = self.lineEdit_search.text()
            # self.browser.load(QUrl(get_url))
            QNetworkProxyFactory.setUseSystemConfiguration(False);  # 取消代理，加快网页加载速度

            self.url = "https://cn.bing.com/"
            self.browser.load(QUrl(self.url))
            self.browser.show()


    def btnClick(self):
        """
        最大化按钮
        """
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_MaxShow":
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()

    def buttonClick(self):
        """
        QStackedWidget分窗显示，点击按钮切换分页
        """
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)  # 切换分页

        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)

        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page)

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    def btnClick(self):
        btn = self.sender()
        if btn == self.btn_addFile:
            pass

    def addFile(self):
        """
        文件选择框
        """
        self.fileDialog = QFileDialog(self)
        self.fileDialog.setObjectName("fileDialog")
        self.fileDialog.setGeometry(500, 300, 275, 250)
        self.filePath, ok = self.fileDialog.getOpenFileName(self, "选取文件",
                                                            "C:/")  # 设置文件扩展名过滤,注意用双分号间隔 "All Files (*);;Text Files (*.txt)"
        if ok:
            # QMessageBox.question(self, "文件选择确认框", "是否确认选择此文件?\n"+self.filePath, QMessageBox.Yes | QMessageBox.No)
            self.textEdit.setText(f'您已选取: "{self.filePath}"')

    def saveImage(self):  # 保存图片到本地
        screen = QApplication.primaryScreen()
        pix = screen.grabWindow(self.label_image.winId())
        fd, type = QFileDialog.getSaveFileName(self.centralwidget, "保存图片", "", "*.jpg;;*.png;;All Files(*)")
        pix.save(fd)

    def openDirectory(self):  # 打开文件夹（目录）
        fd = QFileDialog.getExistingDirectory(self.centralwidget, "选择文件夹", "")
        self.label_directoryPath.setText(fd)

    def openTextFile(self):  # 选择文本文件上传
        fd, fp = QFileDialog.getOpenFileName(self.centralwidget, "选择文件", "", "*.txt;;All Files(*)")
        f = open(fd, 'r')
        self.label_txt.setText(f.read())
        self.label_filePath.setText(fd)
        f.close()

    def saveTextFile(self):  # 保存文本文件
        fd, fp = QFileDialog.getSaveFileName(self.centralwidget, "保存文件", "", "*.txt;;All Files(*)")
        f = open(fd, 'w')
        f.write(self.label_txt.text())
        f.close()

    # --------------自定义窗口移动方法----------
    self.flag = False
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

    def closeEvent(self, e):
        # 点击退出提示框
        reply = QMessageBox.question(self, 'Message', "是否确认退出?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()

    def keyPressEvent(self, e):
        # 按“Esc”键退出程序！
        if e.key() == Qt.Key_Escape:
            self.close()

    def loadBrower(self):
        """
        查看浏览器页面
        """
        ##### 调用搜索引擎
        self.browser = QWebEngineView(self.frame)
        self.browser.setObjectName("brower")

        self.browser.setGeometry(10, 70, self.frame.width() - 20, self.frame.height() - 90)
        self.browser.setStyleSheet(
            """
            QWebEngineView{border-radius: 10px}

            """
        )
        self.url = "https://cn.bing.com/"
        self.browser.load(QUrl(self.url))

        self.browser.show()

        # self.webViewFrame.browser.load(QUrl('http://task.tgyc.com/#/taskFeekback'))

    def resize(self):
        self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
        self.right_grip = CustomGrip(self, Qt.RightEdge, True)
        self.top_grip = CustomGrip(self, Qt.TopEdge, True)
        self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)
        if True:
            self.left_grip.setGeometry(0, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
            self.top_grip.setGeometry(0, 0, self.width(), 10)
            self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    def regularRefreshPage(self):
        """
        定时执行刷新界面
        :return:
        """
        self.timer = QTimer()
        self.timer.start(60)
        self.timer.timeout.connect(self.refreshPage)

    def refreshPage(self):
        """
        刷新页面
        :return:
        """
        QApplication.processEvents()

    def setGradientColor(self):
        """
        background - color: qlineargradient(spread:pad, x1: 1, y1: 0, x2: 0, y2: 1, stop: 0 lightCyan, stop: 0.5 skyBlue, stop: 1 deepSkyBlue);
        """
        pass