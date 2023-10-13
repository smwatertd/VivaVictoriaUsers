from core.extensions import db

from flask import request
from flask.blueprints import Blueprint

from schemas import CreateUserSchema

from services import create_user


users_view = Blueprint('users', __name__)


@users_view.route('/users', methods=['POST'])
def register() -> tuple[str, int]:
    user = CreateUserSchema.model_validate(request.json)
    create_user(db.session, user)
    return '', 201
