from core import get_test_app

from flask import Flask
from flask.testing import FlaskClient

import pytest

from schemas import CreateUserSchema


@pytest.fixture(scope='session')
def app() -> Flask:
    return get_test_app()


@pytest.fixture(scope='session')
def client(app: Flask) -> FlaskClient:
    return app.test_client()


@pytest.fixture(scope='class', autouse=True)
def class_client(request: pytest.FixtureRequest, client: FlaskClient) -> None:
    request.cls.client = client


@pytest.fixture(scope='session')
def create_user_schema() -> CreateUserSchema:
    return CreateUserSchema(
        email='user1@gmail.com',
        username='user1',
        password='password',
    )
