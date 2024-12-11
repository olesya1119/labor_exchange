from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required  # type: ignore
from flask_login import logout_user, current_user  # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash
from app.repositories import get_user_id, add_user, get_user_by_id
from app.repositories import get_activ_page, get_menu_by_id


home_blueprint = Blueprint('home', __name__, url_prefix='/',)
home_blueprints = {'home.render_home': home_blueprint}


# TODO: сделать отдельную страницу главной страницы.
# TODO: сделать страницы авторизации и регистрации здесь.

@home_blueprint.route("/")
@login_required
def render_home():
    '''Рендер главной страницы'''
    pages = get_menu_by_id(current_user.get_id())
    return render_template("home/home.html",
                           active_page=get_activ_page(pages, 'home.home'),
                           pages=pages)


@home_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        add_user(login, hashed_password)

        return redirect(url_for('home.login'))
    return render_template('auth/register.html')


@home_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']

        user_id = get_user_id(login)
        if user_id:
            user = get_user_by_id(user_id)
            if check_password_hash(user.password_hash, password):
                login_user(user)
                return redirect(url_for('home.render_home'))
            else:
                flash('Неверное имя пользователя или пароль', 'danger')
    return render_template('auth/login.html')


@home_blueprint.route('/protected')
@login_required
def protected():
    return "This is a protected page."


@home_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.login'))


@home_blueprint.route("/documents")
@login_required
def documents():
    pages = get_menu_by_id(current_user.get_id())
    return render_template("documents/documents.html",
                           active_page=get_activ_page(pages, 'documents'),
                           pages=pages)


@home_blueprint.route("/help")
@login_required
def help():
    pages = get_menu_by_id(current_user.get_id())
    return render_template("help/help.html",
                           active_page=get_activ_page(pages, 'help'),
                           pages=pages)


@home_blueprint.route("/various")
@login_required
def various():
    pages = get_menu_by_id(current_user.get_id())
    return render_template("various/various.html",
                           active_page=get_activ_page(pages, 'various'),
                           pages=pages)
