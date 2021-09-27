"""
@author: coulson
@version: 2021/7/22  18:58
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(443, 120)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(50, 40, 301, 25))
        self.widget.setObjectName("widget")

        # 框布局
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 打开文件按钮
        self.openFileButton = QtWidgets.QPushButton(self.widget)
        self.openFileButton.setObjectName("openFileButton")
        self.horizontalLayout.addWidget(self.openFileButton)

        # 单行文本输入框
        self.filePathlineEdit = QtWidgets.QLineEdit(self.widget)
        self.filePathlineEdit.setObjectName("filePathlineEdit")
        self.horizontalLayout.addWidget(self.filePathlineEdit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "下载文件"))    # 窗口标题
        self.openFileButton.setText(_translate("Form", "选择文件"))           # 按钮名称



class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        # 点击按钮响应事件
        self.openFileButton.clicked.connect(self.openFile)

    # 响应事件
    def openFile(self):
        get_filename_path, ok = QFileDialog.getOpenFileName(self,
                      "选取单个文件",
                      "C:/",
                      "All Files (*);;Text Files (*.txt)")
        if ok:
            # 消息提示框
            QMessageBox.question(self, "确认框", "请确认是否选择此文件路径?\n"+get_filename_path, QMessageBox.Yes | QMessageBox.No)
            # 设置单行文本输入框内容
            self.filePathlineEdit.setText(str(get_filename_path))

if __name__ == "__main__":
  app = QApplication(sys.argv)
  w = MyMainForm()
  w.show()
  sys.exit(app.exec_())