import glob

import pyodbc
from joblib import Parallel, delayed

from config import config 
from src.clear_tables import truncate_table

""" this script truncates only tables that exist in the production folder;
    It doesn't not truncate ALL the table in the database.
    !!! Use sql script to truncate all tables in the schema.
"""


# let's create individual statements
files = glob.glob(r"./unzipped/production/*.xls*")

data_tables = Parallel(n_jobs=-1, verbose=10)(
    delayed(truncate_table)(file) for file in files
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
            print("tables truncated successfully!")

