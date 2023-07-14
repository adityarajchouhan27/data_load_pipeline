from src.helpers.data_operation import DataOperations
from src.helpers.utility import Utility
from src.helpers._mysql_connector import MysqlConnector


class Incremental:
    def __init__(self, entity):
        self.__entity = entity
        self.__incr_params = Utility().get_schema_from_file("INCREMENTAL_PARAMETERS")
        self.__db_ops = DataOperations()
        self.__mysql = MysqlConnector()

    def get_incremental_param(self):
        return self.__incr_params["database_name"], self.__incr_params["table_name"]

    def get_incremental_date(self, **kwargs):
        entity = kwargs.get("entity", None)
        db_name, tbl_name = self.get_incremental_param()
        conn = self.__mysql.get_db_connection(db_name)
        query = f"""
            SELECT max_date
            FROM `{db_name}`.`{tbl_name}`
            WHERE
                table_name = "{entity if entity is not None else self.__entity}"
        """
        self.__db_ops.set_database_connection(conn)
        df = self.__db_ops.get_data(query)
        print(f"Incremental Date fetched successfully from table '{tbl_name}'")
        return str(df.loc[0, "max_date"])

    def update_incremental_date(self, date, **kwargs):
        entity = kwargs.get("entity", None)
        db_name, tbl_name = self.get_incremental_param()
        conn = self.__mysql.get_db_connection(db_name)
        query = f"""
            UPDATE `{db_name}`.`{tbl_name}`
            SET max_date = "{date}"
            WHERE
                table_name = "{entity if entity is not None else self.__entity}"
        """
        self.__db_ops.set_database_connection(conn)
        self.__db_ops.run_raw_query(query)
        print(f"Incremental Date updated successfully in table '{tbl_name}'")
