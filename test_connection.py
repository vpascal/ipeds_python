
import os

import oracledb
from dotenv import load_dotenv

from src.oracle import oracle_params

load_dotenv()

# connect to Oracle
connection = oracledb.connect(params=oracle_params, dsn=os.getenv('dsn'))

with connection.cursor() as cursor:
    for row in cursor.execute("select 'hello','world' from dual"):
        print(row)