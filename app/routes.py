from flask import g
from flask import Blueprint
from .db import get_db_connection


app = Blueprint('main', __name__)


@app.route("/test", methods=["GET"])
def test_connection():
    # get_db_connection()
    # cursor = g.db_conn.cursor()
    # cursor.execute('''SELECT * FROM applicant''')
    # g.db_conn.commit()
    return 'Hello, World!'


@app.route("/", methods=["GET"])
def test_connection1():
    get_db_connection()
    cursor = g.db_conn.cursor()
    cursor.execute('''SELECT * FROM applicant''')
    g.db_conn.commit()
    return cursor.fetchall()
