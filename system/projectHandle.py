#encoding=utf-8

import sys,config,MySQLdb,time,os
reload(sys)
sys.setdefaultencoding('utf-8')

class ProjectSet():
    def __init__(self):
        self.library = MySQLdb.connect(host=config.getDatabaseDSN(),user=config.getDatabaseUser(),passwd=config.getDatabasePwd(),db=config.getDatabase(),port=3306,charset='utf8')
        self.cursor = self.library.cursor()

    def addProject(self,name,image,desc):
        uploadPath = "../storage/project/"
        filename = "%s+%s"%(str(time.time()),str(image[0]['filename']))
        filepath = os.path.join(uploadPath, filename)
        with open(filepath, 'wb') as up:
            up.write(image[0]['body'])
        sql = "insert into project_list (`name`,`head`,`desc`,`status`,`time`) values ('%s','%s','%s','1','%s')"%(str(name),str(filename),str(desc),str(time.time()))
        result = self.cursor.execute(sql)
        self.library.commit()
        projectID = self.library.insert_id()
        if result == 1:
            createData = {
            'code':1,
            'ID':projectID
            }
        else:
            createData = {
            'code':0,
            'ID':''
            }
        return createData
