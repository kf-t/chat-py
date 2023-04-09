from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from chatServerLogic import chatServer
import login_logic


class server_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(943, 687)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 370, 241, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(620, 10, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(620, 80, 301, 561))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 470, 561, 121))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 410, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 610, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:self.send_mes())
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 370, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda :self.start_listen())
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 20, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 80, 571, 281))
        self.tableWidget.setAutoScrollMargin(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.setColumnWidth(0, 70)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setColumnWidth(1, 70)  # 设置table col的宽度
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.setColumnWidth(2, 200)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.setColumnWidth(3, 180)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "服务端"))
        self.label.setText(_translate("MainWindow", "消息记录"))
        self.textEdit_2.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "消息发送框："))
        self.pushButton.setText(_translate("MainWindow", "发送"))
        self.pushButton_3.setText(_translate("MainWindow", "连接客户端"))
        self.label_3.setText(_translate("MainWindow", "用户登录信息："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "用户名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "密码"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "登录时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "登录IP"))

    # 对设置端口进行监听/连接
    def start_listen(self):
        portNum = self.lineEdit_2.text()
        self.cs.listening(self.ui, int(portNum))

    # 消息发送
    def send_mes(self):
        mes = self.textEdit.toPlainText()
        # self.cs.s.recv(1024)
        # self.cs.conn, self.cs.addr = self.cs.s.accept()
        self.cs.conn.send(mes.encode('utf8'))
        self.textEdit.clear()
        self.textEdit_2.append("已发送至" + self.cs.addr + "：\n" + mes)

    # 读取数据库登录信息并显示
    def show_userInfo(self):
        loginLog = login_logic.loginLogic()
        loginLog.getLoginInfo()
        tupInfo = loginLog.loginInfo
        for num in range(len(tupInfo)):
            row_count = self.tableWidget.rowCount()  # 返回当前行数(尾部)
            self.tableWidget.insertRow(row_count)  # 尾部插入一行
            for i in range(1, len(tupInfo[num])):
                # 设置num行，i-1列的内容值为str(tupInfo[num][i])
                te = str(tupInfo[num][i])
                print(str(tupInfo[num][i]))
                self.tableWidget.setItem(num, i - 1, QtWidgets.QTableWidgetItem(str(tupInfo[num][i])))

if __name__ == '__main__':
    cs = chatServer()
    ap = QApplication(sys.argv)
    mw = QMainWindow()
    ui = server_MainWindow()  # 这是类函数的名称
    ui.cs = cs
    ui.ui = ui
    ui.setupUi(mw)  # 运行类函数里的setupUi
    mw.show()  # 显示窗口
    ui.show_userInfo()
    sys.exit(ap.exec())

