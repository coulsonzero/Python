## 创建窗口 Ⅰ
```python
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

if __name__ == '__main__':
    app = QApplication(sys.argv)    # 1.创建应用程序(必备)，若少此设置不会显示
    w = QWidget()                   # 2.默认构造函数(必备)
    w.show()                        # 3.显示窗口(必须位于最后一行)
    sys.exit(app.exec_())           # 4.退出程序(必备)(其它可选设置必须位于此之前)，少了此设置程序会立刻闪退
```



## 创建窗口OOP Ⅱ
```python3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()           

    def initUI(self):
        self.show()                     # 显示窗口(必须位于最后一行)

if __name__ == '__main__':
    app = QApplication(sys.argv)        # 1.创建应用程序(必备)
    w = Window()
    sys.exit(app.exec_())               # 3.退出显示(必备), 没有会闪退
```

窗口设置
```python3
.show()                              # 显示窗口
.setWindowTitle('Title')             # 标题,默认"python"
.setGeometry(x, y, length, width)    # 位置及大小, 参数不可为空
.setWindowIcon(QIcon("logo.png"))    # 图标
.usetWindowFlags(Qt.FramelessWindowHint)    # 去边框
.setAttribute(Qt.WA_TranslucentBackground)  # 窗口透明

#.move(x, y)                         # 位置, 默认"居中"
#.resize(300, 350)                   # 大小, 有默认大小
#.setFixedSize(960, 700)             # 固定大小
#.setFixedSize(self.width(), self.height()) 
```


## 组件
```python3
QLabel('password')                       # 标签   .setPixmap(QPixmap('close.png'))    .serText(*.toString)
QPushButton()                            # 按钮   .clicked.connect()   .setText()
QLineEdit()                              # 单行文本输入框  .testChanged[str].connect()  .setText(str(text)) .adjustSize()  .text()
QTextEdit()                              # 多行文本输入框  .setCentralWidget(textEdit)
QMessageBox.information(self,'titel',message=self.lineEdit.text())  # 消息提示框
QMessageBox.question()
QToolTip.setFont(QFont('SansSerif', 10)) # 字体                                  
QLCDNumber(self)                         # 数字显示屏    .display
QSlider(Qt.Horizontal, self)             # 滑条   .valueChanged.connect(lcd.display)    # 绑定事件 if value > ...
QCheckBox()                              # 复选框  .toggle()   .stateChanged.connect()
QComboBox                                # 下拉列表框    .addItem('China')  .activated[str].connect()    
QColor()                                 # 颜色框  .se
QProgressBar()                           # 进度条  .setValue()
QBasicTimer()                            # 时间块  .stop() .isActive()
QCalendarWidget()                        # 日历    .setGridVisible(True) .clocked[QDate].connect() date=cal.selectedDate()
QFrame()                                 # 框架    .setFrameshape(QFrame.StyledPanel)
QSplitter(Qt.Horizontal/Vertical)        #         .addWidget(QFrame(self))
menuBar()                                # 菜单栏  .addMenu() -> .addAction()
addToolBar                               # 工具栏  .addAction()
setToolTip()                             # 提示     

# 绝对布局
btn.move(100, 200)
# 框布局
vbox = QVBoxLayout()
vbox.addWidget(lcd)
vbox.addWidget(sld)
self.setLayout(vbox)

# 信号接收者
btn = sender()
btn.objectName()
```

## 菜单栏
```python3
菜单/工具栏响应事件
exitAction = QAction(QIcon(path), 'Exit', self) # "File"菜单"exit"选项
exitAction.setShortcut('Ctrl+Q')                # 菜单选项快捷键
exitAction.triggered.connect(self.close)        # 点击退出 Ⅰ
exitAction.triggered.connect(qApp.quit)         # 点击退出 Ⅱ
exitAction.setStatusTip('Exit application')     # 鼠标放置状态提示
self.statusBar()

# 菜单
menubar = self.menuBar()            # 创建菜单栏
fileMenu = menubar.addMenu('File')  # 添加"File"菜单
fileMenu.addAction(exitAction)      # 绑定"File"响应事件

# 工具栏
toolbar = self.addToolBar('Exit')
toolbar.addAction(exitAction)
```

## 事件响应
```python
# 点击按钮绑定事件
def initUI(self):
    btn = QPushButton("Button 1", self)
    btn.move(30, 50)
    btn.clicked.connect(self.buttonClicked)                                # 绑定事件
    # btn.clicked.connect(QCoreApplication.instance().quit)                # 点击按钮退出程序
    # btn.setToolTip('This is a <b>QPushButton</b> widget')                # 按钮放置提示
    ...
def buttonClicked(self):
    sender = self.sender()                                                 # 判断信号接收者
    self.statusBar().showMessage(sender.text() + ' was pressed')           # "Button 1 was pressed"


# 点击退出提示框
def closeEvent(self, e):
    reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    if reply == QMessageBox.Yes:
        e.accept()
    else:
        e.ignore()


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
```


## 对话框
```python3
# 消息提示对话框
QMessageBox.question(self, "文件选择确认框", "是否确认选择此文件?\n"+get_filename_path, QMessageBox.Yes | QMessageBox.No)    

# 输入对话框
def initUI(self):      
    self.btn = QPushButton('Dialog', self)
    self.btn.move(20, 20)
    self.btn.clicked.connect(self.showDialog)

    self.lineEdit = QLineEdit(self)
    self.lineEdit.move(130, 22)

    self.setGeometry(300, 300, 290, 150)
    self.setWindowTitle('Input dialog')
    self.show()
        
def showDialog(self):
    text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
    if ok:
        self.lineEdit.setText(str(text))


# 字体选择对话框   QFontDialog.getFont()   -> .setFont()
def initUI(self):
    btn = QPushButton('Dialog', self)
    btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    btn.move(20, 20)
    btn.clicked.connect(self.showDialog)
    self.lbl = QLabel('Knowledge only matters', self)
    self.lbl.move(130, 20)
def showDialog(self):
    font, ok = QFontDialog.getFont()
    if ok:
        self.lbl.setFont(font)


# 颜色选取对话框   QColorDialog.getColor()  -> .setStyleSheet()
    def initUI(self):
        col = QColor(0, 0, 0)
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }"% col.name())
    def showDialog(self):
        col = QColorDialog.getColor()   # 色彩选取对话框
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())
```



## 布局方式
```python3
# 绝对布局  .move(x,y)
QPushButton("button", self).move(50, 50)

# 框布局   QVBoxLayout()/QHBoxLayout() -> .addWidget()/vbox.addLayout(hbox) -> self.setLayout(vbox)
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


# 表格布局1  QGridLayout()
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



