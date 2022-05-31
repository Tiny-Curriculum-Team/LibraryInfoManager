from os.path import join
from lib.utils import connect_to_db, disconnect_db, execute_sql_script


def check_existence_of_database():
    init_connection = connect_to_db()
    init_cursor = init_connection.cursor()
    init_cursor.execute("show databases like 'LIMS';")
    result = init_cursor.fetchall()
    if result:
        answer = input("Database LIMS exists, want to remove it?[y/N]\n")
        if answer == 'y':
            init_cursor.execute('drop database LIMS;')
        else:
            print('Nothing done.')
            return False
    init_cursor.execute("create database LIMS CHARACTER SET utf8 COLLATE utf8_general_ci;")
    disconnect_db(init_connection)
    return True


def init_db(data_initialize):
    check_existence_of_database()
    database_connection = connect_to_db(database='LIMS')
    cursor = database_connection.cursor()
    execute_sql_script(cursor, join('./SQLs', 'InitDatabase.sql'))
    database_connection.commit()
    disconnect_db(database_connection)
    data_initialize()


def init_data():
    database_connection = connect_to_db(database='LIMS')
    cursor = database_connection.cursor()
    execute_sql_script(cursor, join('./SQLs', 'InitData.sql'))
    database_connection.commit()
    disconnect_db(database_connection)


if __name__ == '__main__':
    init_db(init_data)
