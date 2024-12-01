import psycopg2  # type: ignore
from flask import g


class BaseRepository():
    def execute_query(func):
        def wrapper(self, *args, **kwargs):
            cursor = g.db_conn.cursor()
            query = func()
            try:
                cursor.execute(query)
                g.db_conn.commit()
                return True
            except psycopg2.DatabaseError:
                return False
            finally:
                cursor.close()
        return wrapper
