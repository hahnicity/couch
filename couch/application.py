"""
couch.application
~~~~~~~~~~~~~~~~~
"""
from os.path import abspath, dirname

from tornado.web import Application, StaticFileHandler

from couch import static, templates
from couch.handlers import GetHandler


class CouchApplication(Application):
    def __init__(self):
        handlers = [
            (r"/", GetHandler),
            (r"/favicon.ico", StaticFileHandler),
        ]
        settings = dict(
            template_path=abspath(dirname(templates.__file__)),
            static_path=abspath(dirname(static.__file__)),
            debug=True,
            autoescape=None,
        )
        super(CouchApplication, self).__init__(handlers, **settings)
