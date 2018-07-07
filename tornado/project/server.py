import tornado.web
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
import application
import config


if __name__ == "__main__":
   server = HTTPServer(application.Application())
   server.bind(config.options["port"])
   server.start(1)
   IOLoop.current().start()

