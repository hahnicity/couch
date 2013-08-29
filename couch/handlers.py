"""
couch.handlers
~~~~~~~~~~~~~~
"""
from tornado.web import RequestHandler, UIModule


class GetHandler(RequestHandler):
    def get(self):
        """
        Simple GET request to the server
        """
        self.render(
            "index.html",
            page_title="Greg",
            header_text="Foo",
            footer_text="Baz",
        )


class CouchUI(UIModule):
    def embedded_javascript(self):
        """
        Embed a piece of JS into our scripts
        """
        """
        <script src="https://www.paypalobjects.com/js/external/api.js"></script>
        <script>
        paypal.use( ["login"], function(login) {
              login.render ({
                      "appid": "d3428641e41208c246d07b2e5f3cc7a5",
                      "scopes": "profile email address phone https://uri.paypal.com/services/paypalattributes",
                      "containerid": "myContainer",
                      "locale": "en-us",
                      "returnurl": "http://my.domain.here/return.php"
                    });
        });
        </script>
        """


# XXX not implemented
class PostHandler(RequestHandler):
    def post(self):
        """
        Simple POST request to the server
        """
        self.set_header("Content-Type", "application/json")
        baz = self.get_argument("baz", "40")
        self.write(baz)
