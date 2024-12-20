from .db import get_db_connection  # type: ignore
from typing import Tuple
from app.models import BaseModel


class BaseRepository():

    table_name = 'not_found'

    @staticmethod
    def execute_query(func):
        def wrapper(*args, **kwargs):
            cursor = get_db_connection().cursor()
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
    def execute_query_without_args(func):
        def wrapper(*args, **kwargs):
            cursor = get_db_connection().cursor()
            query = func(*args, **kwargs)
            try:
                cursor.execute(query)
                get_db_connection().commit()
                print(query)
                return 'Запрос успешно выполнен! '
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
    def fetch_results_with_head(func):
        def wrapper(*args, **kwargs):
            cursor = get_db_connection().cursor()
            query, values = func(*args, **kwargs)
            try:
                cursor.execute(query, values)
                # Получение названий столбцов
                column_names = tuple(desc[0] for desc in cursor.description)

                # Получение данных
                rows = cursor.fetchall()

                # Формирование результата
                result = [column_names] + rows
                return result
            except Exception as e:
                raise e
            finally:
                cursor.close()
        return wrapper

    @staticmethod
    def fetch_results_with_head_without_args(func):
        def wrapper(*args, **kwargs):
            cursor = get_db_connection().cursor()
            query = func(*args, **kwargs)
            try:
                cursor.execute(query)
                # Получение названий столбцов
                column_names = tuple(desc[0] for desc in cursor.description)

                # Получение данных
                rows = cursor.fetchall()

                # Формирование результата
                result = [column_names] + rows
                return result
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

    @fetch_results_with_head
    def select(self, limit: int, offset: int, order_by: int = 0,
               order_acs: bool = True, mask: str = '') -> Tuple[str, tuple]:
        return (
            f'''SELECT *
            FROM {self.table_name} '''
            f'''ORDER BY id {'ASC' if order_acs else 'DESC'} '''
            f'''LIMIT %s OFFSET %s''',
            (limit, offset, ))

    @fetch_results_with_head
    def select_with_join(self, limit: int, offset: int, order_by: int = 0,
                         order_acs: bool = True, mask: str = ''
                         ) -> Tuple[str, tuple]:
        return (
            f'''SELECT *
            FROM {self.table_name} '''
            f'''ORDER BY {order_by} {'ASC' if order_acs else 'DESC'} '''
            f'''LIMIT %s OFFSET %s''',
            (limit, offset, ))

    def _get_where_querry(self, title: list):
        where_querry = "WHERE LOWER(CONCAT_WS(' ', "
        for name in title:
            where_querry += f"{name}, "
        where_querry = where_querry[:-2] + ')) LIKE LOWER(%s)'
        return where_querry

    @fetch_results_with_head_without_args
    def universal_select(self, querry):
        return querry

    @execute_query_without_args
    def universal_querry(self, querry):
        return querry
