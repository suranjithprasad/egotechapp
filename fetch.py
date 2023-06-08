import psycopg2
conn = psycopg2.connect(
    host='localhost',
    dbname='test',
    user='postgres',
    password='1234'
)
cursor = conn.cursor()
cursor.execute('SELECT * FROM submission')
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()
