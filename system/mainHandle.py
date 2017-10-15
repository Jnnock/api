#encoding=utf-8

import tornado.ioloop
import tornado.web
import MySQLdb,sys,json,loginHandle
reload(sys)
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


class registerHandler(tornado.web.RequestHandler):
    def post(self):
        staffEmail = self.get_argument("email")
        passwd = self.get_argument("password")
        name = self.get_argument("name")
        result = loginHandle.loginModel().register(staffEmail,passwd,name)
        print result
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
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(18000)
    tornado.ioloop.IOLoop.current().start()
