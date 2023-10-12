from core import get_test_app

from flask import Flask
from flask.testing import FlaskClient

import pytest


@pytest.fixture(scope='session')
def app() -> Flask:
    return get_test_app()


@pytest.fixture(scope='session')
def client(app: Flask) -> FlaskClient:
    return app.test_client()


@pytest.fixture(scope='class', autouse=True)
def class_client(request: pytest.FixtureRequest, client: FlaskClient) -> None:
    request.cls.client = client
