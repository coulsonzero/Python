# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fileload.ui'
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
        Form.resize(861, 606)
        icon = QIcon()
        icon.addFile(u"iconServer.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(180, 50, 467, 411))
        self.widget.setStyleSheet(u"QWidget #widget {\n"
"	border-radius: 20px;\n"
"	background-color: #323232;\n"
"}\n"
"\n"
"QPushButton #btn_min:hover {\n"
"	color: red;\n"
"}\n"
"QPushButton {\n"
"	color: white;\n"
"	font-family: \u5fae\u8f6f\u96c5\u9ed1;\n"
"	font-weight: bold;\n"
"	background-color: grap;\n"
"}\n"
"QPushButton:hover {\n"
"	color: #f9d423;\n"
"	background-color: #323232;\n"
"	border-radius:2px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_min = QPushButton(self.widget)
        self.btn_min.setObjectName(u"btn_min")
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/Administrator/Desktop/images/min.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_min.setIcon(icon1)
        self.btn_min.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_min)

        self.btn_close = QPushButton(self.widget)
        self.btn_close.setObjectName(u"btn_close")
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
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButton_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableWidget = QTableWidget(self.widget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.verticalSpacer = QSpacerItem(446, 6, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 20)
        self.verticalLayout.setStretch(3, 16)
        self.verticalLayout.setStretch(4, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5929\u5de5\u827a\u5f69\u6279\u91cf\u4e0a\u4f20\u5de5\u5177", None))
        self.btn_min.setText("")
        self.btn_close.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u6392\u961f\u4e2d", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c\u4e2d", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u6210\u529f", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u5904\u7406\u5931\u8d25", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u6587\u4ef6", None))
    # retranslateUi

