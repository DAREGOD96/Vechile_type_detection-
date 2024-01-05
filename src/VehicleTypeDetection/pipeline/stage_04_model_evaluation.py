from src.VehicleTypeDetection.config.configuration import ConfigurationManager
from src.VehicleTypeDetection.components.model_evaluation import Evaluation
from src.VehicleTypeDetection.logger import logging
from src.VehicleTypeDetection.exception import CustomException
import sys
class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        configuration_manager_object=ConfigurationManager()
        get_model_evaluation_config=configuration_manager_object.get_model_evaluation_config()
        evaluation_object=Evaluation(get_model_evaluation_config)
        evaluation_object.model_evaluation()
        evaluation_object.save_score()

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

