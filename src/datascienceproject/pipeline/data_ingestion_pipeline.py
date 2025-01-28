from src.datascienceproject.config.configuration import *
from src.datascienceproject.components.data_ingestion import *
from src.datascienceproject import logger


STAGE_NAME = "Data ingestion Stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config=ConfigurationManger()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


    
