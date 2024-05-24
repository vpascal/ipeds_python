import keyring

base_url = 'https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx?year='

# 2013 to 2021
years =  [i for i in range(2022,2023)]

data_url = 'https://nces.ed.gov/ipeds/datacenter/data/'

db_password = keyring.get_password('odwp', 'password')
dsn = f"DSN=ODWP;PWD={db_password}"