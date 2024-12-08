from flask import Flask
from config import Config
from .repositories.db import init_db
from .routes import home_blueprint, ArchiveRoutes, ApplicantsRoutes
from .routes import VacanciesRoutes, EmployersRoutes
from .routes import directories_blueprints


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

    print(app.jinja_loader.searchpath)

    return app
