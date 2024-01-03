import sys
from src.VehicleTypeDetection.config.configuration import ConfigurationManager
from src.VehicleTypeDetection.components.data_ingestion import DataIngestion
from src.VehicleTypeDetection.exception import CustomException
from src.VehicleTypeDetection.logger import logging


stage_name="Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        configuration_manager_object=ConfigurationManager()
        config=configuration_manager_object.get_data_ingestion_config()
        data_ingestion_object=DataIngestion(config=config)
        data_ingestion_object.extract_zip_file()

if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {stage_name} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise CustomException(e,sys)

        
