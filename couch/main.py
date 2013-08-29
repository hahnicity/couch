"""
couch.main
~~~~~~~~~~

CLI to start couch service
"""
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_command_line
# XXX unimplemented
#from tornado.web import StaticFileHandler

from couch.application import CouchApplication
# XXX unimplemented
#from couch.handlers import BasicHandler, PostHandler


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
    http_server = HTTPServer(CouchApplication())
    http_server.listen(options.port)
    IOLoop.instance().start()


def main():
    """
    Console script entry point
    """
    define_options()
    parse_command_line()
    start_service()
