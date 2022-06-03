import hashlib


def md5_encrypt(message: str) -> str:
    hashlib_objection = hashlib.md5()
    hashlib_objection.update(message.encode(encoding='utf-8'))
    return hashlib_objection.hexdigest()


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
