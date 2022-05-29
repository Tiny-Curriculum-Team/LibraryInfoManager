def connect2db(host="192.168.192.1",
               port=3306,
               user="anyone",
               password="KeXie@5108space",
               database='LIMS',
               charset='utf8'):
    import pymysql
    pymysql.install_as_MySQLdb()
    db = pymysql.connect(host=host, port=port, user=user,
                         password=password, db=database, charset=charset)
    return db


def disconnect_db(db):
    cursor = db.cursor()
    cursor.close()
    db.close()
