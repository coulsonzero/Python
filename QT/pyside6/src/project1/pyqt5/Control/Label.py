"""
@author: coulson
@version: 2021/7/23  11:27

在单行文本输入框输入内容后，在标签中显示出来
"""
import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QLineEdit, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 标签
        self.lbl = QLabel(self)
        self.lbl.move(60, 40)

        # 单行文本输入框
        qle = QLineEdit(self)
        qle.move(60, 100)
        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()

    # 输入文本后，在标签显示
    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()   # 自动调整大小


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
