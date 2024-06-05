import glob

import pyodbc
from joblib import Parallel, delayed

from config import config 
from src.clear_tables import delete_table

""" this script deletes only tables that exist in the production folder;
    It doesn't not delete ALL the table in the database.
    !!! Use sql script to delete all tables in the schema.
"""

# let's create individual statements
files = glob.glob(r"./unzipped/production/*.xls*")

data_tables = Parallel(n_jobs=-1, verbose=10)(
    delayed(delete_table)(file) for file in files
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
            print("tables deleted successfully!")

