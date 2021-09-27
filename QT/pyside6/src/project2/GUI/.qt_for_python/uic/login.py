# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
        Form.resize(347, 454)
        icon = QIcon()
        icon.addFile(u"../../../../gitwork/git/pyside2/src/project2/designerUI/Demo2/iconServer.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"#Form {\n"
"	background: url(:/resourse/Project/project2/src/resourse/background.png);  /* border-image */\n"
"}")
        self.Login = QWidget(Form)
        self.Login.setObjectName(u"Login")
        self.Login.setGeometry(QRect(20, 20, 311, 401))
        self.Login.setToolTipDuration(1)
        self.Login.setStyleSheet(u"QWidget #Form {\n"
"    background-color: rgb(85, 85, 127);\n"
"    \n"
"	\n"
"	z-index: 2;\n"
"	/* color: white; */	\n"
"}\n"
"\n"
"QWidget #Login {\n"
"	border-radius: 20px;\n"
"	background-color: #323232;\n"
"	font-family: Arial, Helvetica; \n"
"}\n"
"\n"
"\n"
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
"QPushButton#btn_close:pressed, #btn_min:pressed {\n"
"	border: 2px solid skyblue;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushbutton #btn_SignIn {\n"
"	\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.label = QLabel(self.Login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(16, 15, 16, 16))
        self.label.setAutoFillBackground(False)
        self.label.setPixmap(QPixmap(u"../resourse/logo.ico"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.widget = QWidget(self.Login)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 60, 291, 321))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.userBox = QHBoxLayout()
        self.userBox.setObjectName(u"userBox")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.userBox.addItem(self.horizontalSpacer_4)

        self.userLabel = QLabel(self.widget)
        self.userLabel.setObjectName(u"userLabel")
        self.userLabel.setPixmap(QPixmap(u"C:/Users/Administrator/Desktop/images/user4.png"))
        self.userLabel.setAlignment(Qt.AlignCenter)
        self.userLabel.setOpenExternalLinks(False)

        self.userBox.addWidget(self.userLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.userBox.addItem(self.horizontalSpacer)

        self.userLine = QLineEdit(self.widget)
        self.userLine.setObjectName(u"userLine")
        self.userLine.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(179, 179, 179);\n"
"font-size:14px;\n"
"\n"
"")
        self.userLine.setAlignment(Qt.AlignCenter)

        self.userBox.addWidget(self.userLine)

        self.userSpaceRight = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.userBox.addItem(self.userSpaceRight)

        self.userBox.setStretch(0, 1)
        self.userBox.setStretch(1, 2)
        self.userBox.setStretch(2, 1)
        self.userBox.setStretch(3, 18)
        self.userBox.setStretch(4, 1)

        self.verticalLayout.addLayout(self.userBox)

        self.passwordBox = QHBoxLayout()
        self.passwordBox.setObjectName(u"passwordBox")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.passwordBox.addItem(self.horizontalSpacer_5)

        self.passwordLabel = QLabel(self.widget)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setPixmap(QPixmap(u"C:/Users/Administrator/Desktop/images/password.png"))
        self.passwordLabel.setAlignment(Qt.AlignCenter)

        self.passwordBox.addWidget(self.passwordLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.passwordBox.addItem(self.horizontalSpacer_2)

        self.passwordLine = QLineEdit(self.widget)
        self.passwordLine.setObjectName(u"passwordLine")
        self.passwordLine.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(179, 179, 179);\n"
"font-size:14px;")
        self.passwordLine.setAlignment(Qt.AlignCenter)

        self.passwordBox.addWidget(self.passwordLine)

        self.passwordSpacerRight = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.passwordBox.addItem(self.passwordSpacerRight)

        self.passwordBox.setStretch(0, 1)
        self.passwordBox.setStretch(1, 2)
        self.passwordBox.setStretch(2, 1)
        self.passwordBox.setStretch(3, 18)
        self.passwordBox.setStretch(4, 1)

        self.verticalLayout.addLayout(self.passwordBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.Label_SignIn = QLabel(self.widget)
        self.Label_SignIn.setObjectName(u"Label_SignIn")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.Label_SignIn.setFont(font)

        self.horizontalLayout.addWidget(self.Label_SignIn)

        self.btn_SignIn = QPushButton(self.widget)
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
        icon1.addFile(u"../resourse/login.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_SignIn.setIcon(icon1)
        self.btn_SignIn.setIconSize(QSize(100, 100))
        self.btn_SignIn.setCheckable(False)
        self.btn_SignIn.setAutoRepeat(False)
        self.btn_SignIn.setAutoExclusive(False)
        self.btn_SignIn.setAutoRepeatInterval(100)
        self.btn_SignIn.setAutoDefault(False)
        self.btn_SignIn.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_SignIn)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 8)
        self.horizontalLayout.setStretch(2, 12)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_SignUp = QPushButton(self.widget)
        self.btn_SignUp.setObjectName(u"btn_SignUp")
        self.btn_SignUp.setStyleSheet(u"font: 10pt \"Comic Sans MS\";\n"
"text-decoration: underline;\n"
"color: rgb(179, 179, 179);\n"
"background-color: rgb(85, 85, 127); \n"
"")
        self.btn_SignUp.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_SignUp)

        self.btn_Forgot = QPushButton(self.widget)
        self.btn_Forgot.setObjectName(u"btn_Forgot")
        self.btn_Forgot.setStyleSheet(u"font: 10pt \"Comic Sans MS\";\n"
"text-decoration: underline;\n"
"color: rgb(179, 179, 179);\n"
"background-color: rgb(85, 85, 127); ")
        self.btn_Forgot.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_Forgot)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.widget1 = QWidget(self.Login)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(42, 11, 251, 26))
        self.horizontalLayout_3 = QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.btn_min = QPushButton(self.widget1)
        self.btn_min.setObjectName(u"btn_min")
        icon2 = QIcon()
        icon2.addFile(u"../resourse/min.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_min.setIcon(icon2)
        self.btn_min.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btn_min)

        self.btn_close = QPushButton(self.widget1)
        self.btn_close.setObjectName(u"btn_close")
        icon3 = QIcon()
        icon3.addFile(u"../resourse/close2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon3)
        self.btn_close.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.retranslateUi(Form)

        self.btn_SignIn.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5929\u5de5\u827a\u5f69\u5ba2\u6237\u7aefV1.0", None))
        self.label.setText("")
        self.userLine.setText("")
        self.userLine.setPlaceholderText(QCoreApplication.translate("Form", u"username", None))
        self.passwordLabel.setText("")
        self.passwordLine.setPlaceholderText(QCoreApplication.translate("Form", u"password", None))
        self.Label_SignIn.setText(QCoreApplication.translate("Form", u"Sign in", None))
        self.btn_SignIn.setText("")
        self.btn_SignUp.setText(QCoreApplication.translate("Form", u"Sign up", None))
        self.btn_Forgot.setText(QCoreApplication.translate("Form", u"Forgot Passwords", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5929\u5de5\u827a\u5f69", None))
        self.btn_min.setText("")
        self.btn_close.setText("")
    # retranslateUi

