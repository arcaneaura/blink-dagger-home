import configparser
import pymongo
import os
import tornado

class BaseHandler(tornado.web.RequestHandler):
    #auth is not required now.

    def get_current_user(self):
        return self.get_secure_cookie("user")
        
    def auth_check(self):
        self.remote_ip = self.request.remote_ip if not self.request.headers.get("X-Real-IP") else self.request.headers.get("X-Real-IP")
        try:
            #ipcheck = creds.get("BLACK_IP", self.remote_ip)
            if self.get_secure_cookie("user"):                
                return True               
            else:                
                self.redirect(r"/login")
        
        except configparser.NoOptionError:
            self.write("Your IP is BLACKLISTED Hahaha!")