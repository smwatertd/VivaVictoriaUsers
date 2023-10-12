from flask.blueprints import Blueprint
from flask import jsonify, Response


health_view = Blueprint('health', __name__)


@health_view.route('/health', methods=['GET'])
def check_health() -> tuple[Response, int]:
    return jsonify({'status': 'ok'}), 200
