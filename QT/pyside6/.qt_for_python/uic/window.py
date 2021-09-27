# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fileloadvTvImM.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setContextMenuPolicy(Qt.ActionsContextMenu)
        icon = QIcon()
        icon.addFile(u"iconServer.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setGeometry(QRect(200, 400, 800, 801))
        Form.setWindowFlags(Qt.FramelessWindowHint)  # 去边框
        Form.setAttribute(Qt.WA_TranslucentBackground)  # 窗口透明

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(130, 40, 471, 501))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet(
            u"QWidget #widget {\n"
"	border-radius: 20px;\n"
"	background-color: #323232;\n"
"}\n"
"QLabel #logo{\n"
"	color: red;\n"
"}\n"
"QPushButton #btn_min:hover {\n"
"	color: red;\n"
"}\n"
"QPushButton {\n"
"	color: white;\n"
"	font-family: \u5fae\u8f6f\u96c5\u9ed1;\n"
"	font-weight: bold;\n"
"	background-color: grap;	\n"
"}\n"
"QPushButton:hover {\n"
"	color: #f9d423;\n"
"	background-color: #323232;\n"
"	border-radius:20px;\n"
"}\n"
"QTextEdit, QTableWidget{\n"
"	background-color: rgb(122, 122, 122);\n"
"}")

        self.img = QLabel(self.widget)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(15, 10, 16, 16))
        font = QFont()
        font.setPointSize(7)
        self.img.setFont(font)
        self.img.setFrameShape(QFrame.NoFrame)
        self.img.setPixmap(QPixmap(u"logo.ico"))
        self.img.setScaledContents(True)
        self.img.setWordWrap(False)
        self.img.setOpenExternalLinks(False)

        self.logo = QLabel(self.widget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(50, 10, 48, 16))
        self.logo.setStyleSheet(u"color: rgb(85, 255, 255);")

        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 30, 449, 456))

        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_min = QPushButton(self.widget1)
        self.btn_min.setObjectName(u"btn_min")
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/Administrator/Desktop/images/min.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_min.setIcon(icon1)
        self.btn_min.setCheckable(False)
        self.btn_min.setAutoDefault(False)
        self.btn_min.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_min)

        self.btn_close = QPushButton(self.widget1)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setEnabled(True)
        self.btn_close.setStyleSheet(u"image-color: white;")
        icon2 = QIcon()
        icon2.addFile(u"C:/Users/Administrator/Desktop/images/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)
        self.btn_close.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_close)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.widget1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_5 = QPushButton(self.widget1)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_4 = QPushButton(self.widget1)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet(u"")
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableWidget = QTableWidget(self.widget1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet(u"border-radius: 10px;")
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setCornerButtonEnabled(True)

        self.verticalLayout.addWidget(self.tableWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.textEdit = QTextEdit(self.widget1)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"border-radius: 10px;")

        self.verticalLayout.addWidget(self.textEdit)

        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 40)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 15)

        self.retranslateUi(Form)
        self.btn_close.clicked.connect(self.widget.close)
        self.btn_min.clicked.connect(self.widget.hide)

        self.pushButton_4.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5929\u5de5\u827a\u5f69\u6279\u91cf\u4e0a\u4f20\u5de5\u5177", None))
        self.img.setText("")
        self.logo.setText(QCoreApplication.translate("Form", u"\u5929\u5de5\u827a\u5f69", None))
        self.btn_min.setText("")
        self.btn_close.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u6392\u961f\u4e2d", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c\u4e2d", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u6210\u529f", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u5904\u7406\u5931\u8d25", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u6587\u4ef6", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication([])
    win = QMainWindow()
    w = Ui_Form()
    w.setupUi(win)
    win.show()
    app.exec_()