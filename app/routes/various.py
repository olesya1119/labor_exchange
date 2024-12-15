from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user  # type: ignore
from app.repositories import get_activ_page, get_menu_by_id, update_password
from werkzeug.security import generate_password_hash, check_password_hash
from app.repositories import get_user_by_id


various_blueprint = Blueprint('various', __name__, url_prefix='/various',)
various_blueprints = {'various.render_various': various_blueprint}


@various_blueprint.route("/")
@login_required
def render_various():
    pages = get_menu_by_id(current_user.get_id())
    return render_template("various/various.html",
                           active_page=get_activ_page(pages,
                                                      'help.render_help'),
                           pages=pages)


@various_blueprint.route("/change_password", methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        new_hashed_password = generate_password_hash(new_password)
        user = get_user_by_id(current_user.get_id())

        if not check_password_hash(user.password_hash, old_password):
            flash('Текущий пароль введен неверно', 'danger')
            return redirect(url_for('various.change_password'))

        if len(new_hashed_password) < 8:
            flash('Длина нового пароля должна быть на меньше 8 симоволов!',
                  'danger')
            return redirect(url_for('various.change_password'))

        update_password(current_user.get_id(), new_hashed_password)
        flash('Пароль успешно сменен!', 'success')
        return redirect(url_for('various.change_password'))

    pages = get_menu_by_id(current_user.get_id())
    return render_template("various/change_password.html",
                           active_page=get_activ_page(pages,
                                                      'various.change_password'
                                                      ),
                           pages=pages)
