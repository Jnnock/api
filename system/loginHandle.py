#encoding=utf-8

import sys,config,MySQLdb,hashlib
reload(sys)
sys.setdefaultencoding('utf-8')

class loginModel:
    def __init__(self):
        self.library = MySQLdb.connect(host=config.getDatabaseDSN(),user=config.getDatabaseUser(),passwd=config.getDatabasePwd(),db=config.getDatabase(),port=3306,charset='utf8')
        self.cursor = self.library.cursor()

    def authenticate(self,email,passwd):
        encode = hashlib.md5()
        m = encode.update("password")
        print m
        print passwd
        print m.hexdigest()
        sql = "select * from user_info where email = '%s'"%str(email)
        staffInfo = self.cursor.execute(sql)
        result = self.cursor.fetchone()
        if result == None:
            return 2
