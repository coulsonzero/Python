```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

if __name__ == '__main__':
    app = QApplication(sys.argv)    # 1.创建应用程序(必备)，若少此设置不会显示
    w = QWidget()                   # 2.默认构造函数(必备)
    w.show()                        # 3.显示(必备)

    # w.setWindowTitle('Simple')    # 窗口标题，默认"python"
    # w.move(500, 300)              # 窗口位置，默认"居中"
    # w.resize(300, 350)            # 调整窗口的大小, 默认
    # w.setFixedSize(960, 700)      # 固定窗口大小
    # w.setGeometry(600, 300, 700, 220) # 窗口位置和大小, 参数不可为空
    # w.setWindowIcon(QIcon(r'C:\Users\Administrator\Desktop\img.jpg'))  # 需要额外导入模块
    sys.exit(app.exec_())           # 4.退出程序(必备)(其它可选设置必须位于此之前)，少了此设置程序会立刻闪退
```



## Basic
```python3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Windows(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()           

    def initUI(self):
        # self.setGeometry(300, 300, 350, 300)
        # self.setWindowTitle('Title')
        # self.setWindowIcon(QIcon(r'C:\Users\Administrator\Desktop\img.jpg'))    # 窗口图标
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```



## Control
```python3
QLineEdit()         # 单行文本输入框
QTextEdit()         # 多行文本输入框
QLabel('Title')     # 标签
QPushButton("button", self)  # 按钮   绝对布局加self
QToolTip.setFont(QFont('SansSerif', 10))   # 字体

lcd = QLCDNumber(self)                  # Lcd显示屏
sld = QSlider(Qt.Horizontal, self)      # 滑条
sld.valueChanged.connect(lcd.display)   # 绑定事件
```

```python3
# 菜单
exitAction = QAction(QIcon(r'C:\Users\Administrator\Desktop\img.jpg'), 'Exit', self)
exitAction.setShortcut('Ctrl+Q')    # 菜单快捷键
exitAction.setStatusTip('Exit application') # 状态提示
exitAction.triggered.connect(self.close)    # 退出
# exitAction.triggered.connect(qApp.quit)   # 退出

self.statusBar()

menubar = self.menuBar()            # 创建菜单栏
fileMenu = menubar.addMenu('&File') # 添加菜单
fileMenu.addAction(exitAction)      # 绑定菜单事件

# 工具栏
toolbar = self.addToolBar('Exit')
toolbar.addAction(exitAction)
```


```python
# 点击按钮绑定事件
    def initUI(self):
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)
        btn1.clicked.connect(self.buttonClicked)    # 绑定事件
        ...
    # 事件处理
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


# 按“Esc”键退出程序！
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

# 点击窗口任意处退出
class Communicate(QObject):
    closeApp = pyqtSignal()
class Example(QMainWindow):
    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
    def mousePressEvent(self, event):
        self.c.closeApp.emit()


# 点击按钮显示事件
    def initUI(self):
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)
        btn1.clicked.connect(self.buttonClicked)    # 绑定事件
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

```


## 对话框
```python3
# 消息对话框
def initUI(self):
    self.btn = QPushButton('Dialog', self)      # 对话框
    self.btn.move(20, 20)
    self.btn.clicked.connect(self.showDialog)   # 绑定点击事件
    
    self.le = QLineEdit(self)
    self.le.move(130, 22)
def showDialog(self):
    text, ok = QInputDialog.getText(self, 'Input Dialog',
                                    'Enter your name:')


# 字体选择对话框
def initUI(self):
    btn = QPushButton('Dialog', self)
    btn.setSizePolicy(QSizePolicy.Fixed,
                      QSizePolicy.Fixed)
    btn.move(20, 20)
    btn.clicked.connect(self.showDialog)
    self.lbl = QLabel('Knowledge only matters', self)
    self.lbl.move(130, 20)
def showDialog(self):
    font, ok = QFontDialog.getFont()
    if ok:
        self.lbl.setFont(font)

# 颜色选取对话框
    def initUI(self):
        col = QColor(0, 0, 0)
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())
    def showDialog(self):
        col = QColorDialog.getColor()   # 色彩选取对话框
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())
```



## Layout
```python3
# 绝对布局
QPushButton("button", self).move(50, 50)

# 框布局
vbox = QVBoxLayout()
vbox.addWidget(btn)
vbox.addWidget(self.lbl)
self.setLayout(vbox)



okButton = QPushButton("OK")
cancelButton = QPushButton("Cancel")

hbox = QHBoxLayout()
hbox.addStretch(1)
hbox.addWidget(okButton)
hbox.addWidget(cancelButton)

vbox = QVBoxLayout()
vbox.addStretch(1)
vbox.addLayout(hbox)

self.setLayout(vbox) 


# 表格布局1
grid = QGridLayout()
self.setLayout(grid)
names = ['Cls', 'Bck', '', 'Close',
         '7', '8', '9', '/',
        '4', '5', '6', '*',
         '1', '2', '3', '-',
        '0', '.', '=', '+']
positions = [(i,j) for i in range(5) for j in range(4)]
for position, name in zip(positions, names):
    if name == '':
        continue
    button = QPushButton(name)
    grid.addWidget(button, *position)


# 表格布局2
title = QLabel('Title')
author = QLabel('Author')
review = QLabel('Review')

titleEdit = QLineEdit()
authorEdit = QLineEdit()
reviewEdit = QTextEdit()

grid = QGridLayout()
grid.setSpacing(10)

grid.addWidget(title, 1, 0)
grid.addWidget(titleEdit, 1, 1)

grid.addWidget(author, 2, 0)
grid.addWidget(authorEdit, 2, 1)

grid.addWidget(review, 3, 0)
grid.addWidget(reviewEdit, 3, 1, 5, 1)
```


***

## Coding
```python
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Windows(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()           

    def initUI(self):
        """
        按钮组件
        """
        btn = QPushButton("button", self)                                       # 创建按钮，名称
        btn.move(100, 50)                                                       # 移动按钮位置，默认左上角
        # qbtn.clicked.connect(QCoreApplication.instance().quit)                # 点击按钮退出程序
        # btn.setToolTip('This is a <b>QPushButton</b> widget')                 # 按钮放置提示
        
        
        # 标签
        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 10)
        
        """
        字体    
        """
        QToolTip.setFont(QFont('SansSerif', 10))                                # 设置字体
        
        """
        绘制窗口
        """
        self.setWindowTitle('AppWindows')                                       # 窗口标题
        self.setGeometry(700, 300, 400, 500)                                    # 位置和大小,参数不可为空
        # self.move(500, 300)              # 窗口位置，默认"居中"
        # self.resize(300, 350)            # 窗口的大小, 有默认值
        # self.setFixedSize(960, 700)      # 固定窗口大小，不可缩放
        
        self.setWindowIcon(QIcon(r'C:\Users\Administrator\Desktop\img.jpg'))    # 窗口图标
        self.show()                                                             # 显示窗口(必须位于最后一行)
    
    # 退出提示框
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
    # 按"Esc"退出程序
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 1.创建应用程序(必备)
    ex = Windows()                
    sys.exit(app.exec_())         # 3.退出显示(必备), 没有会闪退
```
