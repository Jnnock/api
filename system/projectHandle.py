#encoding=utf-8

import sys,config,MySQLdb,time,os,config
reload(sys)
sys.setdefaultencoding('utf-8')

class ProjectSet():
    def __init__(self):
        self.library = MySQLdb.connect(host=config.getDatabaseDSN(),user=config.getDatabaseUser(),passwd=config.getDatabasePwd(),db=config.getDatabase(),port=3306,charset='utf8')
        self.cursor = self.library.cursor()

    # 添加项目
    def addProject(self,name,image,desc,user):
        uploadPath = "../storage/project/"
        filename = "%s+%s"%(str(time.time()),str(image[0]['filename']))
        filepath = os.path.join(uploadPath, filename)
        with open(filepath, 'wb') as up:
            up.write(image[0]['body'])
        sql = "insert into project_list (`name`,`head`,`desc`,`status`,`time`,`create_id`) values ('%s','%s','%s','1','%s','%s')"%(str(name),str(filename),str(desc),str(time.time()),str(user))
        result = self.cursor.execute(sql)
        projectID = self.library.insert_id()
        relation = "insert into project_user_relation (`project_id`,`user_id`,`status`,`relation`,`time`) values ('%s','%s','1','1','%s')"%(str(projectID),str(user),str(int(time.time())))
        self.cursor.execute(relation)
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

    # 获取用户创建的项目
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

    # 添加项目模块
    def addProjectModel(self,name,desc,project):
        sql = "insert into project_model (`project_id`,`name`,`desc`,`status`,`time`) value ('%s','%s','%s','1','%s')"%(str(project),str(name),str(desc),str(int(time.time())))
        result = self.cursor.execute(sql)
        modelID = self.library.insert_id()
        self.library.commit()
        if result == 1:
            createData = {
                'code':1,
                'data':modelID
            }
        else:
            createData = {
                'code':0,
                'data':''
            }
        return createData

    # 获取项目模块
    def getProjectModels(self,project):
        sql = "select * from project_model where `project_id` = '%s' and `status` = 1"%str(project)
        result = self.cursor.execute(sql)
        if result > 0:
            modelsInfo = self.cursor.fetchmany(result)
            data = []
            for i in modelsInfo:
                model = {
                    'name':i[2],
                    'desc':i[3],
                    'id':i[0]
                }
                data.append(model)
            info = {
                'code':1,
                'data':data
            }
        else:
            info = {
                'code':0,
                'data':''
            }
        return info

    # 获取项目模块
    def getProject(self,project):
        sql = "select * from project_list where `id` = '%s' and `status` = 1"%str(project)
        result = self.cursor.execute(sql)
        if result > 0:
            project = self.cursor.fetchone()
            if len(project[2]) == 0:
                image = 'http://ooe5frhzu.bkt.clouddn.com/1398738960.76.jpg'
            else:
                image = "%s/storage/project/%s"%(str(config.getUrl()),str(project[2]))
            info = {
                'code':1,
                'data':{
                    'name':project[1],
                    'desc':project[3],
                    'image':image,
                }
            }
        else:
            info = {
                'code':0,
                'data':''
            }
        return info
