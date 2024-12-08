PAGES = [
    {
        'name': 'home.render_home',
        'ru': 'Главная страница',
        'have_submenu': False
    },
    {
        'name': 'applicants.render_table',
        'ru': 'Соискатели',
        'have_submenu': False
    },
    {
        'name': 'employers.render_table',
        'ru': 'Работодатели',
        'have_submenu': False
    },
    {
        'name': 'vacancies.render_table',
        'ru': 'Вакансии',
        'have_submenu': False
    },
    {
        'name': 'archive.render_table',
        'ru': 'Архив',
        'have_submenu': False
    },
    {
        'name': 'home.directories',
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
        'name': 'home.documents',
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
        'name': 'home.help',
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
        'name': 'home.various',
        'ru': 'Разное',
        'have_submenu': True
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
