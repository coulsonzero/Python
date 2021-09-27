"""
@author: coulson
@version: 2021/7/27  16:32
"""
"""
@author: coulson
@version: 2021/7/27  12:14
"""
from PySide6.QtWidgets import *
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt


class Window:
    def __init__(self):
        # 从文件中加载UI定义
        qfile = QFile("fileload.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()

        # 从UI定义中动态创建一个相应的窗口对象, 将其内部文件定义为self.ui.PushButton
        self.ui = QUiLoader().load(qfile)
        self.ui.setWindowFlags(Qt.FramelessWindowHint)      # 去边框
        self.ui.setAttribute(Qt.WA_TranslucentBackground)   # 窗口透明









if __name__ == '__main__':
    app = QApplication([])
    w = Window()
    w.ui.show()
    app.exec_()
