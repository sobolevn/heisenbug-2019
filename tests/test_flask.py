# -*- coding: utf-8 -*

import pytest
from flask import url_for

from heisenbug.flask_app import app, log_to_sentry_and_show_sorry_page


@pytest.fixture
def flask_client():
    """Testing client for flask apps."""
    app.config['TESTING'] = True
    app.config['SERVER_NAME'] = 'localhost'
    client = app.test_client()

    with app.app_context():
        yield client


def test_hello_view(flask_client):
    """This is a regular integration test, that really tests nothing."""
    url = url_for('hello', index=0)
    response = flask_client.get(url)

    assert response.status_code == 200
    assert b'world' in response.data
    assert b'0' in response.data


def test_error_handler():
    """We can also find this kind of test somewhere in the codebase."""
    error_text, code = log_to_sentry_and_show_sorry_page(TypeError())

    assert isinstance(error_text, str)
    assert isinstance(code, int)
