"""
couch.configure
~~~~~~~~~~~~~~~
"""
from slothpal.oauth import OAuth

from couch import constants
# XXX DEBUG obviously
from couch import credentials
from couch.controllers import create_routes


def configure_app(app, args, oauth):
    """
    Configure the application's behavior
    """
    app.debug = args.debug
    app.testing = args.testing

    # Create all application controllers
    create_routes(app, oauth)


def get_auth_credentials(args):
    """
    Get necessary PayPal authentication credentials
    """
    return {
        True: credentials.SANDBOX,
        False: credentials.LIVE,
    }[args.sandbox]


def get_host(args):
    """
    Configure the host string to run our app on
    """
    if args.host:
        return args.host
    else:
        return {
            True: "127.0.0.1",
            False: "0.0.0.0"
        }[args.local]


def get_oauth(args):
    """
    Configure initial oauth and get a token
    """
    endpoint = get_url_endpoint(args)
    auth = get_auth_credentials(args)
    oauth = OAuth(endpoint, auth[0], auth[1])
    oauth.request_token()
    return oauth


def get_url_endpoint(args):
    """
    Get the PayPal URL endpoint
    """
    return {
        True: constants.SANDBOX_ENDPOINT,
        False: constants.LIVE_ENDPOINT,
    }[args.sandbox]
