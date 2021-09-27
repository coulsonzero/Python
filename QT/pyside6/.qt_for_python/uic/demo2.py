# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demo2.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import fp_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(476, 699)
        icon = QIcon()
        icon.addFile(u"iconServer.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"")
        self.Login = QWidget(Form)
        self.Login.setObjectName(u"Login")
        self.Login.setGeometry(QRect(-1, -1, 478, 705))
        self.Login.setToolTipDuration(1)
        self.Login.setStyleSheet(u"QWidget #Form {\n"
"    background-color: rgb(85, 85, 127);\n"
"    font-family: Arial, Helvetica; \n"
"	background: url(backImg.png);\n"
"	z-index: 2;\n"
"	/* color: white; */	\n"
"}\n"
"QWidget #Login {\n"
"	background-color: rgb(85, 85, 127);\n"
"	font-family: Arial, Helvetica; \n"
"	z-index: 1;\n"
"	/* color: white; */\n"
"	\n"
"}\n"
"QLabel, QPushButton, QCheckBox {\n"
"	color: white;\n"
"}\n"
"QLineEdit {\n"
"	height: 30px;\n"
"}\n"
"\n"
"QLabel #Label_SignIn {\n"
"	font-size: 20px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.Login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.Login)
        self.label.setObjectName(u"label")
        self.label.setMouseTracking(False)
        self.label.setTabletTracking(False)
        self.label.setAcceptDrops(False)
        self.label.setAutoFillBackground(False)
        self.label.setPixmap(QPixmap(u"C:/Users/Administrator/Desktop/img.jpg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setIndent(2)
        self.label.setOpenExternalLinks(False)

        self.verticalLayout.addWidget(self.label)

        self.userBox = QHBoxLayout()
        self.userBox.setObjectName(u"userBox")
        self.userLabel = QLabel(self.Login)
        self.userLabel.setObjectName(u"userLabel")
        self.userLabel.setPixmap(QPixmap(u"user.png"))
        self.userLabel.setAlignment(Qt.AlignCenter)
        self.userLabel.setOpenExternalLinks(False)

        self.userBox.addWidget(self.userLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.userBox.addItem(self.horizontalSpacer)

        self.userLine = QLineEdit(self.Login)
        self.userLine.setObjectName(u"userLine")
        self.userLine.setAlignment(Qt.AlignCenter)

        self.userBox.addWidget(self.userLine)

        self.userSpaceRight = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.userBox.addItem(self.userSpaceRight)

        self.userBox.setStretch(0, 2)
        self.userBox.setStretch(1, 1)
        self.userBox.setStretch(2, 18)
        self.userBox.setStretch(3, 1)

        self.verticalLayout.addLayout(self.userBox)

        self.passwordBox = QHBoxLayout()
        self.passwordBox.setObjectName(u"passwordBox")
        self.passwordLabel = QLabel(self.Login)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setPixmap(QPixmap(u"password.png"))
        self.passwordLabel.setAlignment(Qt.AlignCenter)

        self.passwordBox.addWidget(self.passwordLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.passwordBox.addItem(self.horizontalSpacer_2)

        self.passwordLine = QLineEdit(self.Login)
        self.passwordLine.setObjectName(u"passwordLine")
        self.passwordLine.setStyleSheet(u"")
        self.passwordLine.setAlignment(Qt.AlignCenter)

        self.passwordBox.addWidget(self.passwordLine)

        self.passwordSpacerRight = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.passwordBox.addItem(self.passwordSpacerRight)

        self.passwordBox.setStretch(0, 2)
        self.passwordBox.setStretch(1, 1)
        self.passwordBox.setStretch(2, 18)
        self.passwordBox.setStretch(3, 1)

        self.verticalLayout.addLayout(self.passwordBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.Label_SignIn = QLabel(self.Login)
        self.Label_SignIn.setObjectName(u"Label_SignIn")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.Label_SignIn.setFont(font)

        self.horizontalLayout.addWidget(self.Label_SignIn)

        self.btn_SignIn = QPushButton(self.Login)
        self.btn_SignIn.setObjectName(u"btn_SignIn")
        font1 = QFont()
        font1.setPointSize(10)
        self.btn_SignIn.setFont(font1)
        self.btn_SignIn.setMouseTracking(False)
        self.btn_SignIn.setTabletTracking(False)
        self.btn_SignIn.setAcceptDrops(False)
        self.btn_SignIn.setToolTipDuration(4)
        self.btn_SignIn.setLayoutDirection(Qt.LeftToRight)
        self.btn_SignIn.setAutoFillBackground(False)
        self.btn_SignIn.setStyleSheet(u"color: white;\n"
"border-radius: 25px; \n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"login.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_SignIn.setIcon(icon1)
        self.btn_SignIn.setIconSize(QSize(100, 100))
        self.btn_SignIn.setCheckable(False)
        self.btn_SignIn.setAutoRepeat(False)
        self.btn_SignIn.setAutoExclusive(False)
        self.btn_SignIn.setAutoRepeatInterval(100)
        self.btn_SignIn.setAutoDefault(False)
        self.btn_SignIn.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_SignIn)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 5)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_SignUp = QPushButton(self.Login)
        self.btn_SignUp.setObjectName(u"btn_SignUp")
        self.btn_SignUp.setStyleSheet(u"\n"
"font: 10pt \"Comic Sans MS\";\n"
"text-decoration: underline;\n"
"\n"
"background-color: rgb(85, 85, 127); \n"
"")
        self.btn_SignUp.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_SignUp)

        self.btn_Forgot = QPushButton(self.Login)
        self.btn_Forgot.setObjectName(u"btn_Forgot")
        self.btn_Forgot.setStyleSheet(u"font: 10pt \"Comic Sans MS\";\n"
"text-decoration: underline;\n"
"background-color: rgb(85, 85, 127); ")
        self.btn_Forgot.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_Forgot)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        self.btn_SignIn.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5929\u5de5\u827a\u5f69\u6d4b\u8bd5", None))
        self.label.setText("")
        self.userLine.setPlaceholderText(QCoreApplication.translate("Form", u"username", None))
        self.passwordLabel.setText("")
        self.passwordLine.setPlaceholderText(QCoreApplication.translate("Form", u"password", None))
        self.Label_SignIn.setText(QCoreApplication.translate("Form", u"Sign in", None))
        self.btn_SignIn.setText("")
        self.btn_SignUp.setText(QCoreApplication.translate("Form", u"Sign up", None))
        self.btn_Forgot.setText(QCoreApplication.translate("Form", u"Forgot Passwords", None))
    # retranslateUi

