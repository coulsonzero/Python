"""
author: coulson
version: 2021-7-22  14:04
"""


import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Windows(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()           # 界面绘制交给InitUi方法

    def initUI(self):
        # self.setWindowTitle('Icon')
        # self.setGeometry(700, 300, 400, 500)  # 位置和大小
        # self.setWindowIcon(QIcon(r'C:\Users\Administrator\Desktop\img.jpg'))    # 窗口图标
        self.show()



if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Windows()
    sys.exit(app.exec_())