from abc import ABC, abstractmethod
from typing import Any


class Service(ABC):
    @abstractmethod
    def __call__(self, session: Any, *args: Any, **kwargs: Any) -> Any:
        pass
