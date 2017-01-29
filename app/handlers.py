# -*- coding: utf-8 -*-
from app import *
import pymongo
import json
import subprocess
import datetime
import time

class Homepage(BaseHandler):
    def get(self):
        #if self.auth_check():
        self.render('templates/homepage.html')

class My404Handler(BaseHandler):
    # Override prepare() instead of get() to cover all possible HTTP methods.
    def prepare(self):
        self.set_status(404)
        self.render('templates/error.html', code = '404')



