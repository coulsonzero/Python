"""
@author: coulson
@version: 2021/7/27  14:42
"""
from PyQt5 import Qt
from PySide2.QtWidgets import *
from icecream import ic


class Window:
    def __init__(self):
        self.win = QMainWindow()
        self.win.resize(500, 400)
        self.win.move(700, 210)
        self.win.setWindowTitle("测试窗口")
        # self.win.setWindowFlags(Q)
        # self.win.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗体透明控件不透明

        self.textEdit = QTextEdit(self.win)
        self.textEdit.move(50, 50)
        self.textEdit.resize(200, 300)
        self.textEdit.setPlaceholderText("请输入文本")

        self.btn = QPushButton("btn", self.win)
        self.btn.move(300, 100)
        self.btn.clicked.connect(self.btnClick)

        # 按钮操作判断
        self.btn.isDown()  # 按下？
        self.btn.isChecked()  # 已标记？
        self.btn.isEnabled()  # 可点击？
        self.btn.isCheckable()  # 可标记？
        self.btn.setStyleSheet(
            "QPushButton {color:red;}"
            "QPushButton:hover {color:green;}"
            "QPushButton:pressed {color: blue; border-radius:10px;}"
        )
        self.btn.setFlat(True)  # 去按钮边框

    def btnClick(self, ):
        info = self.textEdit.toPlainText()  # 获取文本信息
        print(info)
        # print("btn被点击")


if __name__ == '__main__':
    app = QApplication([])
    # win = QMainWindow()
    # win.show()
    w = Window()
    w.win.show()
    app.exec_()
