"""
@author: coulson
@version: 2021/7/28  10:40
"""

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class First(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton("Button", self)
        self.btn.move(30, 50)
        self.btn.setStyleSheet(''' 
                             QPushButton
                             {text-align : center;
                             background-color : white;
                             font: bold;
                             border-color: gray;
                             border-width: 2px;
                             border-radius: 10px;
                             padding: 6px;
                             height : 14px;
                             border-style: outset;
                             font : 14px;}
                             QPushButton:pressed
                             {text-align : center;
                             background-color : light gray;
                             font: bold;
                             border-color: gray;
                             border-width: 2px;
                             border-radius: 10px;
                             padding: 6px;
                             height : 14px;
                             border-style: outset;
                             font : 14px;}
                             ''')

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Event sender')
        self.show()


class Second(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Get sender')


if __name__ == '__main__':
    app = QApplication([])
    a = First()
    b = Second()
    a.show()
    a.btn.clicked.connect(b.show)   # 关键：点击按钮跳转到另一个窗口
    app.exec_()