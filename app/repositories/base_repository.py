import psycopg2  # type: ignore
from db import get_db_connection  # type: ignore
from typing import Tuple


class BaseRepository():

    table_name = 'not_found'

    @staticmethod
    def execute_query(func):
        def wrapper(*args, **kwargs):
            cursor = get_db_connection().cursor()
            query = func(*args, **kwargs)
            try:
                cursor.execute(query)
                get_db_connection().commit()
                return True
            except psycopg2.DatabaseError:
                return False
            finally:
                cursor.close()
        return wrapper

    @staticmethod
    def fetch_results(func):
        def wrapper(*args, **kwargs):
            cursor = get_db_connection().cursor()
            query = func(*args, **kwargs)
            try:
                cursor.execute(query)
                return cursor.fetchall()
            except psycopg2.DatabaseError:
                return False
            finally:
                cursor.close()
        return wrapper

    @fetch_results
    def get_by_id(self, id: int) -> Tuple[str, int]:
        return '''SELECT * FROM {table_name} WHERE id = %s''', id

    @fetch_results
    def get_paginated(self, limit: int, offset: int) -> Tuple[str, int, int]:
        return ('''SELECT * FROM {table_name} LIMIT %s OFFSET %s''',
                limit,
                offset)

    @fetch_results
    def delete_by_id(self, id: int) -> Tuple[str, int]:
        return '''DELETE * FROM {table_name} WHERE id = %s''', id
