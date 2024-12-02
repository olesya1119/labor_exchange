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
            except psycopg2.DatabaseError:
                return False
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
            except psycopg2.DatabaseError:
                return False
            finally:
                cursor.close()
        return wrapper

    @fetch_results
    def get_by_id(self, id: int) -> Tuple[str, int]:
        return f'''SELECT * FROM {self.table_name} WHERE id = %s''', id

    @fetch_results
    def get_paginated(self, limit: int, offset: int) -> Tuple[str, tuple]:
        return (
            f'''SELECT * FROM {self.table_name} LIMIT %s OFFSET %s''',
            (limit, offset))

    @fetch_results
    def delete_by_id(self, id: int) -> Tuple[str, int]:
        return f'''DELETE * FROM {self.table_name} WHERE id = %s''', id
