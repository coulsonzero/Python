# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demo1.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtUiTools import QUiLoader


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(575, 377)
        self.textEdit = QPlainTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(90, 9, 371, 271))
        self.button = QPushButton(Form)
        self.button.setObjectName(u"PushButton")
        self.button.setGeometry(QRect(230, 310, 75, 23))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u6d4b\u8bd5\u7a97\u53e3", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u6587\u672c\u6846", None))
        self.button.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi


if __name__ == "__main__":
    app = QApplication([])
    win = QMainWindow()
    w = Ui_Form()
    w.setupUi(win)
    win.show()
    app.exec_()