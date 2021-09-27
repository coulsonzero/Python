"""
@author: coulson
@version: 2021/7/29  11:51
"""

import sys
import time, traceback, os, json

from PyQt5.QtCore import QFileInfo
from PyQt5.Qt import *
from PyQt5.uic import loadUi
from PySide6.QtUiTools import QUiLoader
from icecream import ic




class Login(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('../ui/login.ui', self)
        self.setUI()                        # 调用ui界面
    def setUI(self):
        self.setFixedSize(self.width(), self.height())



class Window(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('../ui/mainWindow.ui', self)
        self.setUI()                # 调用ui界面
        self._initWindow()          # 主窗口初始化设置


    def _initWindow(self):
        #----------- 隐藏外窗口 -----------
        self.setWindowFlags(Qt.FramelessWindowHint)     #关闭默认工具栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明
        #-----------加载qss样式-------------
        self.__my_qss()
        #----------- 关闭 -----------------
        self.btn_close.clicked.connect(QCoreApplication.instance().quit)
        root = QFileInfo(__file__).absolutePath()
        self.btn_close.setIcon(QIcon(root+'src/resourse/close.png'))

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

    #-----------鼠标点击事件-----------
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
        self.textEdit.setText("welcome")
    def run(self):
        pass
    def upload(self):
        # self.ReadJson(self.file_path)
        # self.WriteJson(self.file_path)
        # self.sig_drawTable1_Do()
        pass
    def fail(self):
        pass
    def addFile(self):
        self.file_path, ok = QDialog.getOpenFileName(self, "选取文件", "C:/")  # 设置文件扩展名过滤,注意用双分号间隔 "All Files (*);;Text Files (*.txt)"

        if ok:
            QMessageBox.question(self, "文件选择确认框", "是否确认选择此文件?\n"+self.file_path, QMessageBox.Yes | QMessageBox.No)
            self.textEdit.setText(f'您已选取: "{self.file_path}"')



    #----------- 表格&json文件-------------
    def sig_drawTable1_Do(self, datas):
        if not self.table1DrawOk:
            return
        self.table1DrawOk = False
        self.table1.clearContents()
        self.table1.setRowCount(0)
        try:
            self.table1.setRowCount(len(datas))  # 设置行数
            rowcount = 0
            for i in datas:
                self.table1.setItem(rowcount, 0, QTableWidgetItem(i["id"]))
                self.table1.setItem(rowcount, 1, QTableWidgetItem(i["filename"]))
                self.table1.setItem(rowcount, 2, QTableWidgetItem(i["path"]))
                self.table1.setItem(rowcount, 3, QTableWidgetItem(i["note"]))
                self.table1.setItem(rowcount, 4, QTableWidgetItem(i["user"]))
                self.table1.setItem(rowcount, 5,
                                    QTableWidgetItem(time.strftime("%Y-%m-%d   %H:%M:%S", time.localtime(i["time"]))))
                self.table1.setItem(rowcount, 6, QTableWidgetItem(i["nodeENname"]))
                self.table1.setItem(rowcount, 7, QTableWidgetItem(
                    self.ProjectNameById[i["projectid"]] if i["projectid"] in self.ProjectNameById.keys() else "未知"))

                rowcount += 1
        except:
            traceback.print_exc()

    # 读取json文件内容，返回一个字典
    def ReadJson(path):
        try:
            with open(path, encoding='utf-8') as f:
                content = f.read()  # 读文件
                if content.startswith(u'\ufeff'):
                    content = content.encode('utf8')[3:].decode('utf8')
                js = json.loads(content)  # 把json串变成python的数据类型：字典
            return js
        except:
            return None

    # 接收json字典，存进json文件中
    def WriteJson(path, data):
        try:
            if not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))
            with open(path, 'w', encoding='utf-8') as f:
                # 字典转成json,字典转换成字符串,不需要写文件，自动将转成的json字符串写入到文件中
                json.dump(data, f, ensure_ascii=True, indent=4)
        except:
            traceback.print_exc()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = Login()
    a.show()
    b = Window()
    a.btn_SignIn.clicked.connect(b.show)
    sys.exit(app.exec_())
