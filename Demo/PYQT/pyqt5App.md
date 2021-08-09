
```python3
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
    w.setWindowIcon(QIcon(r'C:\Users\Administrator\Desktop\img.jpg'))  # 需要额外导入模块
    sys.exit(app.exec_())           # 4.退出程序(必备)(其它可选设置必须位于此之前)，少了此设置程序会立刻闪退
```
