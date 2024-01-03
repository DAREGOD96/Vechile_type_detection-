from src.VehicleTypeDetection.utils.constant import *
from src.VehicleTypeDetection.utils.common import read_yaml,create_directories
from src.VehicleTypeDetection.entity.config_entity import DataIngestionConfig
from src.VehicleTypeDetection.logger import logging
class ConfigurationManager:
    def __init__(self,config_file_path=CONFIG_FILE_PATH,params_file_path=PARAMS_FILE_PATH):
        self.config_file=read_yaml(config_file_path)
        self.params_file=read_yaml(params_file_path)
        create_directories([self.config_file.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config_file.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
            root_dir = config.root_dir,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir     
        )
        return data_ingestion_config
        

