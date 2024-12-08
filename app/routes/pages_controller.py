PAGES = [
    {
        'name': 'home.render_home',
        'ru': 'Главная страница',
        'have_submenu': False,
        'submenu': []
    },
    {
        'name': 'applicants.render_table',
        'ru': 'Соискатели',
        'have_submenu': False,
        'submenu': []
    },
    {
        'name': 'employers.render_table',
        'ru': 'Работодатели',
        'have_submenu': False,
        'submenu': []
    },
    {
        'name': 'vacancies.render_table',
        'ru': 'Вакансии',
        'have_submenu': False,
        'submenu': []
    },
    {
        'name': 'archive.render_table',
        'ru': 'Архив',
        'have_submenu': False,
        'submenu': []
    },
    {
        'name': 'directories.render_directories',
        'ru': 'Справочники',
        'have_submenu': True,
        'submenu':
            [
                {
                    'name': 'specializations.render_table',
                    'ru': 'Специальности'
                },
                {
                    'name': 'educational_institutions.render_table',
                    'ru': 'Учебные заведения'
                },
                {
                    'name': 'education_levels.render_table',
                    'ru': 'Уровни образования'
                },
                {
                    'name': 'education_documents.render_table',
                    'ru': 'Документы об образовании'
                },
                {
                    'name': 'allowances.render_table',
                    'ru': 'Пособия'
                },
                {
                    'name': 'applicant_requirements.render_table',
                    'ru': 'Требования к работнику'
                },
                {
                    'name': 'fields_of_activity.render_table',
                    'ru': 'Сферы деятельности'
                },
                {
                    'name': 'cities.render_table',
                    'ru': 'Города'
                },
                {
                    'name': 'streets.render_table',
                    'ru': 'Улицы'
                }
            ]
    },
    {
        'name': 'home.documents',
        'ru': 'Документы',
        'have_submenu': False,
        'submenu': []
    },
    {
        'name': 'home.help',
        'ru': 'Справка',
        'have_submenu': False,
        'submenu': []
    },
    {
        'name': 'home.various',
        'ru': 'Разное',
        'have_submenu': False,
        'submenu': []
    }
]

# TODO: нужно создать таблицу в БД со струткурой страниц и генерацию списка.
# TODO: во все страницы передается список всех страниц. Это нужно
# внести в контекст Flask


def get_active_page(name: str) -> dict:
    '''
    Возвращает информацию о странице с именем name.
    Информация в формате словаря.
    'name' - уникальное название страницы (соответсвует
        названию функции в routes)
    'ru' - название страницы на русском языке
    'have_submenu' - имеет ли страницы подменю
    'submenu' (есть только если have_submenu = True) - описание
        подменю (представляет аналогичный список страниц).
        Предоставляется поддержка только 1-ого уровня подменю на уровне html.
        Т.е. наличие подменю у подменю игнорируется
    '''

    for page in PAGES:
        if page['name'] == name:
            return page
    for page in PAGES:
        if page['have_submenu']:
            for subpage in page['submenu']:
                if subpage['name'] == name:
                    return subpage
    return PAGES[0]


def get_all_pages() -> list:
    '''
    Возвращает информацию обо всех страницах.
    Информация в формате списка словарей.
    Каждый словарь иммет следующую структуру:
    'name' - уникальное название страницы (соответсвует
        названию функции в routes)
    'ru' - название страницы на русском языке
    'have_submenu' - имеет ли страницы подменю
    'submenu' (есть только если have_submenu = True) - описание
        подменю (представляет аналогичный список страниц).
        Предоставляется поддержка только 1-ого уровня подменю на уровне html.
        Т.е. наличие подменю у подменю игнорируется
    '''

    return PAGES
