from src.helpers.data_operation import DataOperations
from src.helpers.utility import Utility
from src.helpers._mysql_connector import MysqlConnector


class MetadataApp:
    def __init__(self, entity):
        self.__entity = entity
        self.__utility = Utility()
        self.__mysql = MysqlConnector()
        self.__db_ops = DataOperations()

    def get_landing_parameters(self, **kwargs):
        entity = kwargs.get("entity", None)
        params = self.__utility.get_schema_from_file("APP_PARAMETERS")
        if entity is not None:
            params = params["entities"][entity]
        else:
            params = params["entities"][self.__entity]
        return params

    def get_destination_parameters(self, params):
        return params["destination"]["database_name"], params["destination"]["table_name"]

    def get_mapping_fields(self, params):
        fields = list(params["mapping"].keys())
        fields = self.__utility.list_to_comma_string(fields)
        return fields

    def get_datetime_fields(self, params):
        return params["alter_type_datetime_cols"]

    def get_incremental_fields(self, params, **kwargs):
        return params["incremental"]["column"]

    def get_destination_db_connection(self, **kwargs):
        entity = kwargs.get("entity", None)
        if entity is not None:
            dst_db, dst_tbl = self.get_destination_parameters(self.get_landing_parameters(entity=entity))
        else:
            dst_db, dst_tbl = self.get_destination_parameters(self.get_landing_parameters())
        return self.__mysql.get_db_connection(dst_db)
