from flask import Flask
from config import Config
from .repositories.db import init_db
from .routes import home_blueprint, ArchiveRoutes, ApplicantsRoutes
from .routes import VacanciesRoutes, EmployersRoutes


def create_app():
    app = Flask(__name__)
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

    return app
