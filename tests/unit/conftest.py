from typing import Generator
from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture(scope='function', autouse=True)
def session() -> Generator[MagicMock, None, None]:
    with patch('core.extensions.db.session', new=MagicMock()) as mock:
        yield mock
