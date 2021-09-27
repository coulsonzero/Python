"""
@author: coulson
@version: 2021/7/23  10:16
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton("打开文件", self)
        btn.move(100, 50)
        btn.clicked.connect(self.openFile)

        filePathlineEdit = QLineEdit(self)  # 单行文本框
        filePathlineEdit.move(200, 50)


        self.setWindowTitle("SelectFile")
        self.setGeometry(700, 420, 400, 150)
        self.show()

    def openFile(self):
        get_filename_path, ok = QFileDialog.getOpenFileName(self, "选取文件", "C:/",
                      "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
        if ok:
            QMessageBox.question(self, "文件选择确认框", "是否确认选择此文件?\n"+get_filename_path, QMessageBox.Yes | QMessageBox.No)
            self.filePathlineEdit.setText(str(get_filename_path))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())