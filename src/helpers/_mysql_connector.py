import pymysql
from sqlalchemy import create_engine

from src.helpers.config import Config

config = Config().get_credentials()


class MysqlConnector:
    def __init__(self):
        pass

    def get_connection_dq(self, host, user, password, port, database):
        try:
            conn = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
            print(f"SUCCESS: Connection to the {database} database is successful")
            return conn
        except Exception as e:
            print("ERROR: Unexpected error: Could not connect to MySql instance. \n" + str(e))
            raise Exception(e)

    def get_db_connection(self, database):
        host = config["db_details"]["db_host"]
        username = config["db_details"]["db_username"]
        password = config["db_details"]["db_password"]
        port = config["db_details"]["db_port"]
        return self.get_connection_dq(host, username, password, port, database)
