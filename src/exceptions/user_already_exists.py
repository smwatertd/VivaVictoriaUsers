from exceptions.user_register_error import UserRegisterError


class UserAlreadyExists(UserRegisterError):
    message = 'user already exists'
