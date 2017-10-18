#encoding=utf-8

import sys,config,MySQLdb,time,os,config
reload(sys)
sys.setdefaultencoding('utf-8')

class ProjectSet():
    def __init__(self):
        self.library = MySQLdb.connect(host=config.getDatabaseDSN(),user=config.getDatabaseUser(),passwd=config.getDatabasePwd(),db=config.getDatabase(),port=3306,charset='utf8')
        self.cursor = self.library.cursor()

    def addProject(self,name,image,desc,user):
        uploadPath = "../storage/project/"
        filename = "%s+%s"%(str(time.time()),str(image[0]['filename']))
        filepath = os.path.join(uploadPath, filename)
        with open(filepath, 'wb') as up:
            up.write(image[0]['body'])
        sql = "insert into project_list (`name`,`head`,`desc`,`status`,`time`,`create_id`) values ('%s','%s','%s','1','%s','%s')"%(str(name),str(filename),str(desc),str(time.time()),str(user))
        result = self.cursor.execute(sql)
        projectID = self.library.insert_id()
        self.library.commit()
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

    def getProjectsByUser(self,user,type):
        sql = "select * from `project_list` where create_id = '%s' and `status` = 1"%str(user)
        result = self.cursor.execute(sql)
        if result > 0:
            projects = self.cursor.fetchmany(result)
            data = []
            for i in projects:
                if len(i[2]) == 0:
                    image = 'http://ooe5frhzu.bkt.clouddn.com/1398738960.76.jpg'
                else:
                    image = "%s/storage/project/%s"%(str(config.getUrl()),str(i[2]))
                project = {
                'pid':i[0],
                'name':i[1],
                'image':image,
                'desc':i[3]
                }
                data.append(project)
            projectsInfo = {
            'code':1,
            'data':data
            }
        else:
            projectsInfo = {
            'code':0,
            'data':''
            }
        return projectsInfo
