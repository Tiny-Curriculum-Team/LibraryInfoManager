def connect_to_db(host="192.168.192.1",
                  port=3306,
                  user="anyone",
                  password="KeXie@5108space",
                  database=None,
                  charset='utf8'):
    import pymysql
    pymysql.install_as_MySQLdb()
    db = pymysql.connect(host=host, port=port, user=user, password=password, charset=charset) \
        if database is None else pymysql.connect(
            host=host, port=port, user=user,
            password=password, db=database, charset=charset
        )
    return db


def disconnect_db(db):
    cursor = db.cursor()
    cursor.close()
    db.close()


def execute_sql_script(cursor, file_path: str):
    with open(file_path, 'r') as f:
        sql_list = f.read().split(';')[:-1]
        for sql in sql_list:
            cursor.execute(sql)

