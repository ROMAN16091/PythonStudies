import mysql.connector

# config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': 'medved1603'
# }
#
# cnx = mysql.connector.connect(**config)
#
# cursor = cnx.cursor()
#
# DB = 'shopdb'
# cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DB} DEFAULT CHARSET = "utf8mb4"')
# cnx.database = DB
#
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS products(
#     name VARCHAR(100),
#     price DECIMAL(10,2)
#
#     )
#
# """)
#
# cnx.commit()
# cnx.close()

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'medved1603',
    database = 'shopdb'
)

print('Connection ', conn.is_connected())
c = conn.cursor()
print(c.execute('SELECT * FROM products '))
print(c.fetchall())
conn.close()



