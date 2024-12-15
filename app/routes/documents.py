from flask import Blueprint, render_template
from flask_login import current_user, login_required  # type: ignore
from app.repositories import get_activ_page, get_menu_by_id


documents_blueprint = Blueprint('documents', __name__, url_prefix='/',)
documents_blueprints = {'documents.render_documents':
                        documents_blueprint}


@documents_blueprint.route("/")
@login_required
def render_documents():
    '''Рендер главной страницы'''
    pages = get_menu_by_id(current_user.get_id())
    return render_template("documents/documents.html",
                           active_page=get_activ_page(pages,
                                                      'documents.'
                                                      'render_documents'
                                                      ),
                           pages=pages)
