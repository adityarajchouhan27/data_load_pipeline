from src.helpers.utility import Utility

# initialize logger

Utility = Utility()

class Config:
    def __init__(self) -> None:
        pass

    def get_credentials(self):
        # Get Database credentials

        db_host = Utility.get_env_parameters("DB_HOST")

        db_username = Utility.get_env_parameters("DB_USERNAME")

        db_password = Utility.get_env_parameters("DB_PASSWORD")

        db_port = Utility.get_env_parameters("DB_PORT")

        config = {
            "db_details": {
                "db_host": db_host,
                "db_username": db_username,
                "db_password": db_password,
                "db_port": db_port,
            },
        }

        return config
