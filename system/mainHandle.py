#encoding=utf-8

import tornado.ioloop
import tornado.web
import MySQLdb,sys,json,loginHandle
reload(sys)
sys.setdefaultencoding('utf-8')

# 登入模块
class loginHandler(tornado.web.RequestHandler):
    def get(self):
        staffEmail = self.get_argument("email")
        passwd = self.get_argument("password")
        print loginHandle.loginModel().authenticate(staffEmail,passwd)

#路由设置
def make_app():
    return tornado.web.Application([

        (r"/login",loginHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
