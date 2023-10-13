from exceptions import InvalidRegisterField

from pydantic import BaseModel, EmailStr, model_validator


class CreateUserSchema(BaseModel):
    email: EmailStr
    username: str
    password: str

    @model_validator(mode='before')
    def temp(cls, values: dict) -> dict:
        cls.validate_email(values.get('email'))
        cls.validate_username(values.get('username'))
        cls.validate_password(values.get('password'))
        return values

    @classmethod
    def validate_email(cls, value: str | None) -> str:
        if value is None:
            raise InvalidRegisterField(field='email', is_blank=True)
        return value

    @classmethod
    def validate_username(cls, value: str | None) -> str:
        if value is None:
            raise InvalidRegisterField(field='username', is_blank=True)
        return value

    @classmethod
    def validate_password(cls, value: str | None) -> str:
        if value is None:
            raise InvalidRegisterField(field='password', is_blank=True)
        return value
