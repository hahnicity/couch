"""
couch.handlers
~~~~~~~~~~~~~~
"""
from tornado.web import RequestHandler


class BasicHandler(RequestHandler):
    def get(self):
        self.write("Congrats on your first web server!")


class PostHandler(RequestHandler):
    def post(self):
        self.set_header("Content-Type", "application/json")
        baz = self.get_argument("baz", "40")
        self.write(baz)
