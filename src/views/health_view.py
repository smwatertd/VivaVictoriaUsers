from flask import Response, jsonify
from flask.blueprints import Blueprint


health_view = Blueprint('health', __name__)


@health_view.route('/health', methods=['GET'])
def check_health() -> tuple[Response, int]:
    return jsonify({'status': 'ok'}), 200
