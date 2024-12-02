from flask import Blueprint, render_template

app = Blueprint('main', __name__)

pages = [
    {
        'name': 'base',
        'ru': 'Главная страница'
    },
    {
        'name': 'applicants',
        'ru': 'Соискатели'
    },
    {
        'name': 'employers',
        'ru': 'Работодатели'
    },
    {
        'name': 'vacancies',
        'ru': 'Вакансии'
    },
    {
        'name': 'archive',
        'ru': 'Архив'
    },
    {
        'name': 'directories',
        'ru': 'Справочники'
    },
    {
        'name': 'documents',
        'ru': 'Документы'
    },
    {
        'name': 'help',
        'ru': 'Справка'
    },
    {
        'name': 'various',
        'ru': 'Разное'
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
    return render_template("applicants.html",
                           active_page=get_active_page('applicants'),
                           pages=pages)


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
