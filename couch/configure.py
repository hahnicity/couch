"""
couch.configure
~~~~~~~~~~~~~~~
"""
from os import urandom

from slothpal.oauth import OAuth

from couch import constants
# XXX DEBUG obviously
from couch import credentials
from couch.controllers import create_routes
from couch.globals import paypal


def configure_app(app, args, oauth):
    """
    Configure the application's behavior
    """
    app.debug = args.debug
    app.testing = args.testing
    app.secret_key = urandom(64)
    app.config["HOST"] = get_host(args)
    app.config["APPLICATION_ROOT"] = get_app_url(args)

    # Create all application controllers
    create_routes(app, oauth)


def configure_paypal(args):
    """
    Construct PayPal specific configuration
    """
    return {
        "id": get_app_id(args),
        "is_sandbox": args.sandbox,
        "redirect_uri": get_redirect_uri(args),
        "scopes": constants.SCOPES,
    }


def get_auth_credentials(args):
    """
    Get necessary PayPal authentication credentials
    """
    return {
        True: credentials.SANDBOX,
        False: credentials.LIVE,
    }[args.sandbox]


def get_app_id(args):
    """
    Get the application id for the PayPal app
    """
    return get_auth_credentials(args)[0]


def get_app_secret(args):
    """
    Get the application secret for the PayPal app
    """
    return get_auth_credentials(args)[1]


def get_app_url(args):
    """
    Get the base url for the app
    """
    return {
        True: constants.SANDBOX_APP_URL,
        False: constants.LIVE_APP_URL,
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


def get_redirect_uri(args):
    """
    Get the application's redirect uri for PayPal
    """
    return {
        True: constants.SANDBOX_REDIRECT,
        False: constants.LIVE_REDIRECT,
    }[args.sandbox]


def make_oauth(args):
    """
    Configure initial oauth and get a token
    """
    oauth = OAuth(paypal["endpoint"], get_app_id(args), get_app_secret(args))
    oauth.request_token()
    return oauth
