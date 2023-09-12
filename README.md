These scripts download IPEDS data files and upload them to Oracle database.

To run
 - create virtual enviroments e.g. ```pip venv env``` and activate it e.g. ```env\scripts\activate```
 - install requirements ```pip install -r requirements.txt```
 - modify the config file as necessarily and then run individual scripts in this order:
   
    - 1_download_files.py (donwloads data files)
    - 2_move_files.py (moves data files in specific folders)
    - 3_create_tables.py (creates tables in Oracle)
    - 4_insert_data.py (loads the data into tables)
    - 5_create_data_dict.py (creates data dictionary)

When working with Oracle, modify your the settings* adding your password, schema, and dsn.
 * create .env file for dsn and wallet and also modify the config file .
