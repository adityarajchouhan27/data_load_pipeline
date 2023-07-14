import datetime as datetime
import json
import os
import pathlib

# import boto3
from dotenv import load_dotenv


class Utility:
    def __init__(self):
        # self.ssm_client = boto3.client("ssm")
        load_dotenv()

    def get_ssm_parameters(self, parameter_name):
        return self.ssm_client.get_parameter(Name=parameter_name, WithDecryption=True)["Parameter"]["Value"]

    def get_env_parameters(self, env_var):
        return os.getenv(env_var)

    def get_schema_from_file(self, path_env_var):
        file_path = os.getenv(path_env_var)
        print("file_path:", file_path)
        file = open(file_path)
        schema = json.load(file)
        return schema

    def list_to_comma_string(self, list):
        return ",".join(list)
