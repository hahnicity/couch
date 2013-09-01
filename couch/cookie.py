"""
couch.cookie
~~~~~~~~~~~~
"""
from flask import session
from slothpal.oauth import get_expiry_time


def make_secure_oauth_cookie(response):
    """
    Make a secure cookie for the user to validate that they currently are
    validated for PayPal transactions
    """
    return {
        "paypal_session": response,
        "expiry": get_expiry_time(response),
    }
