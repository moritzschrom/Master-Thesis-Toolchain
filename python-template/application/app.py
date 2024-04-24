from flask import Flask

def create_app() -> Flask:
    """Yields a configured Flask application"""

    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    from application.routes.hello import hello_blueprint
    app.register_blueprint(hello_blueprint)

    return app
