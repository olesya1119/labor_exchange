from flask import Blueprint, render_template, request
from app.repositories import ApplicantRepository

app = Blueprint('main', __name__)

pages = [
    {
        'name': 'base',
        'ru': 'Главная страница',
        'have_submenu': False
    },
    {
        'name': 'applicants',
        'ru': 'Соискатели',
        'have_submenu': False
    },
    {
        'name': 'employers',
        'ru': 'Работодатели',
        'have_submenu': False
    },
    {
        'name': 'vacancies',
        'ru': 'Вакансии',
        'have_submenu': False
    },
    {
        'name': 'archive',
        'ru': 'Архив',
        'have_submenu': False
    },
    {
        'name': 'directories',
        'ru': 'Справочники',
        'have_submenu': True,
        'submenu':
            [
                {
                    'name': 'specializations',
                    'ru': 'Специальности'
                },
                {
                    'name': '',
                    'ru': 'Учебные заведения'
                },
                {
                    'name': 'Specializations',
                    'ru': 'Уровни образования'
                },
                {
                    'name': 'Specializations',
                    'ru': 'Документы об образовании'
                },
                {
                    'name': 'Specializations',
                    'ru': 'Пособия'
                },
                {
                    'name': 'Specializations',
                    'ru': 'Требования к работнику'
                },
                {
                    'name': 'Specializations',
                    'ru': 'Сферы деятельности'
                },
                {
                    'name': 'Specializations',
                    'ru': 'Города'
                },
                {
                    'name': 'Specializations',
                    'ru': 'Улицы'
                }
            ]
    },
    {
        'name': 'documents',
        'ru': 'Документы',
        'have_submenu': True,
        'submenu':
            [
                {
                    'name': 'Specializations',
                    'ru': 'Экспорт в SCV'
                }
            ]
    },
    {
        'name': 'help',
        'ru': 'Справка',
        'have_submenu': True,
        'submenu':
            [
                {
                    'name': '',
                    'ru': 'Содержание'
                },
                {
                    'name': '',
                    'ru': 'О программе'
                }
            ]
    },
    {
        'name': 'various',
        'ru': 'Разное',
        'have_submenu': True
    }
]


def get_active_page(name: str):
    for page in pages:
        if page['name'] == name:
            return page
    return pages[0]


@app.route("/")
def base():
    return render_template("base.html",
                           active_page=get_active_page('base'),
                           pages=pages)


@app.route("/applicants")
def applicants():
    # Получение количества записей
    records_per_page = int(request.args.get('records_per_page', 10))
    apl_rep = ApplicantRepository()
    applicants_data = apl_rep.get_paginated(records_per_page, 0)
    print(applicants_data)
    return render_template("applicants.html",
                           active_page=get_active_page('applicants'),
                           pages=pages, applicants=applicants_data,
                           records_per_page=records_per_page)


@app.route("/employers")
def employers():
    return render_template("employers.html",
                           active_page=get_active_page('employers'),
                           pages=pages)


@app.route("/vacancies")
def vacancies():
    return render_template("vacancies.html",
                           active_page=get_active_page('vacancies'),
                           pages=pages)


@app.route("/archive")
def archive():
    return render_template("archive.html",
                           active_page=get_active_page('archive'),
                           pages=pages)


@app.route("/directories")
def directories():
    return render_template("directories.html",
                           active_page=get_active_page('directories'),
                           pages=pages)


@app.route("/documents")
def documents():
    return render_template("documents.html",
                           active_page=get_active_page('documents'),
                           pages=pages)


@app.route("/help")
def help():
    return render_template("help.html",
                           active_page=get_active_page('help'),
                           pages=pages)


@app.route("/various")
def various():
    return render_template("various.html",
                           active_page=get_active_page('various'),
                           pages=pages)
