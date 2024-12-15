from flask import Blueprint, render_template
from flask_login import login_required, current_user  # type: ignore
from app.repositories import get_activ_page, get_menu_by_id


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


@various_blueprint.route("/change_password")
@login_required
def change_password():
    pages = get_menu_by_id(current_user.get_id())
    return render_template("various/change_password.html",
                           active_page=get_activ_page(pages,
                                                      'various.change_password'
                                                      ),
                           pages=pages)
