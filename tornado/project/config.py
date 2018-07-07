import os

BASE_DIR = os.path.dirname(__file__)

options = {
        "port" :9000,
}

mysql = {
      "host": "IP",
      "user": "root",
      "passwd": "pwd",
      "dbName": "study"
}

settings = {
         "static_path":os.path.join(BASE_DIR,"static"),
         "template_path" : os.path.join(BASE_DIR,"templates"),
         "debug" : True,
         "xsrf_cookies":True,
         "login_url": "/login",
}
