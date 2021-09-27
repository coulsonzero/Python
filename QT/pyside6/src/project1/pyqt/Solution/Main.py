"""
@author: coulson
@version: 2021/7/22  17:02
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


"""
1. 创建窗口
2. 按钮、绑定按钮点击事件
3. 弹出文件选取窗口
4. 消息弹窗，显示文件路径
"""
class Windows(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton("button", self)       # 创建按钮
        btn.move(180, 100)                      # 按钮位置
        btn.clicked.connect(self.openFile)    # 绑定按钮点击事件




        self.setWindowTitle('Coulson')          # 窗口标题
        self.setGeometry(700, 300, 400, 300)    # 窗口位置和大小
        self.setWindowIcon(QIcon(r'C:\Users\Administrator\Desktop\img.jpg'))    # 窗口图标
        self.show()                             # 显示窗口


    # 文件选取对话框
    def openFile(self):

        get_filename_path, ok = QFileDialog.getOpenFileName(self,
                                                            "选取单个文件",
                                                            "C:/",
                                                            "All Files (*);;Text Files (*.txt)")
        if ok:
            self.filePathlineEdit.setText(str(get_filename_path))
        # fname = QFileDialog.getOpenFileName(self, '选取单个文件', 'C:/')
        # if fname[0]:
        #     with open(fname[0], 'r') as f:
        #         data = f.read()
        #         self.textEdit.setText(data)

    # 消息对话框
    def showMsg(self):
        QMessageBox.question(self, "message", "请确认是否选择此文件?", QMessageBox.Yes | QMessageBox.No)



if __name__ == '__main__':
    app = QApplication(sys.argv)    # 创建应用程序
    ex = Windows()
    sys.exit(app.exec_())           # 退出