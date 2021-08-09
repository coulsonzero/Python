from PySide2.QtWidgets import *
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class Window:
    def __init__(self):
        # 从文件中加载UI定义
        qfile = QFile("demo1.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()

        # 从UI定义中动态创建一个相应的窗口对象, 将其内部文件定义为self.ui.button
        self.ui = QUiLoader().load(qfile)

        self.ui.button.clicked.connect(self.btnClick)
        # self.button.clicked.connect(self.btnClick)

    def btnClick(self):
        info = self.ui.textEdit.toPlainText()   # 获取文本信息
        # info = self.textEdit.toPlainText()
        print(info)


if __name__ == '__main__':
    app = QApplication([])
    w = Window()
    w.ui.show()
    # w.win.show()
    app.exec_()
