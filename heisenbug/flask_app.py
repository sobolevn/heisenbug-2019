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
    """View that will fail in production."""
    return 'Hello, world! {0} faith in you.'.format(1 * 0)


@app.errorhandler(Exception)
def log_to_sentry_and_show_sorry_page(exception):
    """
    It is almost copy-pasted from a real project.

    In reality this view sends a request to Sentry.
    And shows a beautiful page to user in case of an error.
    """
    return 'Sorry, world :(', 200
