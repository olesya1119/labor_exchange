from flask import Blueprint, render_template
from .pages_controller import get_active_page, get_all_pages


home_blueprint = Blueprint('home', __name__, url_prefix='/',)


# TODO: сделать отдельную страницу главной страницы.
# TODO: сделать страницы авторизации и регистрации здесь.

@home_blueprint.route("/")
def render_home():
    '''Рендер главной страницы'''

    return render_template("home/home.html",
                           active_page=get_active_page('home.home'),
                           pages=get_all_pages())


@home_blueprint.route("/documents")
def documents():
    return render_template("documents/documents.html",
                           active_page=get_active_page('documents'),
                           pages=get_all_pages())


@home_blueprint.route("/help")
def help():
    return render_template("help/help.html",
                           active_page=get_active_page('help'),
                           pages=get_all_pages())


@home_blueprint.route("/various")
def various():
    return render_template("various/various.html",
                           active_page=get_active_page('various'),
                           pages=get_all_pages())
