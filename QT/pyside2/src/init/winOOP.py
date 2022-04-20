from PySide6.QtWidgets import *


class Window:
    def __init__(self):
        self.win = QMainWindow()
        self.win.resize(500, 400)
        self.win.move(700, 210)
        self.win.setWindowTitle("测试窗口")

        self.textEdit = QTextEdit(self.win)
        self.textEdit.move(50, 50)
        self.textEdit.resize(200, 300)
        self.textEdit.setPlaceholderText("请输入文本")

        self.button = QPushButton("button", self.win)
        self.button.move(300, 100)
        self.button.clicked.connect(self.btnClick)

    def btnClick(self):
        info = self.textEdit.toPlainText()   # 获取文本信息
        print(info)
        # print("button被点击")


if __name__ == '__main__':
    app = QApplication([])
    # win = QMainWindow()
    # win.show()
    w = Window()
    w.win.show()
    app.exec()
