#encoding=utf-8

import sys,config,MySQLdb,time
reload(sys)
sys.setdefaultencoding('utf-8')

class loginModel:
    def __init__(self):
        self.library = MySQLdb.connect(host=config.getDatabaseDSN(),user=config.getDatabaseUser(),passwd=config.getDatabasePwd(),db=config.getDatabase(),port=3306,charset='utf8')
        self.cursor = self.library.cursor()

    # 0 -> 账户不存在 1 -> 成功 2-> 账户密码不正确
    def authenticate(self,email,passwd):
        sql = "select * from user_info where email = '%s'"%str(email)
        staffInfo = self.cursor.execute(sql)
        result = self.cursor.fetchone()
        if result == None:
            loginInfo = {
            'code':2,
            'data':''
            }
        if passwd == result[6]:
            loginInfo = {
            'code':1,
            'data':result[0]
            }
            update = "update `user_info` set `lasttime` = '%s' where id = '%s'"%(str(int(time.time())),str(result[0]))
            self.cursor.execute(update)
            self.library.commit()
        else:
            loginInfo = {
            'code':0,
            'data':''
            }
        return loginInfo

    # 0->注册失败（多半是服务挂掉了） 1->注册成功 2->邮箱被占用
    def register(self,email,passwd,name):
        check = "select * from user_info where email = '%s'"%str(email)
        checkResult = self.cursor.execute(check)
        if checkResult == 1:
            registerInfo = {
            'code':2,
            'data':'邮箱已注册，请<a href="login.html">登入</a>'
            }
        else:
            sql = "insert user_info (`email`,`passwd`,`name`,`time`,`status`) values('%s','%s','%s','%s','1')"%(str(email),str(passwd),str(name),str(time.time()))
            result = self.cursor.execute(sql)
            self.library.commit()
            lastID = self.library.insert_id()
            if result == 1:
                registerInfo = {
                'code':1,
                'data':lastID
                }
            else:
                registerInfo = {
                'code':0,
                'data':'注册失败'
                }
        return registerInfo
