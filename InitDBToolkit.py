from lib.utils import connect2db, disconnect_db
from lib.SQLs import *

SQLs = [
    create_book_table_sql,
    create_reader_table_sql,
    create_admin_table_sql,
    create_publisher_table_sql,
    create_borrow_table_sql,
    create_manage_table_sql,
]


def init_db():
    database_connection = connect2db()
    db_cursor = database_connection.cursor()
    for sql in SQLs:
        try:
            db_cursor.execute(sql)
        except Exception as e:
            print("Initialization Failed!")
            print(e)
    disconnect_db(database_connection)


if __name__ == '__main__':
    init_db()
