# -*- coding: utf-8 -*-
"""
@Author: coulson
@Version: python3.9
@DateTime: 2021/9/2  18:20
"""
# PtQt5+MSSQL Hospital registrition Sys Manager
# C.H. 2017/12/08 First edition

# v0045 2017-12-10 20:02:37 End
# Release 1.2
# 1.2： 加入图标

# 中文注释重写 via Atom

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import time

i_id = int(time.time()%1000 - time.time()%100)*10   # 默认ID基于时间，并会自动在挂号后增加1
if i_id == 0:
    i_id == 1000                                    # 避开ID等于0的情况

logmsg = ''                                         # 用于保存Log

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        global i_id
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(938, 813)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Quit.setGeometry(QtCore.QRect(700, 690, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Quit.setFont(font)
        self.pushButton_Quit.setMouseTracking(False)
        self.pushButton_Quit.setAutoDefault(False)
        self.pushButton_Quit.setFlat(False)
        self.pushButton_Quit.setObjectName("pushButton_Quit")
        self.lineEdit_ID = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ID.setGeometry(QtCore.QRect(140, 290, 193, 41))
        self.lineEdit_ID.setObjectName("lineEdit_ID")

        # self.lineEdit_ID.setText(str(i_id))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 300, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 357, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 420, 121, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 490, 81, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 550, 81, 41))
        self.label_5.setObjectName("label_5")
        self.checkBox_isExpertRequired = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_isExpertRequired.setGeometry(QtCore.QRect(130, 100, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.checkBox_isExpertRequired.setFont(font)
        self.checkBox_isExpertRequired.setTristate(False)
        self.checkBox_isExpertRequired.setObjectName("checkBox_isExpertRequired")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 60, 81, 31))
        self.label_6.setObjectName("label_6")
        self.pushButton_checkDocOnDuty = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_checkDocOnDuty.setGeometry(QtCore.QRect(110, 160, 161, 51))
        self.pushButton_checkDocOnDuty.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_checkDocOnDuty.setFont(font)
        self.pushButton_checkDocOnDuty.setMouseTracking(False)
        self.pushButton_checkDocOnDuty.setObjectName("pushButton_checkDocOnDuty")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 630, 121, 41))
        self.label_7.setObjectName("label_7")
        self.pushButton_Reg = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Reg.setGeometry(QtCore.QRect(100, 700, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_Reg.setFont(font)
        self.pushButton_Reg.setObjectName("pushButton_Reg")
        self.lineEdit_Name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Name.setGeometry(QtCore.QRect(140, 353, 193, 41))
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.lineEdit_no = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_no.setGeometry(QtCore.QRect(140, 410, 193, 41))
        self.lineEdit_no.setObjectName("lineEdit_no")
        self.lineEdit_Age = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Age.setGeometry(QtCore.QRect(140, 550, 193, 41))
        self.lineEdit_Age.setObjectName("lineEdit_Age")
        self.comboBox_Dept = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Dept.setGeometry(QtCore.QRect(150, 50, 201, 41))

        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.comboBox_Dept.setFont(font)
        self.comboBox_Dept.setObjectName("comboBox_Dept")
        self.comboBox_Dept.addItem("")
        self.comboBox_Dept.addItem("")
        self.comboBox_Dept.addItem("")
        self.comboBox_Dept.addItem("")
        self.comboBox_Dept.addItem("")
        self.comboBox_Dept.addItem("")
        self.comboBox_Dept.addItem("")
        self.comboBox_Dept.addItem("")
        self.comboBox_Dept.addItem("")
        self.comboBox_Dept.addItem("")
        self.comboBox_Dept.addItem("")
        self.comboBox_Dept.addItem("")
        self.commandLinkButton_AutoID = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_AutoID.setGeometry(QtCore.QRect(330, 290, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.commandLinkButton_AutoID.setFont(font)
        icon = QtGui.QIcon.fromTheme("Cancel")
        self.commandLinkButton_AutoID.setIcon(icon)
        self.commandLinkButton_AutoID.setObjectName("commandLinkButton_AutoID")
        self.lineEdit_DocNo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_DocNo.setGeometry(QtCore.QRect(140, 630, 193, 41))
        self.lineEdit_DocNo.setObjectName("lineEdit_DocNo")
        self.pushButton_Quest = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Quest.setGeometry(QtCore.QRect(650, 380, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Quest.setFont(font)
        self.pushButton_Quest.setObjectName("pushButton_Quest")

        font = QtGui.QFont()
        font.setPointSize(12)

        self.radioButton_Man = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_Man.setGeometry(QtCore.QRect(140, 490, 61, 22))
        self.radioButton_Man.setObjectName("radioButton_Man")
        self.radioButton_Man.setFont(font)
        self.radioButton_woman = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_woman.setGeometry(QtCore.QRect(230, 490, 71, 22))
        self.radioButton_woman.setObjectName("radioButton_woman")
        self.radioButton_woman.setFont(font)

        self.radioButton_temp = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_temp.setGeometry(QtCore.QRect(270, 490, 71, 22))
        self.radioButton_temp.setObjectName("radioButton_temp")
        self.radioButton_temp.setVisible(0)

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(470, 390, 111, 61))
        self.label_8.setObjectName("label_8")
        self.pushButton_Del = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Del.setGeometry(QtCore.QRect(650, 480, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Del.setFont(font)
        self.pushButton_Del.setObjectName("pushButton_Del")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(470, 490, 111, 61))
        self.label_9.setObjectName("label_9")
        self.pushButton_Edit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Edit.setGeometry(QtCore.QRect(650, 580, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Edit.setFont(font)
        self.pushButton_Edit.setObjectName("pushButton_Edit")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(460, 590, 141, 61))
        self.label_10.setObjectName("label_10")
        self.pushButton_SaveLog = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SaveLog.setGeometry(QtCore.QRect(520, 690, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_SaveLog.setFont(font)
        self.pushButton_SaveLog.setMouseTracking(False)
        self.pushButton_SaveLog.setAutoDefault(False)
        self.pushButton_SaveLog.setFlat(False)
        self.pushButton_SaveLog.setObjectName("pushButton_SaveLog")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 240, 321, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(400, 380, 21, 391))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(380, 40, 541, 300))
        self.textBrowser.setObjectName("textBrowser")
        # self.textBrowser.setText('HooH')
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.setWindowIcon(QtGui.QIcon(r'icon.png'))

        self.retranslateUi(MainWindow)
        self.pushButton_SaveLog.clicked.connect(self.FILE_savelog)
        self.pushButton_checkDocOnDuty.clicked.connect(self.DB_checkDoc)
        self.pushButton_Quit.clicked.connect(MainWindow.close)
        self.pushButton_Reg.clicked.connect(self.DB_insert)
        self.pushButton_Quest.clicked.connect(self.DB_inquire)
        self.pushButton_Del.clicked.connect(self.DB_del)
        self.pushButton_Edit.clicked.connect(self.DB_update)
        self.commandLinkButton_AutoID.clicked.connect(self.Auto_ID)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):  # UI文件自生成的部分，用html语言可以自定义显示
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "挂号系统"))
        self.pushButton_Quit.setText(_translate("MainWindow", "退出"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">ID</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">姓名</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">健康卡号</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">性别</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">年龄</span></p></body></html>"))
        self.checkBox_isExpertRequired.setText(_translate("MainWindow", "是否专家"))
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">科室</span></p></body></html>"))
        self.pushButton_checkDocOnDuty.setText(_translate("MainWindow", "查询在岗医生"))
        self.label_7.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">医师号</span></p></body></html>"))
        self.pushButton_Reg.setText(_translate("MainWindow", "挂号"))
        self.pushButton_Quest.setText(_translate("MainWindow", "查询"))
        self.radioButton_Man.setText(_translate("MainWindow", "男"))
        self.radioButton_woman.setText(_translate("MainWindow", "女"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>请在左侧填入</p><p>条件进行检索</p></body></html>"))
        self.pushButton_Del.setText(_translate("MainWindow", "取消挂号"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p>请在左侧输入</p><p>ID或健康卡号</p></body></html>"))
        self.pushButton_Edit.setText(_translate("MainWindow", "修改信息"))
        self.label_10.setText(
            _translate("MainWindow", "<html><head/><body><p>请在左侧输入ID</p><p>和要修改的信息</p></body></html>"))
        self.pushButton_SaveLog.setText(_translate("MainWindow", "保存记录"))
        self.comboBox_Dept.setItemText(0, _translate("MainWindow", "全部"))
        self.comboBox_Dept.setItemText(1, _translate("MainWindow", "急症科"))
        self.comboBox_Dept.setItemText(2, _translate("MainWindow", "妇产科"))
        self.comboBox_Dept.setItemText(3, _translate("MainWindow", "肿瘤科"))
        self.comboBox_Dept.setItemText(4, _translate("MainWindow", "普外科"))
        self.comboBox_Dept.setItemText(5, _translate("MainWindow", "泌尿外科"))
        self.comboBox_Dept.setItemText(6, _translate("MainWindow", "儿科"))
        self.comboBox_Dept.setItemText(7, _translate("MainWindow", "五官科"))
        self.comboBox_Dept.setItemText(8, _translate("MainWindow", "中医科"))
        self.comboBox_Dept.setItemText(9, _translate("MainWindow", "放射科"))
        self.comboBox_Dept.setItemText(10, _translate("MainWindow", "麻醉医学科"))
        self.comboBox_Dept.setItemText(11, _translate("MainWindow", "神经内科"))
        self.commandLinkButton_AutoID.setText(_translate("MainWindow", "自动"))

    def Auto_ID(self):                              # ID自动编号
        global i_id
        self.lineEdit_ID.setText(str(i_id))

    def DB_checkDoc(self):                          #查询符合条件的医生
        global logmsg
        logmsg = ''
        strDp = self.comboBox_Dept.currentText()
        if self.checkBox_isExpertRequired.isChecked():
            isExpt = 1
            isExptzh = '是'
        else:
            isExpt = 0
            isExptzh = '否'

        Msg = '科室: ' + strDp + '  是否专家: ' + isExptzh + '\n查询到如下医生'
        self.textBrowser.setText(Msg)
        # 构造SQL语句
        sql = "SELECT * FROM doctor where Dept ='" + strDp + "' and ON_DUTY = 'Y' and Expert = " + str(isExpt)
        if strDp == '全部':
            sql = "SELECT * FROM doctor where ON_DUTY = 'Y' and Expert = " + str(isExpt)
        print(sql)
        # 连接到数据库
        server = "DESKTOP-9RUT87E"
        user = "Hospital"
        password = "123456"
        #print('Connecting to MSSQL...')
        conn = pymysql.connect(server, user, password, database="Hospital", charset='utf8')
        print('Connected')
        # 数据库操作
        logmsg += Msg + "\n" + sql +"\n"
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        while row:
            print(row)
            self.textBrowser.append("%s\t%s\t%8s\t%s" %(row[0], row[1], row[2], row[3]))
            logmsg += "%s\t%s\t%8s\t%s\n" %(row[0], row[1], row[2], row[3])
            row = cursor.fetchone()
        conn.close()
        self.statusbar.showMessage('查询成功', 1000)

    def DB_insert(self):                   # 挂号操作
        global i_id
        global logmsg
        logmsg = ''
        flag = 0    # 用于处理异常
        # 获取输入
        strID = self.lineEdit_ID.text()
        strName = self.lineEdit_Name.text()
        strNo = self.lineEdit_no.text()
        strAge = self.lineEdit_Age.text()
        strDocNo = self.lineEdit_DocNo.text()
        strDp = self.comboBox_Dept.currentText()
        if self.radioButton_Man.isChecked():
            strGender = '男'
            i_iGender = 1
        else:
            strGender = '女'
            i_iGender = 1

        Msg = '正在挂号'
        self.textBrowser.setText(Msg)
        #连接到数据库
        server = "DESKTOP-9RUT87E"
        user = "Hospital"
        password = "123456"
        print('Connecting to MSSQL...')
        conn = pymysql.connect(server, user, password, database="Hospital", charset='utf8')
        print('Connected...')

        cursor = conn.cursor()
        # 构造SQL语句
        sql = "insert into registration values('" + strID +"', '"+strName+"', '"+strNo+"', '"+strGender+"', '"+strAge+"', '"+strDp+"', '"+strDocNo+"')"
        # print(sql)
        logmsg += Msg +"\n" + sql
        # 数据库操作
        try:
            cursor.execute(sql)
            conn.commit()
            conn.close()
            self.textBrowser.append("\n挂号成功")
            logmsg += "\n挂号成功"
            self.textBrowser.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            # 清除填入的信息
            self.lineEdit_Name.clear()
            self.lineEdit_ID.clear()
            self.lineEdit_DocNo.clear()
            self.lineEdit_Age.clear()
            self.lineEdit_no.clear()
            self.radioButton_temp.setChecked(1)
            self.statusbar.showMessage('挂号成功', 2000)
            i_id += 1
            #self.lineEdit_ID.setText(str(i_id))
            flag = 1
        except Exception:   #处理异常
            if flag == 0:
                self.textBrowser.append("挂号失败，检查输入")
                self.statusbar.showMessage('插入异常', 2000)
                logmsg += '插入异常'

    def DB_inquire(self):     #可选条件查询操作
        global i_id
        global logmsg
        logmsg = '开始查询\n'
        # 获取输入
        strID = self.lineEdit_ID.text()
        strName = self.lineEdit_Name.text()
        strNo = self.lineEdit_no.text()
        strAge = self.lineEdit_Age.text()
        strDocNo = self.lineEdit_DocNo.text()
        strDp = self.comboBox_Dept.currentText()
        strGender = -1
        if self.radioButton_Man.isChecked():
            strGender = 1
            strGenderzh = '男'
        if self.radioButton_woman.isChecked():
            strGender = 0
            strGenderzh = '女'

        # 构造SQL语句
        sql_inquire = """SELECT registration.pti_ID,registration.pti_name, registration.pti_sex, registration.pti_age,doctor.doc_name,doctor.Dept
                      FROM registration,doctor
                      WHERE registration.doc_ID = doctor.doc_ID"""
        isini = 1           # 用于判断是否第一个动态构造块，即是否需要加 and
        # 对各项输入构造SQL语句
        if strID == '':  # ID
            print('ID  is empty')
            pass
        else:
            if isini == 1:
                sql_inquire += " and "
            sql_inquire += "registration.pti_ID = '" + strID + "'"
            isini = 1

        if strName == '':  # 姓名
            print('Name  is empty')
            pass
        else:
            if isini == 1:
                sql_inquire += " and "
            sql_inquire += "registration.pti_name = '" + strName + "'"
            isini = 1

        if strNo == '':  # 健康卡号
            print('CardNo is empty')
            pass
        else:
            if isini == 1:
                sql_inquire += " and "
            sql_inquire += "registration.pti_no = '" + strNo + "'"
            isini = 1

        if strGender == -1:  # 性别
            print('Gender is empty')
            pass
        else:
            if isini == 1:
                sql_inquire += " and "
            sql_inquire += "registration.pti_sex = '" + strGenderzh+ "'"
            isini = 1

        if strAge == '':  # 年龄
            print('Age  is empty')
            pass
        else:
            if isini == 1:
                sql_inquire += " and "
            sql_inquire += "registration.pti_age = " + strAge
            isini = 1

        if strDocNo == '':  # 医生
            print('DocID  is empty')
            pass
        else:
            if isini == 1:
                sql_inquire += " and "
            sql_inquire += "registration.doc_ID = '" + strDocNo + "'"
            isini = 1

        if strDp == '全部':  # 科室
            print('Dept is All-included')
            pass
        else:
            if isini == 1:
                sql_inquire += " and "
            sql_inquire += "registration.Dept = '" + strDp + "'"
            isini = 1
        # print(sql_inquire)
        logmsg += sql_inquire +"\n"
        flag = 0
        # 数据库操作
        try:
            server = "DESKTOP-9RUT87E"
            user = "Hospital"
            password = "123456"
            print('Connecting to MSSQL...')
            conn = pymysql.connect(server, user, password, database="Hospital", charset='utf8')
            print('Connected...')
            cursor = conn.cursor()
            cursor.execute(sql_inquire)
            row = cursor.fetchone()
            self.textBrowser.clear()
            self.textBrowser.append("编号\t姓名\t性别 年龄    医生\t 科室")
            while row:
                print(row)
                self.textBrowser.append(
                    "%s\t%s\t  %s   %-2d %+4s\t %s" % (row[0], row[1], row[2], row[3], row[4], row[5]))
                logmsg += "%s\t%s\t  %s   %-2d %+4s\t %s" % (row[0], row[1], row[2], row[3], row[4], row[5]) + "\n"
                row = cursor.fetchone()
            conn.close()
            # 用 \t 实现格式控制
            self.statusbar.showMessage('查询成功', 1000)
            # 清除输入的信息
            self.lineEdit_Name.clear()
            self.lineEdit_DocNo.clear()
            self.lineEdit_Age.clear()
            self.lineEdit_no.clear()
            self.radioButton_temp.setChecked(1)
            flag = 1
        except Exception:       # 处理异常
            if flag == 0:
                self.textBrowser.append("查询失败，检查输入")
                logmsg += "查询失败，检查输入"
                self.statusbar.showMessage('查询异常', 2000)

    def DB_del(self):           # 取消挂号
        global i_id
        global logmsg
        logmsg = '开始删除\n'
        flag = 0
        strID = self.lineEdit_ID.text()
        strNo = self.lineEdit_no.text()

        # 构造SQL语句
        sql_del = "delete from registration where "

        if strID != '':
            sql_del += "pti_ID = '" + strID +"'"
        elif strNo !='':
            sql_del += "pti_no = '" + strNo + "'"
        # 连接数据库
        server = "DESKTOP-9RUT87E"
        user = "Hospital"
        password = "123456"
        #print('Connecting to MSSQL...')
        conn = pymysql.connect(server, user, password, database="Hospital", charset='utf8')
        print('Connected...')
        #print(sql_del)
        logmsg += sql_del +"\n"
        # 数据库操作
        cursor = conn.cursor()
        try:
            cursor.execute(sql_del)
            conn.commit()
            conn.close()
            self.textBrowser.setText("\n取消挂号成功\n" + strID +" " + strNo +"项已删除")
            logmsg += "\n取消挂号成功\n" + strID +" " + strNo +"项已删除"
            self.textBrowser.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            # 清除填入的信息
            self.lineEdit_ID.clear()
            self.lineEdit_no.clear()
            self.radioButton_temp.setChecked(1)
            self.statusbar.showMessage('删除成功', 2000)
            flag = 1
        except Exception:           #处理异常
            if flag == 0:
                self.textBrowser.append("取消失败，检查输入")
                logmsg += "取消失败，检查输入"
                self.statusbar.showMessage('删除异常', 2000)

    def DB_update(self):            #修改信息
        global i_id
        global logmsg
        logmsg = "开始修改\n"
        flag = 0
        strID = self.lineEdit_ID.text()
        # 获取输入
        strName = self.lineEdit_Name.text()
        strNo = self.lineEdit_no.text()
        strAge = self.lineEdit_Age.text()
        strDocNo = self.lineEdit_DocNo.text()
        strDp = self.comboBox_Dept.currentText()
        strGender = ''
        if self.radioButton_Man.isChecked():
            strGender = '男'
        if self.radioButton_woman.isChecked():
            strGender = '女'
        if self.radioButton_temp.isChecked():
            strGender = ''
        # 构造SQL语句
        sql_edit = "update registration set "
        isini = 1  # 用于判断是否第一个动态构造块，即是否需要加 ','

        if strName != '':
            if isini == 0:
                sql_edit +=", "
            sql_edit += "pti_name = '"+ strName +"'"
            isini = 0

        if strNo != '':
            if isini == 0:
                sql_edit +=", "
            sql_edit += "pti_no = '"+ strNo +"'"
            isini = 0
        if strGender != '':
            if isini == 0:
                sql_edit +=", "
            sql_edit += "pti_sex = '"+ strGender +"'"
            isini = 0
        if strAge != '':
            if isini == 0:
                sql_edit +=", "
            sql_edit += "pti_age = "+ strAge
            isini = 0
        if strDp != '全部':
            if isini == 0:
                sql_edit +=", "
            sql_edit += "Dept = '"+ strDp +"'"
            isini = 0
        else:
            self.textBrowser.append("请选择要更改的科室")

        if strDocNo != '':
            if isini == 0:
                sql_edit +=", "
            sql_edit += "doc_ID = '"+ strDocNo +"'"
            isini = 0

        sql_edit +=" where pti_ID = '" + strID +"'"
        print(sql_edit)
        logmsg += sql_edit
        # 连接到数据库
        server = "DESKTOP-9RUT87E"
        user = "Hospital"
        password = "123456"
        print('Connecting to MSSQL...')
        conn = pymysql.connect(server, user, password, database="Hospital", charset='utf8')
        print('Connected...')
        #数据库操作
        cursor = conn.cursor()
        try:
            cursor.execute(sql_edit)
            conn.commit()
            conn.close()
            self.textBrowser.append("\n修改成功, ID: " + strID + " 项已修改")
            logmsg += "\n修改成功, ID: " + strID + " 项已修改"
            self.textBrowser.append(
                "%s\t%s\t  %s   %-2s %+4s\t %s" % (strID, strName, strGender, strAge, strDp, strDocNo))
            self.textBrowser.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            # 清除填入的信息
            self.lineEdit_Name.clear()
            self.lineEdit_ID.clear()
            self.lineEdit_DocNo.clear()
            self.lineEdit_Age.clear()
            self.lineEdit_no.clear()
            self.radioButton_temp.setChecked(1)
            self.statusbar.showMessage('修改成功', 2000)
            flag = 1
        except Exception:           #处理异常
            if flag == 0:
                self.textBrowser.append("修改失败，检查输入")
                logmsg += "修改失败，检查输入"
                self.statusbar.showMessage('修改异常', 2000)

    def FILE_savelog(self):         #保存日志
        fw = open('log.txt', 'a+')  #追加模式打开log
        global logmsg
        fw.write("\n" +time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "\n"+ logmsg+ "\n")
        fw.close()
        self.statusbar.showMessage('保存成功', 5000)

