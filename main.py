import sys
from src.VehicleTypeDetection.logger import logging
from src.VehicleTypeDetection.exception import CustomException
from src.VehicleTypeDetection.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.VehicleTypeDetection.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipline
from src.VehicleTypeDetection.pipeline.stage_03_model_training import ModelTrainingPipeline
from src.VehicleTypeDetection.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline


stage_name="Data_ingesiton_staeg"

if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {stage_name} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise CustomException(e,sys)
    
STAGE_NAME="Prepare_Base_Model"
if __name__ == '__main__':
    try:
        logging.info(f"*******************")
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelPipline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise CustomException(e,sys)
    
STAGE_NAME="Model Training"
if __name__ == '__main__':
    try:
        logging.info(f"*******************")
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise CustomException(e,sys)
    
STAGE_NAME="Model Evalution"
if __name__ == '__main__':
    try:
        logging.info(f"*******************")
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise CustomException(e,sys)