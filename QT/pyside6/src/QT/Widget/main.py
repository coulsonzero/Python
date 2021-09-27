"""
@author: coulson
@version: 2021/8/10  14:27
"""
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader
# from resource.ui_mainWindow import Ui_Form


class Window:
    def __init__(self):
        super(Window, self).__init__()


if __name__ == '__main__':
    app = QApplication([])
    # app.setWindowIcon(QIcon("logo.png"))    # 添加图标
    w = Window()
    w.show()
    app.exec_()