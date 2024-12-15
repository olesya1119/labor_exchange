from flask_login import UserMixin  # type: ignore
from .db import get_db_connection


class User(UserMixin):
    def __init__(self, id, login, password_hash):
        self.id = id
        self.login = login
        self.password_hash = password_hash

    def get_id(self):
        return str(self.id)


def get_user_by_id(user_id):
    cursor = get_db_connection().cursor()
    try:
        cursor.execute("SELECT id, login, password_hash "
                       "FROM app_user WHERE id = %s", (user_id,))
        row = cursor.fetchone()
        if row:
            return User(row[0], row[1], row[2])
        return None
    except Exception:
        return None


def get_user_id(login):
    cursor = get_db_connection().cursor()
    cursor.execute("SELECT id, login, password_hash "
                   "FROM app_user WHERE login = %s", (login, ))
    row = cursor.fetchone()
    if row:
        return row[0]
    return None


def add_user(login, hashed_password):
    cursor = get_db_connection().cursor()
    cursor.execute("INSERT INTO app_user (login, password_hash) "
                   "VALUES (%s, %s)", (login, hashed_password))
    get_db_connection().commit()


def update_password(user_id, new_hashed_password):
    cursor = get_db_connection().cursor()
    cursor.execute("UPDATE app_user SET password_hash= %s "
                   "WHERE id = %s", (new_hashed_password, user_id))
    get_db_connection().commit()
