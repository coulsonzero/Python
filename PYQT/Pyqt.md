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


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 1.创建应用程序(必备)
    ex = Windows()                
    sys.exit(app.exec_())         # 3.退出显示(必备), 没有会闪退
```
