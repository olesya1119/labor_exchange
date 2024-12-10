from flask import Blueprint, render_template, request, redirect, url_for, flash
from .pages_controller import get_active_page, get_all_pages
from flask_login import login_user, login_required  # type: ignore
from flask_login import logout_user  # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash
from app.repositories import get_user_id, add_user, get_user_by_id


home_blueprint = Blueprint('home', __name__, url_prefix='/',)
home_blueprints = {'home.render_home': home_blueprint}


# TODO: сделать отдельную страницу главной страницы.
# TODO: сделать страницы авторизации и регистрации здесь.

@home_blueprint.route("/")
@login_required
def render_home():
    '''Рендер главной страницы'''

    return render_template("home/home.html",
                           active_page=get_active_page('home.home'),
                           pages=get_all_pages())


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
    return redirect(url_for('login'))


@home_blueprint.route("/documents")
@login_required
def documents():
    return render_template("documents/documents.html",
                           active_page=get_active_page('documents'),
                           pages=get_all_pages())


@home_blueprint.route("/help")
@login_required
def help():
    return render_template("help/help.html",
                           active_page=get_active_page('help'),
                           pages=get_all_pages())


@home_blueprint.route("/various")
@login_required
def various():
    return render_template("various/various.html",
                           active_page=get_active_page('various'),
                           pages=get_all_pages())
