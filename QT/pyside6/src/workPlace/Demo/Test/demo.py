import sys
# 懒得一个一个的写
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *


# 如果是pyqt5用下面的import
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *

class CircularProgress(QWidget):
    def __init__(self):
        super().__init__()
        # 记录角度
        self.angle = 90
        # 这个是用于绘制的，angle才是真实的角度
        self.drawAngle = self.angle
        # 进度条宽度
        self.lineWidth = 20
        # 时间线做动画
        self.timeLine = QTimeLine(1000, self)
        self.timeLine.frameChanged.connect(self.updateTimeline)


        # 数字输入框
        self.input = QSpinBox(self)
        self.input.setRange(0, 360)
        self.input.setValue(45)
        self.input.setGeometry(10, 10, 90, 30)
        # 按钮
        self.btn = QPushButton("Set", self)
        self.btn.setGeometry(10, 45, 90, 30)
        self.btn.clicked.connect(self.setAngle)
        # 透明样式
        self.setStyleSheet("QSpinBox,QPushButton{background:transparent;border:1px solid black;}")

    def updateTimeline(self, frame):
        self.drawAngle = frame
        self.update()

    def setAngle(self):
        self.drawAngle = self.angle
        self.angle = self.input.value()
        self.timeLine.stop()
        self.timeLine.setFrameRange(self.drawAngle, self.angle)
        # self.update()
        self.timeLine.start()

    def paintEvent(self, event):
        # 这里有个问题是，pyqt5无法隐式吧QRect转为QRectF(PySide2可以)，所以这里直接用QRectF
        the_rect = QRectF(0, 0, self.width(), self.height())
        if the_rect.isNull():
            return
        # 画笔
        painter = QPainter(self)
        painter.fillRect(the_rect, QColor("darkCyan"))
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform, on=True)
        # 镜像翻转，这样就是顺时针
        painter.setViewport(self.width(), 0, -self.width(), self.height())

        # path默认OddEvenFill，这样就填充两个圆相交的部分
        the_path = QPainterPath()
        the_path.addEllipse(the_rect.adjusted(1, 1, -1, -1))
        the_path.addEllipse(the_rect.adjusted(
            1 + self.lineWidth, 1 + self.lineWidth, -1 - self.lineWidth, -1 - self.lineWidth))
        painter.fillPath(the_path, QColor(6, 79, 103))

        # 径向渐变（参数为中心点和起始角度），默认时从右侧开始逆时针算的
        the_gradient = QConicalGradient(the_rect.center(), 90)
        the_angle = self.drawAngle / 360
        the_gradient.setColorAt(0, QColor(255, 255, 0));
        the_gradient.setColorAt(the_angle, QColor(255, 0, 255));
        if the_angle + 0.001 < 1:
            the_gradient.setColorAt(the_angle + 0.001, QColor(0, 0, 0, 0));
        painter.fillPath(the_path, the_gradient);


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = CircularProgress()
    w.resize(400, 400)
    w.show()
    sys.exit(app.exec_())