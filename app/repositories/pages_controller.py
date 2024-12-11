from .db import get_db_connection


def get_menu_by_id(id: int):
    cursor = get_db_connection().cursor()
    cursor.execute('SELECT menu.id, menu.id_parent,'
                   'menu.function_name, menu.name, user_rights.r, '
                   'user_rights.w, user_rights.e, user_rights.d '
                   'FROM user_rights '
                   'LEFT JOIN menu ON menu.id = user_rights.id '
                   'WHERE user_rights.id_app_user = %s '
                   'ORDER BY menu.id_parent, menu.menu_order', (id,))
    menu = cursor.fetchall()
    pages = []
    for menu_item in menu:
        if menu_item[1] == 0:
            pages.append(
                {
                    'id': menu_item[0],
                    'function_name': menu_item[2],
                    'name': menu_item[3],
                    'r': menu_item[4],
                    'w': menu_item[5],
                    'e': menu_item[6],
                    'd': menu_item[7],
                    'have_submenu': False
                }
            )
        else:
            for page in pages:
                if page['id'] == menu_item[1]:
                    if 'submenu' not in page:
                        page['have_submenu'] = True
                        page['submenu'] = []
                    page['submenu'].append(
                        {
                            'id': menu_item[0],
                            'function_name': menu_item[2],
                            'name': menu_item[3],
                            'r': menu_item[4],
                            'w': menu_item[5],
                            'e': menu_item[6],
                            'd': menu_item[7],
                        }
                    )
    return pages


def get_activ_page(pages, page_function_name):
    for page in pages:
        if page['function_name'] == page_function_name:
            return page
        elif page['have_submenu']:
            for subpage in page['submenu']:
                if subpage['function_name'] == page_function_name:
                    return subpage
    return pages[0]
