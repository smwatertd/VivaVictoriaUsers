from typing import Generator
from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture(scope='function')
def create_user_service() -> Generator[MagicMock, None, None]:
    with patch('services.create_user_service.CreateUserService.__call__', new=MagicMock(return_value=None)) as mock:
        yield mock
