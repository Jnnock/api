#encoding=utf-8

import sys,config,MySQLdb,time
reload(sys)
sys.setdefaultencoding('utf-8')

class ProjectSet():
    def __init__(self):
        self.library = MySQLdb.connect(host=config.getDatabaseDSN(),user=config.getDatabaseUser(),passwd=config.getDatabasePwd(),db=config.getDatabase(),port=3306,charset='utf8')
        self.cursor = self.library.cursor()

    def addProject(self,name,image,desc):
        sql = "insert into project_list (`name`,`head`,`desc`,`status`,`time`) values ('%s','%s','%s','%s','%s')"%(str())
