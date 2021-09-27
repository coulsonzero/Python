"""
@author: coulson
@version: 2021/8/5  16:50
"""

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from src.module.ui_main import Ui_Form
from src.ui import *

widgets = None
class MyWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # self.__initWindow()  # 主窗口初始化设置
        # SET AS GLOBAL WIDGETS
        self.setUI()
        self.show()

    def __initWindow(self):
        # ----------- 隐藏外窗口 -----------
        self.setWindowFlags(Qt.FramelessWindowHint)  # 关闭默认工具栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明

    def setUI(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        title = "Coulson - Modern GUI"
        self.setWindowTitle(title)


        # widgets.titleRightInfo.setText(description)
        widgets.btn1.clicked.connect(self.buttonClick)
        widgets.btn2.clicked.connect(self.buttonClick)
        widgets.btn3.clicked.connect(self.buttonClick)

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn1":
            widgets.stackedWidget.setCurrentWidget(widgets.page1)
            # UIFunctions.resetStyle(self, btnName)
            # btn.setStyleSheet(
            #     """
            #     QPushbutton{background-color: green;}
            #     QPushbutton:hover{background-color: yellow;}
            #     QPushbutton:pressed{background-color: red;}
            #     """
            # )

        # SHOW NEW PAGE
        elif btnName == "btn2":
            widgets.stackedWidget.setCurrentWidget(widgets.page2)  # SET PAGE
            print("page2 was changed")
            # UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        elif btnName == "btn3":
            widgets.stackedWidget.setCurrentWidget(widgets.page3)

        else:
            print("No button pressed")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


if __name__ == "__main__":
    app = QApplication([])
    # app.setWindowIcon(QIcon("icon.ico"))
    window = MyWindow()
    app.exec()     #'exec_' will be removed in the future. Use 'exec' instead.


