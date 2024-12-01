import psycopg2  # type: ignore
from flask import current_app, g

# TODO: Добавить других пользователей


def get_db_connection():
    if 'db_conn' not in g:
        g.db_conn = psycopg2.connect(
            dbname=current_app.config['DB_NAME'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            host=current_app.config['DB_HOST'],
            port=current_app.config['DB_PORT']
        )
    return g.db_conn


def close_db_connection(exc=None):
    db_conn = g.pop('db_conn', None)
    if db_conn is not None:
        db_conn.close()


def init_db(app):
    app.teardown_appcontext(close_db_connection)
