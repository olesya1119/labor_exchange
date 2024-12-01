import psycopg2  # type: ignore
from flask import g
from .util import to_filds_list, to_values_list


def create_entry(table_name: str, **kwargs) -> bool:
    '''
    Создает запись в таблице table_name.
    kwargs - словарь, вида ['имя_поля': значение]
    Возвращает True при успешной записи, и False при ошибке
    '''
    cursor = g.db_conn.cursor()
    if 'id' in kwargs.keys():
        kwargs.pop('id')
    query = (f'''INSERT INTO {table_name} {to_filds_list(kwargs.keys())}'''
             f'''VALUES {to_values_list(len(kwargs.keys()))}''')

    try:
        cursor.execute(query, kwargs.values())
        g.db_conn.commit()
        return True
    except psycopg2.DatabaseError:
        return False
    finally:
        cursor.close()
