#encoding=utf-8

import tornado.ioloop
import tornado.web
import MySQLdb,sys,json,os
import loginHandle,apiModelHandle,projectHandle
sys.setdefaultencoding('utf-8')

# 登入模块
class loginHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')

    def post(self):
        result = loginHandle.loginModel().authenticate(self.get_argument("email"),self.get_argument("password"))
        self.write("%s"%str(json.dumps(result)))

# 注册模块
class registerHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')

    def post(self):
        result = loginHandle.loginModel().register(self.get_argument("email"),self.get_argument("password"),self.get_argument("name"))
        self.write("%s"%str(json.dumps(result)))

# 新建API模块
class createAPIHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')

    def post(self):
        argvNum = self.get_argument("number")
        callback = self.get_argument("callback")
        title = self.get_argument("title")
        desc = self.get_argument("desc")
        create_id = self.get_argument("user")
        link = self.get_argument("link")
        result = apiModelHandle.ApiSet().newApi(argvNum,link,callback,title,desc,create_id)
        if result['code'] == 1:
            data = {
            'code':1,
            'data':result['ID']
            }
        else:
            data = {
            'code':result['code'],
            'data':''
            }
        self.write("%s"%str(json.dumps(data)))

# 更新API模块
class editAPIHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')

    def post(self):
        argvNum = self.get_argument("number")
        callback = self.get_argument("callback")
        title = self.get_argument("title")
        desc = self.get_argument("desc")
        create_id = self.get_argument("user")
        link = self.get_argument("link")
        result = apiModelHandle.ApiSet().editApi(apiId,argvNum,link,callback,title,desc)
        if result['code'] == 1:
            data = {
            'code':1,
            'data':result['ID']
            }
        else:
            data = {
            'code':result['code'],
            'data':''
            }
        self.write("%s"%str(json.dumps(data)))

# 创建项目模块
class createProjectHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')

    def post(self):
        result = projectHandle.ProjectSet().addProject(self.get_argument("name"),self.request.files.get("image"),self.get_argument("desc"),self.get_argument("user"))
        if result['code'] == 1:
            data = {
            'code':1,
            'data':result['ID']
            }
        else:
            data = {
            'code':result['code'],
            'data':''
            }
        self.write("%s"%str(json.dumps(data)))

# 获取我的项目模块
class getProjectHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')

    def get(self):
        result = projectHandle.ProjectSet().getProjectsByUser(self.get_argument("user"),self.get_argument("type"))
        self.write("%s"%str(json.dumps(result)))

#路由设置
def make_app():
    return tornado.web.Application([
        (r"/login",loginHandler),
        (r"/register",registerHandler),
        (r"/create/api",createAPIHandler),
        (r"/create/project",createProjectHandler),
        (r"/get/projects",getProjectHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(18000)
    tornado.ioloop.IOLoop.current().start()
