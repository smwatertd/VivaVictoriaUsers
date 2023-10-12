from flask import Flask
from views import all_views


def get_production_app() -> Flask:
    app = Flask(__name__)
    _register_views(app)
    return app


def run_app(app: Flask) -> None:
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )


def _register_views(app: Flask) -> None:
    for view in all_views:
        app.register_blueprint(view)
