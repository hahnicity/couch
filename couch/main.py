"""
couch.main
~~~~~~~~~~
"""
from argparse import ArgumentParser

from couch.app import create_app
from couch.configure import configure_app, get_host, get_oauth


def parse_argv():
    """
    Parse all command line arguments
    """
    parser = ArgumentParser()
    add_app_arguments(parser)
    add_paypal_arguments(parser)
    add_other_arguments(parser)
    return parser.parse_args()


def add_app_arguments(parser):
    """
    Add arguments for where the app will be run
    """
    parser.add_argument("--port", help="The port to listen on", type=int)
    hosts = parser.add_mutually_exclusive_group()
    hosts.add_argument("--local", help="Launch the app on 127.0.0.1", action="store_true")
    hosts.add_argument("--host", help="Launch the app on a specific host eg: 1.1.1.1")


def add_paypal_arguments(parser):
    """
    Add PayPal specific arguments
    """
    parser.add_argument("--sandbox", help="Enable this to point to the sandbox", action="store_true")
    # XXX I imagine more to come


def add_other_arguments(parser):
    """
    Add other arguments
    """
    others = parser.add_argument_group("Other Options")
    others.add_argument(
        "--debug",
        help="Enable exception logging and reload the app if the source changes",
        action="store_true",
    )
    others.add_argument(
        "--testing",
        help="Enable exception logging and usage of mocks for configuration functions",
        action="store_true",
    )


def main():
    """
    Console Entry point
    """
    args = parse_argv()
    app = create_app()
    oauth = get_oauth(args)
    configure_app(app, args, oauth)
    app.run(host=get_host(args), port=args.port)
