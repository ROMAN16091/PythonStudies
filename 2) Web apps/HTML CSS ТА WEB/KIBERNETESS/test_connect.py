import psycopg2

try:
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432',
    )
    print('ok')
    conn.close()
except Exception as e:
    print(e)