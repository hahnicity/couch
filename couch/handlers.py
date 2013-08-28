"""
couch.handlers
~~~~~~~~~~~~~~
"""
from tornado.web import RequestHandler


class BasicHandler(RequestHandler):
    def get(self):
        self.write("Congrats on your first web server!")
