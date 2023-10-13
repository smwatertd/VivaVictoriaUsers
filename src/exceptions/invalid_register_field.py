from typing import Any, Literal

from exceptions.user_register_error import UserRegisterError


class InvalidRegisterField(UserRegisterError):
    def __init__(
        self,
        field: Literal['email', 'username', 'password'],
        is_blank: bool = False,
        *args: Any,
    ) -> None:
        self.message = f'{field} is {"required" if is_blank else "invalid"}'
        super().__init__(*args)
