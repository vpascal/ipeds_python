import pandas as pd
import warnings


def create_dictionary(file):
    warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

    table_name = file.split("\\")[1]
    table_name = table_name.split(".")[0]

    df = pd.read_excel(file, sheet_name=1, usecols=["varname", "varTitle"])
    df.insert(0, "ipeds_table", table_name)
    df.insert(0, "years", df.ipeds_table.str.extract(r"(\d{4})"))

    desc = pd.read_excel(file, sheet_name=2, usecols=["varname", "longDescription"])

    df_final = df.merge(desc, left_on="varname", right_on="varname")

    return df_final
