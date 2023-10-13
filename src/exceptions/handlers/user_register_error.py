from exceptions.user_register_error import UserRegisterError

from flask import Response, jsonify


def user_register_error_handler(error: UserRegisterError) -> tuple[Response, int]:
    return jsonify({'status': 'error', 'message': error.message}), 400
