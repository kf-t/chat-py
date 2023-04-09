import socket
import threading                                                # 导入多线程模块


class chatServer():
    def listening(self, ui, portNum):
        self.ui = ui
        print("Waitting to be connected......")
        self.HostPort = ('127.0.0.1', portNum)  # 9999初始
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket实例
        self.s.bind(self.HostPort)
        self.s.listen(5)
        self.conn, addr = self.s.accept()
        global true
        true = True
        self.addr = str(addr)
        print('Connecting by : %s ' % self.addr)

        def Receve(esc ,true):  # 将接收定义成一个函数
            while true:
                data = self.conn.recv(1024).decode('utf8')
                if data == 'quit':
                    true = False
                print("you have receve: " + data + " from" + self.addr)  # 当接收的值为'quit'时，退出接收线程，否则，循环接收并打印
                self.ui.textEdit_2.append('来自客户端: \n%s' % data)

        thrd = threading.Thread(target=Receve, args=(None, true))  # 线程实例化，target为方法，args为方法的参数
        thrd.start()  # 启动线程


