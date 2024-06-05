import csv
import glob

import pandas as pd
import pyodbc
from joblib import Parallel, delayed

from config import config
from src.data_dict import create_dictionary

""" this script goes through all Excel files reading the data,
processing it, saving it as csv file in unzipped/production/ipeds_data_dictionary.csv
and then loading it into Oracle db.
"""


files = glob.glob(r"./unzipped/production/*.xls*")
data_file = "./unzipped/ipeds_data_dictionary.csv"
BATCH_SIZE = 1000

dicts = Parallel(n_jobs=-1, verbose=10)(
    delayed(create_dictionary)(file) for file in files
)
df = pd.concat(dicts)
df.to_csv(data_file, index=False)


# connect to Oracle
connection = pyodbc.connect(config.dsn)

with connection.cursor() as cursor:
    # let's create a table
    cursor.execute(
        "create table ipeds_data_dictionary (\
               years varchar(5), ipeds_table varchar(25),\
               varname varchar(25), varTitle varchar(255),\
               longDescription clob)"
    )

    # insert the data
    with open(data_file, "r", encoding="Latin1") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")

        sql = (
            "insert into ipeds_data_dictionary (years, ipeds_table, varname, varTitle, longDescription)\
              values (:1, :2, :3, :4, :5)"
        )

        data = []
        for row in csv_reader:
            data.append(row)
            if len(data) % BATCH_SIZE == 0:
                cursor.executemany(sql, data)
                data = []
        if data:
            cursor.executemany(sql, data)
        connection.commit()
