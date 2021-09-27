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
        # 从文件中加载UI定义
        # QMainWindow.__init__(self)
        super(Window, self).__init__(parent)

        self._init_main_window()  # 主窗口初始化设置
        self.initUI()  # 界面绘制交给InitUi方法

    def _init_main_window(self):
        # 关闭默认工具栏
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 设置背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)


    def initUI(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        ############ 排队中 ################
        # self.ui.btn_queue.clicked.connect(self.btnClick)
        # self.ui.btn_queue.setCheckable(True)  # 是否被选中
        self.ui.btn_queue.clicked.connect(self.func)
        ############ 添加文件 ###############
        self.ui.btn_addfile.clicked.connect(self.btnClick)
        self.ui.btn_addfile.setCheckable(True)  # 是否被选中

        ############ 关闭 ##################
        self.ui.btn_close.clicked.connect(QCoreApplication.instance().quit)

        ############ 最小化 ################

        self.ui.btn_min.clicked.connect(self.showMinimized)

        ############ 运行中 ################
        self.ui.btn_run.clicked.connect(self.btnClick)





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



    def btnClick(self):
        self.btn = self.sender()
        btnName = self.btn.objectName() # self.btn.text()
        print(btnName)


        if btnName == "btn_queue":
            self.ui.btn_queue.setStyleSheet(
                "QPushButton#btn_queue {color:green; background-color:skyblue; border:6px solid skyblue; border-radius: 10px;}"
            )
            self.ui.tableWidget.hide()
            self.ui.textEdit.show()
            info = self.ui.textEdit.toPlainText()   # 获取文本信息
            # info = self.textEdit.toPlainText()
            print(info)

        # 打开文件
        if btnName == "btn_addfile":
            self.ui.btn_addfile.setStyleSheet(
                "QPushButton#btn_addfile {color:green; background-color:skyblue; border:6px solid skyblue; border-radius: 10px;}"
            )
            self.openFile()


    def openFile(self):
        get_filename_path, ok = QFileDialog.getOpenFileName(self, "选取文件", "C:/" )  # 设置文件扩展名过滤,注意用双分号间隔 "All Files (*);;Text Files (*.txt)"
        if ok:
            # QMessageBox.question(self, "文件选择确认框", "是否确认选择此文件?\n"+get_filename_path, QMessageBox.Yes | QMessageBox.No)
            self.ui.textEdit.setText(f'您已选取: "{get_filename_path}"')






    
if __name__ == '__main__':
    app = QApplication([])
    w = Window()
    w.show()
    app.exec_()