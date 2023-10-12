from core import get_production_app, run_app


app = get_production_app()


if __name__ == '__main__':
    run_app(app)
