from repositories.sqlalchemy import SQLAlchemyUserRepository

from services.create_user_service import CreateUserService
from services.password_encryptors import BcryptPasswordEncryptor


create_user = CreateUserService(
    SQLAlchemyUserRepository(),
    BcryptPasswordEncryptor(),
)
