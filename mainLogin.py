# -*- coding: utf-8 -*-
import login_logic
import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow():
    def setupUi(self, MainWindow):
        # 主窗口的设置——名称、大小
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 584)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # lable的设置——位置、字体、大小
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 250, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 80, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        # 文本框的设置——同lable
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(260, 250, 291, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 310, 291, 41))
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 310, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 400, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        # 设置button的点击事件完成登录操作
        self.pushButton.clicked.connect(lambda: self.loginverify(MainWindow))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "账号"))
        self.label.setText(_translate("MainWindow", "实时通讯登录界面"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        MainWindow.setWindowTitle('通讯系统')

    # 登录验证的函数
    def loginverify(self, MainWindow):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        # 类的实例化
        loginLog = login_logic.loginLogic()
        msg, state = loginLog.checklogin(username, password)
        if state == 1:
            self.show_message(msg)
            # 执行跳转并关闭当前窗口
            MainWindow.close()
            # 跳转另一个窗口
            os.system("python chartClientLogic.py ")
        else:
            self.show_message(msg)
        print(msg, state)

    # 对登录的提示信息进行显示
    def show_message(self, msg):
        msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, '提示', msg)
        msg_box.exec_()
