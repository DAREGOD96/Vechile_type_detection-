import sys
from src.VehicleTypeDetection.logger import logging
from src.VehicleTypeDetection.exception import CustomException
from src.VehicleTypeDetection.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

stage_name="Data_ingesiton_staeg"

if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {stage_name} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise CustomException(e,sys)