from src.helpers.constants import Constants
from src.app.app_datapipeline import DataPipelineApp


class DataPipelineMain:
    def __init__(self, entity, load_type):
        self.__entity = entity
        self.__load_type = load_type
        self.__const = Constants()
        self.__datapipeline_entity = DataPipelineApp(self.__entity, self.__load_type)

    def run_data_pipeline_process(self):
        print(f"Starting loading process for {self.__entity}")

        if self.__entity.upper() == self.__const.TB_SF_DEVELOPER_DTL.upper():
            self.__datapipeline_entity.developer_details_run("DATAPIPELINE_DEVELOPER_DTL_FP")
        elif self.__entity.upper() == self.__const.TB_SF_DEVOPS_DTL.upper():
            self.__datapipeline_entity.devops_details_run("DATAPIPELINE_DEVOPS_DTL_FP")
        elif self.__entity.upper() == self.__const.TB_SF_TESTER_DTL.upper():
            self.__datapipeline_entity.tester_details_run("DATAPIPELINE_TESTER_DTL_FP")
        else:
            raise Exception(f"Please verify the table provided for {self.__entity}")
