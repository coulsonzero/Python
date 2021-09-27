"""
@author: coulson
@version: 2021/7/26  10:26
"""
from PySide6.QtGui import Qt
from PySide6.QtWidgets import *


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(500, 400)
        self.move(700, 210)
        self.setWindowTitle("测试窗口")


        self.frame = QFrame(self)
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.move(50, 50)
        self.textEdit.resize(200, 300)
        self.textEdit.setPlaceholderText("请输入文本")       # 文本提示

        self.btn = QPushButton("btn", self.frame)
        self.btn.move(300, 100)
        self.btn.clicked.connect(self.btnClick)
        # self.btn.clicked.connect(Qt.WindowMaximized)
        self.btn.setStyleSheet(
            """
            QPushButton {
                color:red;
                border-radius: 5px; 
            }
            QPushButton:hover {color:green;}
            QPushButton:pressed {color: blue; border-radius:10px;}
            """
        )
        # self.btn.setFlat(True)  # 去按钮边框

    def btnClick(self):
        # self.textEdit.append("welcome to here!")          # 增
        self.textEdit.clear()                           # 删
        print(self.textEdit.toPlainText())                # 查
        # self.textEdit.setText()                         # 改
        # self.textEdit.setPlaceholderText()



if __name__ == '__main__':
    app = QApplication([])
    # win = QMainWindow()
    # win.show()
    w = Window()
    w.show()
    app.exec_()

