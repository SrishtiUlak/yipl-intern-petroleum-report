import sqlite3
from sqlite3 import Error
database = "petroReport.db"


def create_connection():
    conn = None
    try:
        # establishing the connection with database
        conn = sqlite3.connect(database)
        return conn

    except Error as e:
        print(e)

    return conn
