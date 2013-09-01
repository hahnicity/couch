"""
couch.controllers
~~~~~~~~~~~~~~~~~
"""
from time import time

from flask import redirect, render_template, request, session
from slothpal.exceptions import StatusCodeError
from slothpal.oauth import make_consent_url

from couch.cookie import make_secure_oauth_cookie
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
            return redirect(make_consent_url(**get_consent_params()))
        else:
            _check_if_token_expired()

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

    def _check_if_token_expired():
        """
        Check to see if the user's bearer token is expired. If it is attempt
        to get a new token.
        """
        if session["token"]["expiry"] < time():
            _handle_expired_tokens()

    def _handle_expired_tokens():
        """
        Attempt to obtain a new token using the refresh token. It that doesn't
        work, re-direct the user to the PayPal login
        """
        try:
            response = oauth.use_refresh_token(
                session["token"]["paypal_session"]["refresh_token"]
            )
        except StatusCodeError:
            redirect(make_consent_url(**get_consent_params()))
        else:
            session["token"] = make_secure_oauth_cookie(response)

    def _generate_session():
        """
        Handle the case when a user is redirected from PayPal back to the
        homepage
        """
        if "token" not in session:
            # XXX There will need to be error handling for bad responses
            response = oauth.exchange_auth_code(request.args.get("code"))
            session["token"] = make_secure_oauth_cookie(response)
