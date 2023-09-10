import keyring

base_url = 'https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx?year='

# 2013 to 2021
years =  [i for i in range(2013,2022)]

data_url = 'https://nces.ed.gov/ipeds/datacenter/data/'

db_username = 'ipeds'
db_password = keyring.get_password('oracle_cloud', 'db_password')
wallet_password = keyring.get_password('oracle_cloud', 'wallet_password')
