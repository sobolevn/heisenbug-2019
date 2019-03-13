# -*- coding: utf-8 -*-

"""
Flask example.

To run this app use:

    FLASK_APP=heisenbug/flask_app.py flask run

Docs: http://flask.pocoo.org/
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """
    View that will fail in production.

    How to fix it?
    The bad thing we do here is that we bind our logic and presentation.
    We need to move `1 * 0` to some other function.
    Let's call it `create_context()`.

    So, we can later test it with unit-tests, that will fail for bad mutations.
    """
    return 'Hello, world! {0} faith in you.'.format(1 * 0)


@app.errorhandler(Exception)
def log_to_sentry_and_show_sorry_page(exception):
    """
    It is almost copy-pasted from a real project.

    In reality this view sends a request to Sentry.
    And shows a beautiful page to user in case of an error.
    Because we do not want to send 500 code,
    since business says that it is bad for google search rating.
    """
    return 'Sorry, world :(', 200
