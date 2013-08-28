"""
couch.main
~~~~~~~~~~

CLI to start couch service
"""
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_command_line
from tornado.web import Application, StaticFileHandler

from couch.handlers import BasicHandler, PostHandler


def define_options():
    """
    Define all options for running our tornado server
    """
    # XXX More to come
    define("port", default=8888, help="The port we want to run on", type=int)


def start_service():
    """
    Initialize the webapp
    """
    app = Application([
        (r"/favicon.ico", StaticFileHandler, {"path": "/var/www/media/images/favicon.ico"}),
        (r"/", BasicHandler),
        (r"/post", PostHandler)
    ])
    app.listen(options.port)
    IOLoop.instance().start()


def main():
    """
    Console script entry point
    """
    define_options()
    parse_command_line()
    start_service()
