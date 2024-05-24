import pyodbc

from config import config

""" this is just a test connection to Oracle server"""

# connect to Oracle
connection = pyodbc.connect(config.dsn)

with connection.cursor() as cursor:
    cursor.execute("select 'hello','world' from dual")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
