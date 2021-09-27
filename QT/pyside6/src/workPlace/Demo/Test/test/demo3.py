import sys
import time

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from ui_Sever import Ui_Form
from faker import Faker



class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.index = 0
        self.setupUI()
        self.show()



    def setupUI(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.table = self.ui.tableWidget
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)              # 将表格设置为只读模式
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)             # 设置整行选中



        self.add_btn = QPushButton(self)
        self.add_btn.setStyleSheet('''QWidget{ min-height: 20px; font-size:10pt; border:2px solid #F76677;border-radius:5px;}
                                                         QWidget:hover{background-color:rgb(225, 225, 225);}
                                                         QWidget:pressed{background-color:rgb(205, 205, 205);}
                                                     ''')
        self.add_btn.setText('添加定时器')
        self.add_btn.setGeometry(50, 10, 70, 20)
        self.add_btn.clicked.connect(self.add_timer)

    def add_timer(self):
        fake = Faker(locale='zh_CN')  # zh_CN/en_US
        # colList = [fake.name(), fake.password(), fake.address(), fake.ssn(), fake.company(), fake.phone_number(), fake.pystr()]
        col_1 = QTableWidgetItem(fake.name())
        col_1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        col_2 = QTableWidgetItem(fake.password())
        col_3 = QTableWidgetItem(fake.address())
        col_4 = QTableWidgetItem(fake.ssn())
        col_5 = QTableWidgetItem(fake.company())
        col_6 = QTableWidgetItem(fake.phone_number())
        col_7 = QTableWidgetItem(fake.pystr())
        # deleteButton = QPushButton()
        # deleteButton.setText("删除定时器")
        # deleteButton.clicked.connect(self.delTimer)
        self.table.insertRow(int(self.table.rowCount()))
        self.table.setItem(self.index, 0, col_1)
        self.table.setItem(self.index, 1, col_2)
        self.table.setItem(self.index, 2, col_3)
        self.table.setItem(self.index, 3, col_4)
        self.table.setItem(self.index, 4, col_5)
        self.table.setItem(self.index, 5, col_6)
        self.table.setItem(self.index, 6, col_7)
        # self.table.setCellWidget(self.index, 3, deleteButton)
        self.table.update()
        self.index += 1







    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.flag = True
            self.m_Position = QMouseEvent.globalPos() - self.pos()
            QMouseEvent.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))



if __name__ == '__main__':
    app = QApplication([])
    w = Window()
    app.exec()