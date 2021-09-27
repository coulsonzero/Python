# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainhuoUvJ.ui'
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
        Form.resize(1188, 729)
        self.styleSheet = QWidget(Form)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setGeometry(QRect(180, 80, 951, 581))
        self.styleSheet.setStyleSheet(u"*{\n"
"	margin: 0;\n"
"	padding: 0;\n"
"}\n"
"\n"
"QPushbutton{background-color: green;}\n"
"QPushbutton:hover{background-color: yellow;}\n"
"QPushbutton:pressed{background-color: red;}")
        self.app = QFrame(self.styleSheet)
        self.app.setObjectName(u"app")
        self.app.setGeometry(QRect(20, 20, 911, 531))
        self.app.setFrameShape(QFrame.StyledPanel)
        self.app.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.app)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.LeftMenu = QFrame(self.app)
        self.LeftMenu.setObjectName(u"LeftMenu")
        self.LeftMenu.setFrameShape(QFrame.StyledPanel)
        self.LeftMenu.setFrameShadow(QFrame.Raised)
        self.btn1 = QPushButton(self.LeftMenu)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setGeometry(QRect(20, 60, 75, 24))
        self.btn2 = QPushButton(self.LeftMenu)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setGeometry(QRect(20, 170, 75, 24))
        self.btn3 = QPushButton(self.LeftMenu)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setGeometry(QRect(20, 290, 75, 24))

        self.horizontalLayout.addWidget(self.LeftMenu)

        self.pages = QFrame(self.app)
        self.pages.setObjectName(u"pages")
        self.pages.setFrameShape(QFrame.StyledPanel)
        self.pages.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 641, 421))
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.label = QLabel(self.page1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, -10, 721, 441))
        self.label.setPixmap(QPixmap(u"C:/Users/Administrator/Desktop/images/background.png"))
        self.label.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.comboBox = QComboBox(self.page2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(40, 70, 69, 22))
        self.textEdit = QTextEdit(self.page2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(150, 70, 471, 311))
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.calendarWidget = QCalendarWidget(self.page3)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(10, 20, 631, 401))
        self.stackedWidget.addWidget(self.page3)

        self.horizontalLayout.addWidget(self.pages)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 6)

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn1.setText(QCoreApplication.translate("Form", u"home", None))
        self.btn2.setText(QCoreApplication.translate("Form", u"btn2", None))
        self.btn3.setText(QCoreApplication.translate("Form", u"btn3", None))
        self.label.setText("")
    # retranslateUi

