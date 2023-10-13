from typing import Any

from repositories.base import UserRepository

from schemas import CreateUserSchema

from services.password_encryptors.password_encryptor import PasswordEncryptor
from services.service import Service


class CreateUserService(Service):
    def __init__(
        self,
        user_repository: UserRepository,
        password_encryptor: PasswordEncryptor,
    ) -> None:
        self._user_repository = user_repository
        self._password_encryptor = password_encryptor

    def __call__(self, session: Any, user: CreateUserSchema) -> None:
        user.password = self._password_encryptor.hash_password(user.password)
        self._user_repository.create_user(session, user)
        session.commit()
