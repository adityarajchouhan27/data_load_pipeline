import os
from datetime import datetime
import pandas as pd

from src.helpers.constants import Constants
from src.helpers.data_operation import DataOperations
from src.incremental.incremental import Incremental
from src.app.app_metadata import MetadataApp


class DataPipelineApp:
    def __init__(self, entity, load_type):
        self.__entity = entity
        self.__load_type = load_type
        self.__meta = MetadataApp(self.__entity)
        self.__const = Constants()
        self.__incr = Incremental(self.__entity)
        self.__data_ops = DataOperations()

    def common_datapipeline(self, path):
        print(f"Starting {self.__entity} table run for landing")
        self.load_csv_to_database(file_path=path)

    def load_csv_to_database(self, file_path):
        max_date = None
        filepath = os.getenv(file_path)
        print(f"File path : {filepath}")
        fields = self.__meta.get_mapping_fields(self.__meta.get_landing_parameters())
        db_name, tbl_name = self.__meta.get_destination_parameters(self.__meta.get_landing_parameters())
        conn = self.__meta.get_destination_db_connection()
        x = "start"
        row_count = 0
        print("Reading csv and Putting the data into database table")
        self.__data_ops.set_database_connection(conn)
        if self.__load_type.upper() == self.__const.LOAD_TYPE_INCR.upper():
            incr_date = self.__incr.get_incremental_date()
        insert_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for chunk in pd.read_csv(filepath, chunksize=self.__const.CHUNK_SIZE, low_memory=False):
            if x == "start":
                file_fields = chunk.columns
                fields_to_fetch = list(set(fields.split(",")) & set(file_fields))
                print(f"Fields loading to table : {fields_to_fetch}")
                x = "close"

            chunk = chunk[fields_to_fetch]
            column = self.__meta.get_incremental_fields(self.__meta.get_landing_parameters())
            chunk[column] = pd.to_datetime(chunk[column])
            alter_type_datetime_cols = self.__meta.get_datetime_fields(self.__meta.get_landing_parameters())
            for col in alter_type_datetime_cols:
                chunk[col] = pd.to_datetime(chunk[col])
            chunk["insert_date"] = insert_date
            from_count = row_count

            if self.__load_type.upper() == self.__const.LOAD_TYPE_INCR.upper():
                chunk = chunk.loc[chunk[column] > incr_date]
            row_count = row_count + len(chunk.index)
            if max_date is None:
                if len(chunk.index) != 0:
                    max_date = chunk[column].max()
            elif max_date < chunk[column].max():
                max_date = chunk[column].max()
            self.__data_ops.replace_data(chunk, tbl_name)
            print(f"Table '{tbl_name}' loaded successfully from record {from_count} to {row_count}.")
        if max_date is not None:
            self.__incr.update_incremental_date(max_date)

    def developer_details_run(self, path):
        self.common_datapipeline(path)

    def devops_details_run(self, path):
        self.common_datapipeline(path)

    def tester_details_run(self, path):
        self.common_datapipeline(path)

