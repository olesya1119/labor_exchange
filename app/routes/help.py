from flask import Blueprint, render_template
from flask_login import login_required, current_user  # type: ignore
from app.repositories import get_activ_page, get_menu_by_id


help_blueprint = Blueprint('help', __name__, url_prefix='/help',)
help_blueprints = {'help.render_help': help_blueprint}


@help_blueprint.route("/")
@login_required
def render_help():
    pages = get_menu_by_id(current_user.get_id())
    return render_template("help/help.html",
                           active_page=get_activ_page(pages,
                                                      'help.render_help'),
                           pages=pages)


@help_blueprint.route("/content")
@login_required
def content():
    pages = get_menu_by_id(current_user.get_id())
    return render_template("help/content.html",
                           active_page=get_activ_page(pages,
                                                      'help.content'),
                           pages=pages)


@help_blueprint.route("/about_program")
@login_required
def about_program():
    pages = get_menu_by_id(current_user.get_id())
    return render_template("help/about_program.html",
                           active_page=get_activ_page(pages,
                                                      'help.about_program'),
                           pages=pages)
