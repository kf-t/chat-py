import pymysql
import time  # 导入time模块
import socket
import datetime


class loginLogic(object):
    def __int__(self):
        super(loginLogic, self).__init__()
        self.init_con()
        self.checklogin()

    def init_con(self):
        # 创建数据库连接
        self.conn = pymysql.connect(
            host='127.0.0.1',  # 连接主机, 默认127.0.0.1
            user='root',  # 用户名
            passwd='root',  # 密码
            port=3306,  # 端口，默认为3306
            db='chat',  # 数据库名称
            charset='utf8'  # 字符编码
        )
        # 生成游标对象 cursor
        self.cursor = self.conn.cursor()

    def getLoginInfo(self):
        self.init_con()
        sql = "SELECT * FROM login_info"  # 注意：需要检索的值要用单引号，不能用双引号
        try:
            self.cursor.execute(sql)  # 执行sql语句
            self.loginInfo = self.cursor.fetchall()  # 查询所有记录
            for i in self.loginInfo:
                print(i)  # 打印每条数据
        except:
            print('查询失败')

    def checklogin(self, username=None, password=None):
        self.init_con()
        self.username = username
        self.password = password
        if (self.username and self.password) == None or (self.username and self.password) == '':
            self.msg = "请输入账号或密码"
            self.loginState = 0
            print(self.msg)
        else:
            self.loginState = 0
            # 查询指定条件的数据
            sql = "SELECT COUNT(*) FROM user WHERE username= '%s' " % (self.username)
            self.cursor.execute(sql)  # 返回值是查询到的数据数量
            self.username_state = self.cursor.fetchone()
            if self.username_state[0]:  # 有这个用户
                # 先看有没有被封
                sql = "SELECT forbi_end_time FROM user WHERE username = '%s' " % (self.username)
                self.cursor.execute(sql)  # 返回值是查询到的数据数量
                forbi_end_time = self.cursor.fetchone()[0]
                sql = "SELECT forbidden FROM user WHERE username = '%s' " % (self.username)
                self.cursor.execute(sql)  # 返回值是查询到的数据数量
                forbidden = self.cursor.fetchone()[0]
                if forbi_end_time != None and forbidden == 1:
                    # 日期格式话模版
                    format_pattern = "%Y-%m-%d %H:%M:%S"
                    nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    nowTime = nowTime.replace('-', '')
                    nowTime = nowTime.replace(':', '')
                    nowTime = nowTime.replace(' ', '')
                    forbi_end_time_former_format = forbi_end_time
                    forbi_end_time = forbi_end_time.replace('-', '')
                    forbi_end_time = forbi_end_time.replace(':', '')
                    forbi_end_time = forbi_end_time.replace(' ', '')
                    difference = int(forbi_end_time) - int(nowTime)
                    if difference > 0:
                        print("持续封禁中...")
                        self.msg = "封禁至:%s" % forbi_end_time_former_format
                    else:
                        print("解封")
                        # 封禁状态和时间归零(时间并未设置为NULL，而是拿当前时间)
                        sql0 = "UPDATE user SET forbi_end_time = '%s' WHERE username = '%s' " % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), self.username)
                        sql1 = "UPDATE user SET login_fail = '%d' WHERE username = '%s' " % (0, self.username)
                        sql2 = "UPDATE user SET forbidden = '%d' WHERE username = '%s' " % (0, self.username)
                        self.cursor.execute(sql0)
                        self.conn.commit()  # 提交到数据库
                        self.cursor.execute(sql1)
                        self.conn.commit()  # 提交到数据库
                        self.cursor.execute(sql2)
                        self.conn.commit()  # 提交到数据库
                else:
                    # 没封的情况↓
                    sql = "SELECT COUNT(*) FROM user WHERE password = '%s' " % (self.password)
                    self.cursor.execute(sql)  # 返回值是查询到的数据数量
                    self.password_state = self.cursor.fetchone()
                    if self.password_state[0]:
                        self.msg = "登录成功"
                        self.loginState = 1
                        # 登录成功则将登录信息插入数据库
                        try:
                            ip = socket.gethostbyname(socket.gethostname())
                            temp_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                            sql = "INSERT INTO login_info(username, login_time, userip, password) VALUES('%s', '%s', '%s', '%s')" % (self.username, temp_time, ip, self.password)
                            self.cursor.execute(sql)
                            self.conn.commit()  # 提交到数据库
                            print("插入登录信息成功")
                        except pymysql.Error as e:
                            print(e.args[0], e.args[1])
                            print("插入登录信息失败")
                    else:
                        self.msg = "密码错误"
                        sql = "SELECT login_fail FROM user where username= '%s'" % (self.username)  # 注意：需要检索的值要用单引号，不能用双引号
                        try:
                            self.cursor.execute(sql)  # 执行sql语句
                            self.results = self.cursor.fetchall()  # 查询所有记录
                            print(self.results[0][0])  # 打印每条数据
                        except:
                            print('查询失败')
                        if self.results[0][0] == 3:
                            self.msg = "封禁"
                            now = datetime.datetime.now()
                            date = now + datetime.timedelta(days=1)
                            forbiDate = date.strftime('%Y-%m-%d %H:%M:%S')
                            sql = "UPDATE user SET forbidden = '%d' WHERE username = '%s' " % (1, self.username)
                            sql1 = "UPDATE user SET forbi_end_time = '%s' WHERE username = '%s' " % (forbiDate, self.username)
                            try:
                                self.cursor.execute(sql)  # 执行sql语句
                                self.conn.commit()  # 提交到数据库
                                self.cursor.execute(sql1)
                                self.conn.commit()  # 提交到数据库
                                self.msg = "封禁至：%s" % forbiDate
                            except:
                                print('封禁操作失败')
                        else:
                            tempNum = self.results[0][0] + 1
                            sql = "UPDATE user SET login_fail = '%d' WHERE username = '%s' " % (tempNum, self.username)
                            try:
                                self.cursor.execute(sql)  # 执行sql语句
                                self.conn.commit()  # 提交到数据库
                            except:
                                print('修改失败次数失败')
            else:
                self.msg = "用户名不存在"
            # print(self.msg)
        self.cursor.close()  # 关闭游标
        self.conn.close()  # 关闭连接
        return self.msg, self.loginState

