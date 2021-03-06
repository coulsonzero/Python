from PySide2.QtWidgets import *
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class Window:
    def __init__(self):
        # 从文件中加载UI定义
        qfile = QFile("demo2.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()

        # 从UI定义中动态创建一个相应的窗口对象, 将其内部文件定义为self.ui.PushButton
        self.ui = QUiLoader().load(qfile)


if __name__ == '__main__':
    app = QApplication([])
    w = Window()
    w.ui.show()
    # w.win.show()
    app.exec_()
