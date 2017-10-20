#encoding=utf-8

import sys,config,MySQLdb,time,os,config
reload(sys)
sys.setdefaultencoding('utf-8')

class UserSet():
    def __init__(self):
        self.library = MySQLdb.connect(host=config.getDatabaseDSN(),user=config.getDatabaseUser(),passwd=config.getDatabasePwd(),db=config.getDatabase(),port=3306,charset='utf8')
        self.cursor = self.library.cursor()

    def getUserInfo(self,userid):
        sql = "select * from `user_info` where id = '%s' and `status` = 1"%str(userid)
        result = self.cursor.execute(sql)
        userInfo = self.cursor.fetchone()
        if userInfo[2] > 0:
            image = "%s/storage/user/%s"%(str(config.getUrl()),str(userInfo[2]))
        else:
            image = "http://ooe5frhzu.bkt.clouddn.com/avatar04.png"
        regTime = time.strftime("%Y-%m-%d", time.localtime(userInfo[5]))
        data = {
            'code':1,
            'data':{
                'name':userInfo[1],
                'image':image,
                'regTime':regTime
            }
        }
        return data
