import sys
from src.VehicleTypeDetection.config.configuration import ConfigurationManager
from src.VehicleTypeDetection.components.prepare_base_model import PrepareBaseModel
from src.VehicleTypeDetection.logger import logging
from src.VehicleTypeDetection.exception import CustomException

STAGE_NAME="Prepare_Base_Model"
class PrepareBaseModelPipline:
    def __init__(self) -> None:
        pass

    def main(self):
        configuration_manager_object=ConfigurationManager()
        get_prepare_base_model_object=configuration_manager_object.get_prepare_base_model()
        prepare_base_model_object=PrepareBaseModel(config=get_prepare_base_model_object)
        prepare_base_model_object.get_base_model()
        prepare_base_model_object.update_base_model()


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