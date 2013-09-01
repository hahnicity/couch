"""
couch.controllers
~~~~~~~~~~~~~~~~~
"""
from flask import render_template, request, session

from couch import constants


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

    @app.route("/", methods=["GET"])
    def homepage():
        """
        Make a GET request to the homepage. This function makes the
        assumption it is the defacto redirect URL
        """
        if request.args.get("scope") and request.args.get("code"):
            _generate_session()

        print "token" in session
        # XXX This will likely need to be abstracted
        homepage_config = {
            "client_id": oauth.id,
            "base_url": app.config["APPLICATION_ROOT"],
            "is_sandbox": app.config["IS_SANDBOX"],
            "scopes": constants.SCOPES
        }
        return render_template("index.html", homepage_config=homepage_config)

    def _generate_session():
        """
        Handle the case when a user is redirected from PayPal back to the
        homepage
        """
        if "token" not in session:
            # XXX There will need to be error handling for bad responses
            access_response = oauth.exchange_auth_code(request.args.get("code"))
            session["token"] = access_response
