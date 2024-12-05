import psycopg2  # type: ignore
from .db import get_db_connection  # type: ignore
from typing import Tuple


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
            except psycopg2.DatabaseError as e:
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
            except psycopg2.DatabaseError as e:
                raise e
            finally:
                cursor.close()
        return wrapper

    @fetch_results
    def get_by_id(self, id: int) -> Tuple[str, int]:
        return (f'''SELECT * FROM {self.table_name} ORDER BY '''
                f'''{self.table_name}.id WHERE id = %s''', id)

    @fetch_results
    def get_paginated(self, limit: int, offset: int) -> Tuple[str, tuple]:
        return (
            f'''SELECT * FROM {self.table_name} ORDER BY '''
            f'''{self.table_name}.id LIMIT %s OFFSET %s''',
            (limit, offset))

    @execute_query
    def delete_by_id(self, id: int) -> Tuple[str, int]:
        return f'''DELETE * FROM {self.table_name} WHERE id = %s''', id

    @execute_query
    def update_by_id(self, id: int, entry: dict) -> Tuple[str, tuple]:
        query = f'''UPDATE {self.table_name} SET '''
        for field_name in entry.keys():
            query += f'''{field_name} = %s, '''
        query = query[:-2] + ''' WHERE id = %s'''
        return query, tuple(entry.values()) + (id, )

    @fetch_results
    def get_count(self) -> Tuple[str, tuple]:
        return (f'''SELECT COUNT(%s) FROM {self.table_name}''', ('*', ))

    @fetch_results
    def get_fields_name(self):
        return ('''SELECT column_name FROM information_schema.columns WHERE'''
                '''table_name = '%s';''', ('self.table_name', ))
