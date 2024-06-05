def truncate_table(file):

    table_name = file.split("\\")[1]
    table_name = table_name.split(".")[0]

    query = f"truncate table {table_name}"

    return query

def delete_table(file):

    table_name = file.split("\\")[1]
    table_name = table_name.split(".")[0]

    query = f"drop table {table_name}"

    return query