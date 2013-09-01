"""
couch.thirdparty
~~~~~~~~~~~~~~~~

PayPal integration functions when slothpal wont cut it
"""
from couch.globals import paypal


def get_button_config():
    """
    Get the configuration necessary to implement a PayPal button
    """
    return {
        "client_id": paypal.id,
        "redirect_uri": paypal.redirect_uri,
        "is_sandbox": paypal.is_sandbox,
        "scopes": paypal.scopes,
    }


def get_consent_params():
    """
    Get parameters necessary to construct a PayPal consent URL
    """
    return {
        "client_id": paypal.id,
        "endpoint": paypal.endpoint,
        "redirect_uri": paypal.redirect_uri,
        "scope": paypal.scopes,
    }
