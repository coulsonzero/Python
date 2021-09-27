# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowVDIwwK.ui'
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
        Form.setEnabled(True)
        Form.resize(1094, 627)
        Form.setContextMenuPolicy(Qt.ActionsContextMenu)
        icon = QIcon()
        icon.addFile(u"C:/Users/Administrator/.designer/Demo3/iconServer.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.000000000000000)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setGeometry(QRect(20, 20, 1041, 601))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet(u"QWidget #widget {\n"
"	border-radius: 20px;\n"
"	background-color: #323232;\n"
"	/*font-family: 'Poppins', sans-serif;*/\n"
"	\n"
"}\n"
"QLabel {\n"
"	color: red;\n"
"	font-family: \u534e\u6587\u884c\u6977;\n"
"	font-size: 15px;\n"
"}\n"
"QPushButton #btn_min:hover {\n"
"	color: red;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton {\n"
"	color: white;\n"
"	font-family: \u534e\u6587\u884c\u6977;\n"
"	font-size: 15px;\n"
"	background-color: grap;	\n"
"	transition: all 0.4s ease;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #f9d423;\n"
"	background-color: #323232;\n"
"	border: 1px solid skyblue;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	color: red;\n"
"	border: 1px solid skyblue;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"     	")
        self.img = QLabel(self.widget)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(15, 10, 16, 16))
        font = QFont()
        self.img.setFont(font)
        self.img.setFrameShape(QFrame.NoFrame)
        self.img.setPixmap(QPixmap(u"logo.ico"))
        self.img.setScaledContents(True)
        self.img.setWordWrap(False)
        self.img.setOpenExternalLinks(False)
        self.logo = QLabel(self.widget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(50, 10, 301, 16))
        self.logo.setStyleSheet(u"color: rgb(85, 255, 255);")
        self.layoutWidget = QWidget(self.widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 1021, 561))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_min = QPushButton(self.layoutWidget)
        self.btn_min.setObjectName(u"btn_min")
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/Administrator/Desktop/images/min.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_min.setIcon(icon1)
        self.btn_min.setCheckable(False)
        self.btn_min.setAutoDefault(False)
        self.btn_min.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_min)

        self.btn_close = QPushButton(self.layoutWidget)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setEnabled(True)
        self.btn_close.setStyleSheet(u"image-color: white;")
        icon2 = QIcon()
        icon2.addFile(u"C:/Users/Administrator/Desktop/images/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)
        self.btn_close.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_close)

        self.top_space = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.top_space)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_queue = QPushButton(self.layoutWidget)
        self.btn_queue.setObjectName(u"btn_queue")
        self.btn_queue.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_queue)

        self.btn_run = QPushButton(self.layoutWidget)
        self.btn_run.setObjectName(u"btn_run")
        self.btn_run.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_run)

        self.btn_upload = QPushButton(self.layoutWidget)
        self.btn_upload.setObjectName(u"btn_upload")
        self.btn_upload.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_upload)

        self.btn_fail = QPushButton(self.layoutWidget)
        self.btn_fail.setObjectName(u"btn_fail")
        self.btn_fail.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_fail)

        self.btn_space = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.btn_space)

        self.btn_addfile = QPushButton(self.layoutWidget)
        self.btn_addfile.setObjectName(u"btn_addfile")
        self.btn_addfile.setAutoFillBackground(False)
        self.btn_addfile.setStyleSheet(u"")
        self.btn_addfile.setAutoDefault(False)
        self.btn_addfile.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_addfile)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableWidget = QTableWidget(self.layoutWidget)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet(u"border-radius: 10px;")
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout.addWidget(self.tableWidget)

        self.bottom_space = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.bottom_space)

        self.textEdit = QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"border-radius: 10px;")

        self.verticalLayout.addWidget(self.textEdit)

        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 40)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 15)

        self.retranslateUi(Form)

        self.btn_addfile.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5929\u5de5\u827a\u5f69\u6279\u91cf\u4e0a\u4f20\u5de5\u5177", None))
        self.img.setText("")
        self.logo.setText(QCoreApplication.translate("Form", u"\u5929\u5de5\u827a\u5f69", None))
        self.btn_min.setText("")
        self.btn_close.setText("")
        self.btn_queue.setText(QCoreApplication.translate("Form", u"\u6392\u961f\u4e2d", None))
        self.btn_run.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c\u4e2d", None))
        self.btn_upload.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u6210\u529f", None))
        self.btn_fail.setText(QCoreApplication.translate("Form", u"\u5904\u7406\u5931\u8d25", None))
        self.btn_addfile.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u6587\u4ef6", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u540d", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u5907\u6ce8\u4fe1\u606f", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u8def\u5f84", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u63d0\u4ea4\u65f6\u95f4", None));
    # retranslateUi

