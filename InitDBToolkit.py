from os.path import join
from lib.encrypt import generate_rsa_keys
from lib.utils import connect_to_db, disconnect_db, execute_sql_script


def check_existence_of_database():
    init_connection = connect_to_db()
    init_cursor = init_connection.cursor()
    init_cursor.execute("show databases like 'LIMS';")
    result = init_cursor.fetchall()
    if result:
        answer = input("Database LIMS exists, want to remove it?[y/N]: ")
        if answer == 'y':
            init_cursor.execute('drop database LIMS;')
        else:
            print('Nothing done.')
            return True
    init_cursor.execute("create database LIMS CHARACTER SET utf8 COLLATE utf8_general_ci;")
    disconnect_db(init_connection)
    return False


def init_db():
    if check_existence_of_database():
        return None
    database_connection = connect_to_db(database='LIMS')
    cursor = database_connection.cursor()
    execute_sql_script(cursor, join('./SQLs', 'InitDatabase.sql'))
    database_connection.commit()
    disconnect_db(database_connection)


def init_data():
    database_connection = connect_to_db(database='LIMS')
    cursor = database_connection.cursor()
    execute_sql_script(cursor, join('./SQLs', 'InitData.sql'))
    database_connection.commit()
    disconnect_db(database_connection)


if __name__ == '__main__':
    init_db()
    init_data()
