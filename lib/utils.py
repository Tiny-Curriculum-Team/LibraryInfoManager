def connect2db():
    import pymysql
    pymysql.install_as_MySQLdb()
    db = pymysql.connect(host="192.168.192.1",
                         port=3306,
                         user="anyone",
                         password="KeXie@5108space",
                         db='LIMS',
                         charset='utf8')
    return db


def disconnect_db(db):
    cursor = db.cursor()
    cursor.close()
    db.close()