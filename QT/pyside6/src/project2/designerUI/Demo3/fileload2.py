"""
@author: coulson
@version: 2021/7/27  12:14
"""
from PySide6.QtWidgets import *
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt



class First(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton("Button", self)
        self.btn.move(30, 50)


        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Event sender')
        self.show()

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
    a = First()
    a.show()
    w = Window()
    # w.ui.show()
    a.btn.clicked.connect(w.ui.show)  # 关键：点击按钮跳转到另一个窗口
    app.exec_()
