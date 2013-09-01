"""
couch.defaults
~~~~~~~~~~~~~~
"""
## App URLs
LIVE_APP_URL =  "http://192.168.1.133:5000/"  # "http://echo-couch-app.herokuapp.com/"
SANDBOX_APP_URL = "http://192.168.1.133:5000/"

LIVE_REDIRECT = "http://192.168.1.133:5000/"
SANDBOX_REDIRECT = "http://192.168.1.133:5000/"

# XXX See if you can find an abstraction for this from the initial token request
## Couch-PayPal Interface
SCOPES = "openid email"
