from core.extensions import db

from exceptions import UserRegisterError
from exceptions.handlers import user_register_error_handler

from flask import request
from flask.blueprints import Blueprint

from schemas import CreateUserSchema

from services import create_user


users_view = Blueprint('users', __name__)


users_view.register_error_handler(UserRegisterError, user_register_error_handler)


@users_view.route('/users', methods=['POST'])
def register() -> tuple[str, int]:
    user = CreateUserSchema.model_validate(request.json)
    create_user(db.session, user)
    return '', 201
