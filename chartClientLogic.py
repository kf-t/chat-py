import socket
import threading
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from client import client_MainWindow


class chatClient():
    def con(self, ui):
        self.ui = ui
        self.hostport = ('127.0.0.1', 9999)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(self.hostport)
        global true
        true = True

        def Receve(s, true):
            while true:
                data = s.recv(1024).decode('utf8')
                if data == 'quit':
                    true = False
                print('recevie news:\033[5;37;46m%s\033[0m' % data)
                self.ui.textEdit_2.append('来自服务器: \n%s' % data)

        thrd = threading.Thread(target=Receve, args=(self.s, true))
        thrd.start()


if __name__ == '__main__':
    cc = chatClient()
    app = QApplication(sys.argv)
    mw = QMainWindow()
    ui = client_MainWindow()  # 这是类函数的名称
    cc.con(ui)
    ui.cc = cc
    ui.setupUi(mw)  # 运行类函数里的setupUi
    mw.show()  # 显示窗口
    sys.exit(app.exec())

