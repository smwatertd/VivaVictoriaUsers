from passlib.context import CryptContext

from services.password_encryptors.password_encryptor import PasswordEncryptor


class BcryptPasswordEncryptor(PasswordEncryptor):
    password_context = CryptContext('bcrypt')

    def hash_password(self, password: str) -> str:
        return self.password_context.hash(password)
