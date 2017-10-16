#encoding=utf-8

import sys,config,MySQLdb,time
reload(sys)
sys.setdefaultencoding('utf-8')

class ApiSet():
    def __init__(self):
        self.library = MySQLdb.connect(host=config.getDatabaseDSN(),user=config.getDatabaseUser(),passwd=config.getDatabasePwd(),db=config.getDatabase(),port=3306,charset='utf8')
        self.cursor = self.library.cursor()

    def newApi(self,paramNums,api,callback,title,desc,create_id):
        sql = "insert into `api_info` (`name`,`desc`,`return`,`status`,`time`,`create_id`,`api`) values ('%s','%s','%s','1','%s','%s','%s')"%(str(title),str(desc),str(callback),str(time.time()),str(create_id),str(api))
        result = self.cursor.execute(sql)
        self.library.commit()
        lastID = self.library.insert_id()
        if result:
            apiInfo = {
            'code':1,
            'ID':lastID
            }
        else:
            apiInfo = {
            'code':0,
            'ID':''
            }
        return apiInfo

    def editApi(self,apiId,argvNum,link,callback,title,desc):
        sql = "update `api_info` set `name`='%s',`desc`='%s',`return`='%s',`last`='%s',`api`='%s' where id = '%s'"%(str(title),str(desc),str(callback),str(time.time()),str(api),str(apiId))
        result = self.cursor.execute(sql)
        self.library.commit()
        if result:
            apiInfo = {
            'code':1,
            'ID':apiId,
            }
        else:
            apiInfo = {
            'code':0,
            'ID':''
            }
        return apiInfo

    def deleteApi(self,apiId):
        sql = "update `api_info` set `status`='0' where id = '%s'"%str(apiId)
        result = self.cursor.execute(sql)
        self.library.commit()
        if result:
            apiInfo = {
            'code':1,
            }
        else:
            apiInfo = {
            'code':0,
            }
        return apiInfo
