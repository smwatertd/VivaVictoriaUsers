from abc import ABC, abstractmethod


class PasswordEncryptor(ABC):
    @abstractmethod
    def hash_password(self, password: str) -> str:
        pass
