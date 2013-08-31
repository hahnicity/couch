"""
couch.controllers
~~~~~~~~~~~~~~~~~
"""
from flask import render_template

from couch import constants


def create_routes(app, oauth):
    @app.route("/agreement")
    def user_agreement():
        """
        Make a GET request to the user agreement page
        """
        return "Do you agree?"

    @app.route("/privacy")
    def privacy_policy():
        """
        Make a GET request to the privacy page
        """
        return "Privacy"

    @app.route("/")
    def homepage():
        """
        Make a GET request to the homepage
        """
        # XXX Remove ID after debug
        app = {"id": "AU3saBBLmtcRB-gglYmD1EDlrB53feI0NxE2JGWdY0_ppX-22dulztl63PYK"}
        # XXX We should not be getting the URL value from constants here
        return render_template("index.html", app=app, base_url=constants.APP_URL)
