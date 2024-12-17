# flake8: noqa
from flask import Blueprint, render_template, request, redirect, url_for, Response
from flask_login import current_user, login_required  # type: ignore
from app.repositories import get_activ_page, get_menu_by_id
from app.repositories import BaseRepository
import csv
from io import StringIO


documents_blueprint = Blueprint('documents', __name__, url_prefix='/documents')
documents_blueprints = {'documents.render_documents':
                        documents_blueprint}


def execute_sql(query, is_select):
    repository = BaseRepository()
    try:
        if is_select:
            return {"type": "table", "data": repository.universal_select(query)}
        else:
            return {"type": "text", "data": repository.universal_querry(query)}
    except Exception as e:
        return {"type": "error", "data": str(e)}


@documents_blueprint.route("/", methods=['GET', 'POST'])
@login_required
def render_documents():
    pages = get_menu_by_id(current_user.get_id())
    query = request.args.get("query", "")  # Получаем параметр query из URL
    if request.method == 'POST':
        is_select = False
        query = request.form.get("sql_query", "").strip()
        if not query:
            return render_template("documents/documents.html", error="Запрос пустой", query=query)

        if query.strip().lower().startswith("select"):
            is_select = True
        result = execute_sql(query, is_select)
        # Обрабатываем результат
        if result["type"] == "error":
            return render_template("documents/documents.html", return_type="error", error=result["data"], active_page=get_activ_page(pages, 'documents.render_documents'), pages=pages, query=query)
        elif result["type"] == "table":
            return render_template("documents/documents.html", return_type="table", data=result["data"], active_page=get_activ_page(pages, 'documents.render_documents'), pages=pages, query=query)
        else:
            return render_template("documents/documents.html", return_type="text", message=result["data"], active_page=get_activ_page(pages, 'documents.render_documents'), pages=pages, query=query)

    return render_template("documents/documents.html", active_page=get_activ_page(pages, 'documents.render_documents'), pages=pages, query=query)

@documents_blueprint.route("/export_csv")
@login_required
def export_csv():
    query = request.args.get("query")
    if not query:
        return "Ошибка: не указан запрос", 400

    is_select = query.strip().lower().startswith("select")
    result = execute_sql(query, is_select)

    if not result or len(result) < 2:
        return "Ошибка: запрос не вернул данных", 400

    # Создаем CSV файл из данных
    output = StringIO()
    writer = csv.writer(output)

    # Пишем данные
    for row in result['data']:
        print(row)
        writer.writerow(row)

    output.seek(0)

    # Возвращаем файл как ответ с правильными заголовками
    return Response(
        output,
        mimetype="text/csv",
        headers={
            "Content-Disposition": "attachment;filename=export.csv"
        }
    )

@documents_blueprint.route("/avalable_vacancies")
@login_required
def avalable_vacancies():
    query = '''
SELECT vacancy.id, vacancy.position_title, vacancy.lower_limit_of_salary, vacancy.upper_limit_of_salary, employer.name AS employer_name
FROM vacancy
JOIN employer ON vacancy.employer_id = employer.id
LEFT JOIN agreement ON vacancy.id = agreement.vacancy_id
WHERE agreement.id IS NULL;
'''
    return redirect(url_for('documents.render_documents', query=query))


@documents_blueprint.route("/no_work_experience")
@login_required
def no_work_experience():
    query = '''
SELECT applicant.id, applicant.last_name, applicant.first_name, applicant.middle_name, applicant.age
FROM applicant
LEFT JOIN specialization_applicant ON applicant.id = specialization_applicant.applicant_id
WHERE specialization_applicant.id IS NULL;
'''
    return redirect(url_for('documents.render_documents', query=query))

@documents_blueprint.route("/no_vacancy")
@login_required
def no_vacancy():
    query = '''
SELECT employer.id, employer.name, employer.phone_number
FROM employer
LEFT JOIN vacancy ON employer.id = vacancy.employer_id
WHERE vacancy.id IS NULL;
'''
    return redirect(url_for('documents.render_documents', query=query))

