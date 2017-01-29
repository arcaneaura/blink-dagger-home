import tornado.ioloop
import tornado.web
import os
from app import *
from app.handlers import Homepage, My404Handler
#from FileDownloader import FileDownloader


class Application(tornado.web.Application):
    def __init__(self):
        handlers = ([
        (r"/",Homepage)])
        
        
        settings = {
            "static_path": os.path.join(os.path.dirname(__file__), "app/"),
            "cookie_secret": "HoMe",
            "login_url": "/login",
            "debug": True
            }
        tornado.web.Application.__init__(self, handlers, default_handler_class=My404Handler, **settings)


if __name__=="__main__":
    app = Application()
    app.listen(80)
    print('Server has started')
    tornado.ioloop.IOLoop.current().start()