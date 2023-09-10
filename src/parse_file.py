import pandas as pd
import warnings


def create_table_query(file):
    warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

    table_name = file.split("\\")[1]
    table_name = table_name.split(".")[0]

    try:
        df = pd.read_excel(
            file, sheet_name=1, usecols=["varname", "Fieldwidth", "imputationvar"]
        )
        dict = df[["imputationvar", "Fieldwidth"]]
        dict = dict.dropna(subset=["imputationvar"])
        dict = dict.rename(columns={"imputationvar": "varname"})

        final = [df[["varname", "Fieldwidth"]], dict]
        final_df = pd.concat(final)
        zipped = zip(final_df.varname.values, final_df.Fieldwidth.values)

    except:
        df = pd.read_excel(file, sheet_name=1, usecols=["varname", "Fieldwidth"])
        zipped = zip(df.varname.values, df.Fieldwidth.values)

    sql = ""
    for value, width in zipped:
        if value in ["ATHURL", "CHFTITLE"]:
            sql = sql + value + f" varchar({width + 50}),"
        else:
            sql = sql + value + f" varchar({width + 15}),"
    sql = sql.rstrip(",")
    query = f"create table {table_name} ({sql})"

    return query
