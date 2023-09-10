import oracledb
import os
from config import config
from dotenv import load_dotenv

load_dotenv()


oracle_params = oracledb.ConnectParams(
    user=config.db_username,
    password=config.db_password,
    wallet_location=os.getenv("wallet_location"),
    wallet_password=config.wallet_password,
)
