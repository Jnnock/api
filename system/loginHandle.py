#encoding=utf-8

import sys,config,MySQLdb,time
reload(sys)
sys.setdefaultencoding('utf-8')

class loginModel:
    def __init__(self):
        self.library = MySQLdb.connect(host=config.getDatabaseDSN(),user=config.getDatabaseUser(),passwd=config.getDatabasePwd(),db=config.getDatabase(),port=3306,charset='utf8')
        self.cursor = self.library.cursor()

    def authenticate(self,email,passwd):
        sql = "select * from user_info where email = '%s'"%str(email)
        staffInfo = self.cursor.execute(sql)
        result = self.cursor.fetchone()
        if result == None:
            loginInfo = {
            'code':2,
            'data':''
            }
        if passwd == result[7]:
            loginInfo = {
            'code':1,
            'data':result
            }
        else:
            loginInfo = {
            'code':0,
            'data':result
            }
        return loginInfo

    def register(self,email,passwd,name):
        sql = "insert user_info (`email`,`passwd`,`name`,`time`,`status`) values('%s','%s','%s','%s','1')"%(str(email),str(passwd),str(name),str(time.time()))
        result = self.cursor.execute(sql)
        lastID = self.library.insert_id()
        if result:
            registerInfo = {
            'code':1,
            'ID':lastID
            }
        else:
            registerInfo = {
            'code':0,
            'ID':''
            }
        return registerInfo
