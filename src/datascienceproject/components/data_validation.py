import os
import urllib.request as request
from src.datascienceproject import logger
from src.datascienceproject.entity.config_entity import *
import pandas as pd


class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}\n")
                    print("dataset is not valid")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}\n")

            return validation_status
        
        except Exception as e:
            raise e
    def validate_all_datatypes(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.items()
            print(all_schema)
            
            for col in all_cols:
                if data[col].dtype != self.config.all_schema[col]:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"data_Validation status: {validation_status}\n")
                    print("dataset is not valid")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"data_Validation status: {validation_status}\n")

            return validation_status
        
        except Exception as e:
            raise e
    