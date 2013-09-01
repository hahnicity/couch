"""
couch.controllers
~~~~~~~~~~~~~~~~~
"""
from flask import redirect, render_template, request, session
from slothpal.oauth import get_expiry_time, make_consent_url

from couch.thirdparty import get_button_config, get_consent_params


def create_routes(app, oauth):
    @app.route("/agreement", methods=["GET"])
    def user_agreement():
        """
        Make a GET request to the user agreement page
        """
        return "Do you agree?"

    @app.route("/privacy", methods=["GET"])
    def privacy_policy():
        """
        Make a GET request to the privacy page
        """
        return "Privacy"

    @app.route("/donatenow", methods=["GET"])
    def donate_now():
        """
        Page where customers can begin the donation process
        """
        if "token" not in session:
            redirect(make_consent_url(get_consent_params()))
            # XXX Do some redirect magic to paypal oauth
            pass

        return "Donations"

    @app.route("/", methods=["GET"])
    def homepage():
        """
        Make a GET request to the homepage. This function makes the
        assumption it is the redirect URL
        """
        if request.args.get("scope") and request.args.get("code"):
            _generate_session()

        button_config = get_button_config()
        return render_template("index.html", button_config=button_config)

    def _generate_session():
        """
        Handle the case when a user is redirected from PayPal back to the
        homepage
        """
        if "token" not in session:
            # XXX There will need to be error handling for bad responses
            access_response = oauth.exchange_auth_code(request.args.get("code"))
            cookie = {
                "session": access_response,
                "expiry": get_expiry_time(access_response)
            }
            session["token"] = cookie
