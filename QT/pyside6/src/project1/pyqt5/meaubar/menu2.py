"""
@author: coulson
@version: 2021/7/22  17:39

菜单栏
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon(r'C:\Users\Administrator\Desktop\img.jpg'), '&Exit', self)  # 菜单图标
        exitAction.setShortcut('Ctrl+Q')                        # 菜单快捷键
        exitAction.setStatusTip('Exit application')             # 状态提示
        exitAction.triggered.connect(qApp.quit)                 # 退出

        self.statusBar()

        # 创建菜单栏
        menubar = self.menuBar()
        # 添加菜单
        fileMenu = menubar.addMenu('&File')
        # 绑定菜单事件
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())