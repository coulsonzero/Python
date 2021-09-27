import sys
from threading import Thread
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Demo.ProcessBar.Demo6.ClientDemo6 import *


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

        self.btn_selectFile = QPushButton(self.frame)
        self.btn_selectFile.setObjectName("btn_selectFile")
        self.btn_selectFile.setGeometry(QRect(50, 130, 60, 21))
        self.btn_selectFile.setText("选择文件")
        self.btn_selectFile.clicked.connect(self.selectFile)

        self.fpEdit = QLineEdit(self.frame)  # 单行文本框
        self.fpEdit.setGeometry(QRect(130, 130, 150, 21))

        self.btn_sendFile = QPushButton(self.frame)
        self.btn_sendFile.setObjectName("btn_sendFile")
        self.btn_sendFile.setGeometry(QRect(300, 130, 60, 21))
        self.btn_sendFile.setText("上传文件")
        self.btn_sendFile.clicked.connect(self.sendFile)
        # self.btn_sendFile.clicked.connect(self.test)
    """
    def test(self):
        client = socket.socket()
        client.connect(('127.0.0.1', 8000))
        while True:
            file_path = self.fpEdit.text()  # input('请输入要上传文件的绝对路径：')
            print(file_path)
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            dic = {"option": "1", "name": file_name, "file_size": file_size}
            client.send(json.dumps(dic).encode())
            msg = client.recv(100)  # 判断服务端准备好接收文件了，还可以防止粘包
            begin_size = file_size
            if msg.decode() == 'ok':
                # 服务端表示准备好接收文件了，开始循环发送文件
                with open(file_path, 'rb') as f:
                    while file_size:
                        content = f.read(1024)
                        client.send(content)
                        file_size -= len(content)
                        print_bar1(round((begin_size - file_size) / begin_size, 2))
                    print('')
                break
        client.close()
    
    def print_bar1(self, percent):
        bar = '\r' + '*' * int((percent * 100)) + ' %3.0f%%|' % (percent * 100) + '100%'
        print(bar, end='', flush=True)
    """
    def selectFile(self):
        get_filename_path, ok = QFileDialog.getOpenFileName(self, "选取文件", "C:/",
                                                            "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
        if ok:
            QMessageBox.question(self, "文件选择确认框", "是否确认选择此文件?\n" + get_filename_path,
                                 QMessageBox.Yes | QMessageBox.No)
            self.fpEdit.setText(str(get_filename_path))

    def sendFile(self):
        self.my_thread = Thread(target=main, args=(self.fpEdit,))
        self.my_thread.start()

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
        self.btn_max.clicked.connect(self.maxWindow)  # 最大化
        self.btn_min.clicked.connect(self.showMinimized)  # 最小化

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
            self.setGeometry(0, 0, self.width, self.height)
            self.frame.setGeometry(0, 0, self.width, self.height)
            self.btn_close.setGeometry(QRect(self.frame.width() - 30, 10, 21, 21))
            self.btn_max.setGeometry(QRect(self.frame.width() - 60, 10, 21, 21))
            self.btn_min.setGeometry(QRect(self.frame.width() - 90, 10, 21, 21))

    def loadQss(self):
        with open("style.qss") as f:
            qss = f.read()
        self.setStyleSheet(qss)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mb = myWindow()
    sys.exit(app.exec_())
