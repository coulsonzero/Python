```python3
"""
@author: coulson
@version: 2021/7/22  14:08

resoult: 设置字体、按钮及提示
"""
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))                # 设置字体
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton("button", self)                       # 创建按钮，名称
        btn.move(100, 50)  # 移动按钮位置，默认左上角
        # btn.setToolTip('This is a <b>QPushButton</b> widget') # 提示
        # btn.resize(btn.sizeHint())                                # btn.sizeHint() 显示默认尺寸



        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```
