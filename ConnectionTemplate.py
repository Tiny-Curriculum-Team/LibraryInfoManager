import pymysql
pymysql.install_as_MySQLdb()

db = pymysql.connect(host="192.168.192.1",
                     port=3306,
                     user="anyone",
                     password="KeXie@5108space",
                     db='LIMS',
                     charset='utf8')
print("Connection Succeeded.")

cursor = db.cursor()

cursor.execute("""
        -- SQL语句
        """)

data = cursor.fetchall()

print(data)

