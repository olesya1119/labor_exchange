from flask import Flask
from config import Config
from .db import init_db
from .routes import app as main_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    init_db(app)

    # Регистрация Blueprint
    app.register_blueprint(main_bp)

    return app
