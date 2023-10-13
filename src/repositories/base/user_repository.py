from abc import ABC, abstractmethod
from typing import Any

from schemas import CreateUserSchema


class UserRepository(ABC):
    @abstractmethod
    def create_user(self, session: Any, user: CreateUserSchema) -> None:
        pass
