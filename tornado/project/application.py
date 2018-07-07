import tornado.web
import config
import os
from views import index

class Application(tornado.web.Application):
      def __init__(self):
          handlers = [
#                    (r'/',index.IndexHandler),
                    (r'/postfile',index.PostFileHandler),
                    (r"/home",index.HomeHandler),
                    (r"/ahome",index.AuthHomeHandler),
                    (r"/login",index.LoginHandler),
                    (r"/cart",index.CartHandler),
                    (r"/child",index.ChildHandler),
                    (r"/pcookie",index.PCookieHandler),
                    (r"/gcookie",index.GetPCookieHandler),
                    (r"/cookienum",index.CookieNumHandler),
                    (r"/postcookie",index.CookiePostHandler),
                    (r"/async",index.AsyncHandler),
                    (r"/coroutine",index.CoRoutineHandler),
                    (r"/coroutine2",index.CoRoutine2Handler),
                    (r"/reverse",index.ReverseHandler),
                    tornado.web.url(r"/init", index.InitHandler,{"key1":"nice","key2":"good"},name="init"),
                    (r"/upload",index.UploadHandler),
                    (r"/(.*)$", tornado.web.StaticFileHandler, {"path":os.path.join(config.BASE_DIR,"static/html"),"default_filename":"index.html"}),
          ]
          super(Application,self).__init__(handlers,**config.settings)
