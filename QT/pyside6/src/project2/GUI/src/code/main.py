"""
@author: coulson
@version: 2021/7/29  11:51
"""
import sys
from PyQt5.Qt import *
from PyQt5.uic import loadUi
from icecream import ic


class Window(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('../ui/mainWindow.ui', self)
        self.setUI()  # 调用ui界面
        self._initWindow()         # 主窗口初始化设置


    def _initWindow(self):
        #----------- 隐藏外窗口 -----------
        self.setWindowFlags(Qt.FramelessWindowHint)     #关闭默认工具栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明
        #-----------加载qss样式-------------
        self.__my_qss()
        #----------- 关闭 -----------------
        self.btn_close.clicked.connect(QCoreApplication.instance().quit)
        #----------- 最小化 ---------------
        self.btn_min.clicked.connect(self.showMinimized)


    def __my_qss(self):
        with open("../resourse/app.qss") as f:
            qss = f.read()
        self.setStyleSheet(qss)


    #--------------自定义窗口移动方法----------
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
        """
        去掉此方法，则无法拖动
        """
        if Qt.LeftButton and self.flag:
            # 更改窗口位置
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        """
        设置后只能在顶部空白处才能拖动，组件位置不可拖动
        """
        self.flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


    # 点击退出提示框
    def closeEvent(self, e):
        reply = QMessageBox.question(self, 'Message', "是否确认退出?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()


    # 按“Esc”键退出程序！
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    ##############################################
    ##############################################
    def setUI(self):
        self.btn_queue.clicked.connect(self.btnClick)
        self.btn_run.clicked.connect(self.btnClick)
        self.btn_upload.clicked.connect(self.btnClick)
        self.btn_fail.clicked.connect(self.btnClick)
        self.btn_addfile.clicked.connect(self.btnClick)

    def btnClick(self):
        send = self.sender()
        btnName = send.objectName()
        ic(btnName)

        if btnName == "btn_queue":
            self.queue()
        if btnName == "btn_run":
            self.run()
        if btnName == "btn_upload":
            self.upload()
        if btnName == "btn_fail":
            self.fail()
        if btnName == "btn_addfile":
            self.addFile()


    def queue(self):
        pass
    def run(self):
        pass
    def upload(self):
        pass
    def fail(self):
        pass
    def addFile(self):
        get_filename_path, ok = QFileDialog.getOpenFileName(self, "选取文件", "C:/")  # 设置文件扩展名过滤,注意用双分号间隔 "All Files (*);;Text Files (*.txt)"
        if ok:
            QMessageBox.question(self, "文件选择确认框", "是否确认选择此文件?\n"+get_filename_path, QMessageBox.Yes | QMessageBox.No)
            self.textEdit.setText(f'您已选取: "{get_filename_path}"')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
