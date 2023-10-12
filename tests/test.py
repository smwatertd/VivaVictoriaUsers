from abc import ABC
from flask.testing import FlaskClient


class TestCase(ABC):
    client: FlaskClient
