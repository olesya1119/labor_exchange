from .db import get_db_connection  # type: ignore
from typing import Tuple
from app.models import BaseModel


class BaseRepository():

    table_name = 'not_found'

    @staticmethod
    def execute_query(func):
        def wrapper(*args, **kwargs):
            cursor = get_db_connection().cursor()
            print(*args, **kwargs)
            print(func(*args, **kwargs))
            query, values = func(*args, **kwargs)
            try:
                cursor.execute(query, values)
                get_db_connection().commit()
                return True
            except Exception as e:
                raise e
            finally:
                cursor.close()
        return wrapper

    @staticmethod
    def fetch_results(func):
        def wrapper(*args, **kwargs):
            cursor = get_db_connection().cursor()
            query, values = func(*args, **kwargs)
            try:
                cursor.execute(query, values)
                return cursor.fetchall()
            except Exception as e:
                raise e
            finally:
                cursor.close()
        return wrapper

    @staticmethod
    def fetch_results_without_args(func):
        def wrapper(*args, **kwargs):
            cursor = get_db_connection().cursor()
            query = func(*args, **kwargs)
            try:
                cursor.execute(query)
                return cursor.fetchall()
            except Exception as e:
                raise e
            finally:
                cursor.close()
        return wrapper

    @execute_query
    def update(self, model: BaseModel) -> Tuple[str, tuple]:
        '''Обновить запись'''
        return '', tuple()

    @execute_query
    def add(self, model: BaseModel) -> Tuple[str, tuple]:
        '''Добавить новую запись'''
        return '', tuple()

    @fetch_results
    def get_by_id(self, id: int) -> Tuple[str, tuple]:
        '''Получить запись по id'''
        return (f'''SELECT * FROM {self.table_name} ORDER BY '''
                f'''{self.table_name}.id WHERE id = %s''', (id, ))

    @fetch_results
    def get_paginated(self, limit: int, offset: int) -> Tuple[str, tuple]:
        '''Получить limit записей с offset сдвигом'''
        return (
            f'''SELECT * FROM {self.table_name} ORDER BY '''
            f'''{self.table_name}.id LIMIT %s OFFSET %s''',
            (limit, offset))

    @execute_query
    def delete_by_id(self, id: int) -> Tuple[str, tuple]:
        '''Удалить запись по id'''
        return (f'''DELETE FROM {self.table_name} WHERE id = %s''', (id, ))

    @fetch_results_without_args
    def get_count(self) -> str:
        '''Получить общее количество записей в таблице'''
        return f'''SELECT COUNT(*) FROM {self.table_name}'''

    @fetch_results_without_args
    def get_fields_name(self) -> str:
        '''Получить название колонок в таблице'''
        return ('''SELECT column_name FROM information_schema.columns WHERE'''
                '''table_name = "{self.table_name}"''')

    @fetch_results_without_args
    def get_last_id(self) -> str:
        '''Получить id последнего элемента'''
        return f'''SELECT MAX({self.table_name}.id) FROM {self.table_name}'''

    # TODO: возможно это неправильно и стоит как-то иначе давать новые id
    # Если удалить и добавить последний элемент то id тот же
