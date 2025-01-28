from src.datascienceproject.config.configuration import *
from src.datascienceproject.components.data_ingestion import *
from src.datascienceproject.components.data_validation import *

from src.datascienceproject import logger

STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config=ConfigurationManger()        
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()