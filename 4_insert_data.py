import csv
import glob
import os

import oracledb
from dotenv import load_dotenv

from src.oracle import oracle_params

""" this script performs bulk loading of the data by processing
individual csv files in the unzipped/production folder
"""

load_dotenv()

files = glob.glob(r"./unzipped/production/*.csv")

BATCH_SIZE = 10000

# connect to Oracle
connection = oracledb.connect(params=oracle_params, dsn=os.getenv('dsn'))

with connection.cursor() as cursor:
    for file in files:
        with open(file, "r", encoding="Latin1") as csv_file:
            cols = []
            data = []

            table_name = file.split("\\")[1]
            table_name = table_name.split(".")[0]
            table_name = table_name.replace("_rv", "")

            csv_reader = csv.reader(csv_file, delimiter=",")
            cols = next(csv_reader)

            length = range(1, len(cols) + 1)
            vals = [f":{i}," for i in length]
            vals = " ".join(str(e) for e in vals)
            vals = vals.rstrip(",")
            vals = "(" + vals + ")"

            sql = f"insert into {table_name} {*cols,} values {vals}"
            sql = sql.replace("'", "")

            print(table_name)

            for row in csv_reader:
                if row[-1] == "":
                    row = row[:-1]
                data.append(row)
                if len(data) % BATCH_SIZE == 0:
                    cursor.executemany(sql, data)
                    data = []
                    cols = []
            if data:
                cursor.executemany(sql, data)
            connection.commit()
