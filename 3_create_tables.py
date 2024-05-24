import glob
import pyodbc
import config 
from joblib import Parallel, delayed
from src.parse_file import create_table_query


""" this script creates empty tables in the Oracle db
by reading 'table schema' from individual Excel files.
Refer to create_table_function for more detailed information.
"""


# let's create individual "create table ..." statements
files = glob.glob(r"./unzipped/production/*.xls*")

data_tables = Parallel(n_jobs=-1, verbose=10)(
    delayed(create_table_query)(file) for file in files
)


# connect to Oracle via ODBC
connection = pyodbc.connect(config.dsn)

with connection.cursor() as cursor:
    for table in data_tables:
        try:
            cursor.execute(table)
        except pyodbc.OperationalError:
            print("integrity issues!")
        else:
            print("table created")
