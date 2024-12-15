from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required  # type: ignore
from flask_login import logout_user, current_user  # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash
from app.repositories import get_user_id, add_user, get_user_by_id
from app.repositories import get_activ_page, get_menu_by_id


home_blueprint = Blueprint('home', __name__, url_prefix='/',)
home_blueprints = {'home.render_home': home_blueprint}


@home_blueprint.route("/")
@login_required
def render_home():
    '''Рендер главной страницы'''
    pages = get_menu_by_id(current_user.get_id())
    return render_template("home/home.html",
                           active_page=get_activ_page(pages,
                                                      'home.render_home'),
                           pages=pages)


@home_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        try:
            # Проверяем, не занят ли логин
            if get_user_id(login):
                flash('Логин уже занят, выберите другой', 'danger')
                return redirect(url_for('home.register'))

            if len(password) < 8:
                flash('Длина пароля должна быть на меньше 8 симоволов!',
                      'danger')
                return redirect(url_for('home.register'))

            # Добавляем пользователя
            add_user(login, hashed_password)
            flash('Регистрация успешна! Теперь вы можете войти.', 'success')
            return redirect(url_for('home.login'))

        except Exception as e:
            flash(f'Ошибка при регистрации: {e}', 'danger')
            return redirect(url_for('home.register'))

    return render_template('auth/register.html')


@home_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']

        try:
            # Проверяем, существует ли пользователь
            user_id = get_user_id(login)
            if not user_id:
                flash('Пользователь с таким логином не найден', 'danger')
                return redirect(url_for('home.login'))

            # Получаем данные пользователя и проверяем пароль
            user = get_user_by_id(user_id)
            if not check_password_hash(user.password_hash, password):
                flash('Неверное имя пользователя или пароль', 'danger')
                return redirect(url_for('home.login'))

            # Успешный вход
            login_user(user)
            return redirect(url_for('home.render_home'))

        except Exception as e:
            flash(f'Ошибка при обработке запроса: {e}', 'danger')
            return redirect(url_for('home.login'))

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
