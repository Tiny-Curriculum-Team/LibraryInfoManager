from os import listdir
from os.path import join
from lib.utils import connect_to_db, disconnect_db


def init_db():
    database_connection = connect_to_db()
    db_cursor = database_connection.cursor()
    with open(join('SQLs', 'InitDatabase.sql'), 'r') as f:
        try:
            db_cursor.execute(f.read())
        except Exception as e:
            print("Initialization Failed!")
            print(e)
    database_connection.commit()
    disconnect_db(database_connection)


if __name__ == '__main__':
    init_db()
