from src.VehicleTypeDetection.utils.constant import *
from src.VehicleTypeDetection.utils.common import read_yaml,create_directories
from src.VehicleTypeDetection.entity.config_entity import DataIngestionConfig,PrepareBaseModelConfig

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
    
    def get_prepare_base_model(self) -> PrepareBaseModelConfig:
        config=self.config_file.prepare_base_model
        create_directories([config.root_dir])

        prepare_base_model=PrepareBaseModelConfig(
            root_dir=config.root_dir,
            base_model_path=config.base_model_path,
            input_shape=self.params_file.input_shape,
            num_classes=self.params_file.num_classes,
            kernel_size=self.params_file.kernel_size,
            learning_rate=self.params_file.learning_rate
        )

        return prepare_base_model

        

