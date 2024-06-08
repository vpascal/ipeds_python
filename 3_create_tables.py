import glob
import os

from dotenv import load_dotenv
from joblib import Parallel, delayed
from oracledb import IntegrityError, connect

from src.oracle import oracle_params
from src.parse_file import create_table_query

load_dotenv()

""" this script creates empty tables in the Oracle db
by reading 'table schema' from individual Excel files.
Refer to create_table_function for more detailed information.
"""


# let's create individual "create table ..." statements
files = glob.glob(r"./unzipped/production/*.xls*")

# create tables in parallel
data_tables = Parallel(n_jobs=-1, verbose=10)(
    delayed(create_table_query)(file) for file in files
)

# connect to Oracle
connection = connect(params=oracle_params, dsn=os.getenv('dsn'))

with connection.cursor() as cursor:
    for table in data_tables:
        try:
            cursor.execute(table)
        except IntegrityError:
            print("integrity issues!")
        else:
            print("table created")
