#encoding=utf-8

import tornado.ioloop
import tornado.web
import MySQLdb,sys,json
import loginHandle,apiModelHandle
sys.setdefaultencoding('utf-8')

# 登入模块
class loginHandler(tornado.web.RequestHandler):
    def post(self):
        staffEmail = self.get_argument("email")
        passwd = self.get_argument("password")
        result = loginHandle.loginModel().authenticate(staffEmail,passwd)
        if result['code'] == 1:
            data = {
            'code':1,
            'data':result[0]
            }
        else:
            data = {
            'code':result['code'],
            'data':''
            }
        self.write("%s"%str(json.dumps(data)))

# 注册模块
class registerHandler(tornado.web.RequestHandler):
    def post(self):
        staffEmail = self.get_argument("email")
        passwd = self.get_argument("password")
        name = self.get_argument("name")
        result = loginHandle.loginModel().register(staffEmail,passwd,name)
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

# 新建API模块
class createAPIHandler(tornado.web.RequestHandler):
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


#路由设置
def make_app():
    return tornado.web.Application([
        (r"/login",loginHandler),
        (r"/register",registerHandler),
        (r"/create/api",createAPIHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(18000)
    tornado.ioloop.IOLoop.current().start()
