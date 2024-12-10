from flask import Flask
from config import Config
from flask_login import LoginManager  # type: ignore
from .repositories.db import init_db
from .routes import blueprints
from .repositories import get_user_by_id


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)
    init_db(app)

    # Регистрация Blueprint
    for bp_name in blueprints:
        app.register_blueprint(blueprints[bp_name])

    # Система авторизаций
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'home.login'  # Укажите функцию обработки входа

    @login_manager.user_loader
    def load_user(user_id):
        return get_user_by_id(user_id)

    return app
