from flask import Blueprint, render_template
from .pages_controller import get_active_page, get_all_pages


home_app = Blueprint('home', __name__, url_prefix='/',
                     template_folder='templates/home')


# TODO: сделать отдельную страницу главной страницы.
# TODO: сделать страницы авторизации и регистрации здесь.

@home_app.route("/")
def render_home():
    '''Рендер главной страницы'''

    return render_template("home.html",
                           active_page=get_active_page('home.home'),
                           pages=get_all_pages())


'''
@home_app.route("/directories")
def directories():
    return render_template("directories.html",
                           active_page=get_active_page('directories'),
                           pages=get_all_pages())


@home_app.route("/documents")
def documents():
    return render_template("documents.html",
                           active_page=get_active_page('documents'),
                           pages=get_all_pages())


@home_app.route("/help")
def help():
    return render_template("help.html",
                           active_page=get_active_page('help'),
                           pages=get_all_pages())


@home_app.route("/various")
def various():
    return render_template("various.html",
                           active_page=get_active_page('various'),
                           pages=get_all_pages())
'''
