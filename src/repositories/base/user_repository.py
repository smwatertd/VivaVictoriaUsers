from abc import ABC, abstractmethod
from typing import Any

from schemas import CreateUserSchema


class UserRepository(ABC):
    @abstractmethod
    def is_user_exists(self, session: Any, **kwargs: dict) -> bool:
        pass

    @abstractmethod
    def create_user(self, session: Any, user: CreateUserSchema) -> None:
        pass
