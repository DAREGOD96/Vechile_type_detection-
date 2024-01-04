from src.VehicleTypeDetection.config.configuration import ConfigurationManager
from src.VehicleTypeDetection.components.prepare_callbacks import PrepareCallbacks
from src.VehicleTypeDetection.components.model_training import ModelTraining
from src.VehicleTypeDetection.logger import logging
from src.VehicleTypeDetection.exception import CustomException
import sys

STAGE_NAME="Model Training"
class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config_object=ConfigurationManager()
        get_prepare_callback=config_object.get_prepare_callback()
        prepare_callback_object=PrepareCallbacks(config=get_prepare_callback)
        callback_list=prepare_callback_object.get_tb_ckpt_callbacks()

        training_config=config_object.get_model_training_config()
        model_training_object=ModelTraining(config=training_config)
        model_training_object.get_base_model()
        model_training_object.train_validaiton_data_generator()
        model_training_object.train(callback_list=callback_list)


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
