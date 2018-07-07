import time,os
import json
import tornado.web
from tornado.web import RequestHandler
import tornado.httpclient
import tornado.gen
#from .. import config
import config

class IndexHandler(RequestHandler):
      def get(self):
          self.write("Hello, this is Jason")

class ReverseHandler(RequestHandler):
      def get(self):
          self.write("Hello, this will use reverse_url <br>")
          self.write('<a href="%s">link to init </a>' % self.reverse_url("init"))

class InitHandler(RequestHandler):
      def initialize(self,key1,key2):
          self.key1 = key1
          self.key2 = key2

      def get(self):
          self.write("Hello, this used initialize method <br>")
          self.write("key1: %s <br>" % self.key1)
          self.write("key2: %s <br>" % self.key2)


class PostFileHandler(RequestHandler):
      def get(self):
          self.render("postfile.html")

      def post(self):
          name=self.get_body_arguments("username")
          pwd=self.get_body_arguments("passwd")
          hbs=self.get_body_arguments("hobby")
          self.write("username: %s" % name)
          self.write("<br>")
          self.write("password: %s" % pwd)
          self.write("<br>")
          self.write("hobby: %s" % hbs)


class UploadHandler(RequestHandler):
      def get(self):
          self.render("upload.html")

      def post(self):
          files=self.request.files
          for file in files:
              fileArr = files[file]
              for fileObj in fileArr:
                  filePath = os.path.join(config.BASE_DIR,'upload/' + fileObj.filename)
                  with open(filePath,"wb") as f:
                       f.write(fileObj.body)
          self.write("%s" % files)

class HomeHandler(RequestHandler):
      def get(self):
          temp = 100
          person = {
                   "name":"ankala",
                   "age" : 18
          }
          self.render("home.html", num = temp, person = person)

class ChildHandler(RequestHandler):
      def get(self):
          self.render("child.html",title="child")

class StudentHandler(RequestHandler):
      def get(self):
          stus = ""
          self.render("students.html",stus=stus)

class PCookieHandler(RequestHandler):
      def get(self):
#          self.set_cookie(name,value,domain=None,expires=None,path="/",expires_days=None,**kwargs)
           self.set_cookie("cookie","Success")
           self.write("This is to setting cookie")

class GetPCookieHandler(RequestHandler):
      def get(self):
          cookie = self.get_cookie("cookie","Never login!")
          self.write("Try to get cookie")

class CookieNumHandler(RequestHandler):
      def get(self):
          count = self.get_cookie("count",None)
          if not count:
             count = 1
#          else:
#             count = int(count)
#             count += 1
#          self.set_cookie("count",str(count)) 
          self.render("cookienum.html",count=count)

class CookiePostHandler(RequestHandler):
       def get(self):
           self.render("postcookie.html")

       def post(self):
           count = self.get_cookie("count",None)
           if not count:
              count = 1
           else:
              count = int(count)
              count += 1
           self.set_cookie("count",str(count))
           self.redirect("/cookienum")

class LoginHandler(RequestHandler):
      def get(self):
         next = self.get_argument("next","/ahome")
         url = "/login?next="+next
         self.render("login.html", url=url)

      def post(self):
          name = self.get_argument("username")
          pwd =  self.get_argument("passwd")
          if name == "1" and pwd == "1":
             next = self.get_argument("next","/ahome")
             self.redirect(next+"?flag=logined")
          else:
              next = self.get_argument("next","/ahome")
              self.redirect("/login?next="+next)


class AuthHomeHandler(RequestHandler):
      def get_current_user(self):
          flag = self.get_argument("flag",None)
          return flag

      @tornado.web.authenticated
      def get(self):
          self.render("authHome.html")

      def post(self):
          self.render("authHome.html")
          

class CartHandler(RequestHandler):
      def get_current_user(self):
          flag = self.get_argument("flag",None)
          return flag

      @tornado.web.authenticated
      def get(self):
          self.render("cart.html")

      def post(self):
          self.render("cart.html")

class AsyncHandler(RequestHandler):
      def on_response(self, response):
          if response.error:
             self.send_error(500)
          else:
#              data = json.loads(response.body)
              self.write("this is from on_response <br>")
#              self.write(data)
              self.finish()

      @tornado.web.asynchronous
      def get(self):
          url= "http://opsmon.visibleworld.com/level/"
          client = tornado.httpclient.AsyncHTTPClient()
          client.fetch(url,self.on_response)
          self.write("This is from AsyncHandler! <br>")


class CoRoutineHandler(RequestHandler):
      @tornado.gen.coroutine
      def get(self):
          url= "http://opsmon.visibleworld.com/level/"
          client = tornado.httpclient.AsyncHTTPClient()
          res = yield client.fetch(url)
          if res.error:
             self.send_error(500)
          else:
             self.write("This is from CoRoutineHandler! <br>")

class CoRoutine2Handler(RequestHandler):
      @tornado.gen.coroutine
      def get(self):
          res = yield self.getData()
          self.write(res)

      @tornado.gen.coroutine
      def getData(self):
          url= "http://opsmon.visibleworld.com/level/"
          client = tornado.httpclient.AsyncHTTPClient()
          res = yield client.fetch(url)
          if res.error:
              ret = {"ret":0}
          else:
              ret = {"ret": "This is from CoRoutine2Handler! <br>"}
          raise tornado.gen.Return(ret)
          
class XStaticFileHandler(tornado.web.StaticFileHandler):
      def __init__(self,*args,**kwargs):
          super(StaticFileHandler,self).__init__(*args,**kwargs)
          self.xsrf_token          
