from flask import Flask
from config import Config
from flask_login import LoginManager  # type: ignore
from .repositories.db import init_db
from .routes import home_blueprint, ArchiveRoutes, ApplicantsRoutes
from .routes import VacanciesRoutes, EmployersRoutes
from .routes import directories_blueprints
from .repositories import get_user_by_id


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)
    init_db(app)

    # Регистрация Blueprint
    app.register_blueprint(home_blueprint)

    archive = ArchiveRoutes()
    applicants = ApplicantsRoutes()
    vacancies = VacanciesRoutes()
    employers = EmployersRoutes()

    app.register_blueprint(archive.get_blueprint())
    app.register_blueprint(applicants.get_blueprint())
    app.register_blueprint(vacancies.get_blueprint())
    app.register_blueprint(employers.get_blueprint())

    for bp in directories_blueprints:
        app.register_blueprint(bp)

    # Система авторизаций
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'home.login'  # Укажите функцию обработки входа

    @login_manager.user_loader
    def load_user(user_id):
        return get_user_by_id(user_id)

    return app
