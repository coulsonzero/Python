from PySide6.QtWidgets import *


def btnClick():
    info = textEdit.toPlainText()   # 获取文本信息
    print(info)
    # print("button被点击")


if __name__ == '__main__':
    app = QApplication([])
    win = QMainWindow()

    # 窗口属性
    win.resize(500, 400)
    win.move(700, 210)    # "默认居中"
    win.setWindowTitle("测试窗口")

    # 多行文本输入框
    textEdit = QTextEdit(win)
    textEdit.move(50, 50)
    textEdit.resize(200, 300)
    textEdit.setPlaceholderText("请输入文本")

    # 按钮
    btn = QPushButton("PushButton", win)
    btn.move(300, 100)
    btn.clicked.connect(btnClick)    # 若为btnClick(): 会打开窗口后立刻执行



    win.show()
    app.exec_()
