from os.path import join
from lib.utils import connect_to_db, disconnect_db


def check_existence_of_database():
    init_connection = connect_to_db()
    init_cursor = init_connection.cursor()
    init_cursor.execute("show databases like 'LIMS';")
    result = init_cursor.fetchall()
    if not result:
        init_cursor.execute("create database LIMS CHARACTER SET utf8 COLLATE utf8_general_ci;")
    disconnect_db(init_connection)


def init_db():
    check_existence_of_database()
    database_connection = connect_to_db(database='LIMS')
    cursor = database_connection.cursor()
    with open(join('./SQLs', 'InitDatabase.sql'), 'r') as f:
        cursor.execute(f.read())
    disconnect_db(database_connection)


if __name__ == '__main__':
    init_db()
