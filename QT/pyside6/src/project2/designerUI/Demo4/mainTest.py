"""
@author: coulson
@version: 2021/7/28  19:05
"""
import json
import os
import time
import traceback

"""
@author: coulson
@version: 2021/7/28  14:32
"""
from PySide6 import QtCore
from PySide6.QtGui import Qt, QCursor

from project2.designerUI.Demo4.ui_mainWindow import Ui_Form, QCoreApplication
from src.project2.designerUI.Demo4 import *

from PySide6.QtWidgets import *
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader




class Window(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setupUi(self)
        self._init_main_window()  # 主窗口初始化设置
        self.initUI()  # 界面绘制交给InitUi方法

    def _init_main_window(self):
        # 设置窗体无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 设置背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)


    def initUI(self):
        ############ 排队中 ################
        self.btn_queue.clicked.connect(self.sig_drawtableWidget_Do)
        # self.btn_queue.setCheckable(True)  # 是否被选中

        ############ 添加文件 ###############
        self.btn_addfile.clicked.connect(self.openFile)
        self.btn_addfile.setCheckable(True)  # 是否被选中

        ############ 关闭 ##################
        self.btn_close.clicked.connect(QCoreApplication.instance().quit)

        ############ 最小化 ################
        self.btn_min.clicked.connect(self.showMinimized)

        ############ 运行中 ################
        # self.btn_run.clicked.connect(self.btnClick)

    def sig_drawtableWidget_Do(self, datas):
        if not self.tableWidgetDrawOk:
            return
        self.tableWidgetDrawOk = False
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        try:
            self.tableWidget.setRowCount(len(datas))  # 设置行数
            rowcount = 0
            for i in datas:
                self.tableWidget.setItem(rowcount, 0, QTableWidgetItem(i["id"]))
                self.tableWidget.setItem(rowcount, 1, QTableWidgetItem(i["filename"]))
                self.tableWidget.setItem(rowcount, 2, QTableWidgetItem(i["path"]))
                self.tableWidget.setItem(rowcount, 3, QTableWidgetItem(i["note"]))
                self.tableWidget.setItem(rowcount, 4, QTableWidgetItem(i["user"]))
                self.tableWidget.setItem(rowcount, 5, QTableWidgetItem(time.strftime("%Y-%m-%d   %H:%M:%S", time.localtime(i["time"]))))
                self.tableWidget.setItem(rowcount, 6, QTableWidgetItem(i["nodeENname"]))
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

    """
    自定义窗口移动方法
    """

    def mousePressEvent(self, QMouseEvent):
        """
        改为拖动按钮
        """
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

    """
    # 点击退出提示框
    def closeEvent(self, e):
        reply = QMessageBox.question(self, 'Message', "是否确认退出?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()
    """

    # 按“Esc”键退出程序！
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    # def btnClick(self):
    #     self.btn = self.sender()
    #     btnName = self.btn.objectName()  # self.btn.text()
    #     print(btnName)
    #
    #     if btnName == "btn_queue":
    #
    #         self.tableWidget.hide()
    #         self.textEdit.show()
    #         info = self.textEdit.toPlainText()  # 获取文本信息
    #         # info = self.textEdit.toPlainText()
    #         print(info)
    #
    #     # 打开文件
    #     if btnName == "btn_addfile":
    #         # self.btn_addfile.setStyleSheet("QPushButton#btn_addfile {color:green; background-color:skyblue; border:6px solid skyblue; border-radius: 10px;}")
    #         self.openFile()

    def openFile(self):
        get_filename_path, ok = QFileDialog.getOpenFileName(self, "选取文件",
                                                            "C:/")  # 设置文件扩展名过滤,注意用双分号间隔 "All Files (*);;Text Files (*.txt)"
        if ok:
            # QMessageBox.question(self, "文件选择确认框", "是否确认选择此文件?\n"+get_filename_path, QMessageBox.Yes | QMessageBox.No)
            self.textEdit.setText(f'您已选取: "{get_filename_path}"')


if __name__ == '__main__':
    app = QApplication([])
    w = Window()
    w.show()
    app.exec_()