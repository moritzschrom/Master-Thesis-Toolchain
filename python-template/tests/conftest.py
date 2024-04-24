import pytest
from flask import Flask
from application import create_app
from flask.testing import FlaskClient, FlaskCliRunner

@pytest.fixture()
def app() -> Flask:
    app = create_app()
    return app

@pytest.fixture()
def client(app:Flask) -> FlaskClient:
    return app.test_client()

@pytest.fixture()
def runner(app:Flask) -> FlaskCliRunner:
    return app.test_cli_runner()
