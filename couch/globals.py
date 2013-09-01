"""
couch.globals
~~~~~~~~~~~~~
"""
from peak.util.proxies import CallbackProxy
from slothpal.context import context

# Serves as a global paypal configuration object for the app
paypal = CallbackProxy(lambda: context["paypal"])
