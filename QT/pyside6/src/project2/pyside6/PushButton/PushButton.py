"""
@author: coulson
@version: 2021/7/27  11:33
"""


'''
PushButton
'''

import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt



class PushButton(QWidget):
    def __init__(self):
        super(PushButton, self).__init__()
        self.initUI()



    def initUI(self):
        self.setWindowTitle("&PushButton")
        self.setGeometry(400, 400, 300, 260)

        # PushButton
        self.closeButton = QPushButton()
        # Attribute
        self.closeButton.move(100, 100)  # 绝对位置
        # self.closeButton.clicked.connect(self.close)  # 鼠标点击响应事件
        # self.closeButton.setFlat(True)
        self.closeButton.setCheckable(True)             # 是否默认被选中
        self.closeButton.setText("Close")               # 文字
        self.closeButton.setIcon(QIcon("close.png"))    # 图标
        self.closeButton.setShortcut('Ctrl+D')          # 快捷键
        self.closeButton.setToolTip("Close the widget") # 放置提示
                       # 隐藏按钮框

        # 按钮操作判断
        self.closeButton.isDown()  # 按下？
        self.closeButton.isChecked()  # 已标记？
        self.closeButton.isEnabled()  # 可点击？
        self.closeButton.isCheckable()  # 可标记？
        self.closeButton.setStyleSheet(                 # css样式
            """
            QPushbutton{color: black}
            QPushbutton:hover{color: green}
            QPushButton:pressed{background-color: yellow}   /* 按下未释放时 */
            """
        )

    def fun(self):
        if self.closeButton.isChecked():
            print('button pressed')

        else:
            print('button released')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PushButton()
    ex.show()
    sys.exit(app.exec_())
