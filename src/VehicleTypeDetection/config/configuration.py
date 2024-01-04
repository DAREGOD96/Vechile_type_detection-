import os
from src.VehicleTypeDetection.utils.constant import *
from src.VehicleTypeDetection.utils.common import read_yaml,create_directories
from src.VehicleTypeDetection.entity.config_entity import DataIngestionConfig,PrepareBaseModelConfig,PrepareCallbackConfig,ModelTrainingConfig

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
            updated_base_model_path=config.updated_base_model_path,
            input_shape=self.params_file.input_shape,
            num_classes=self.params_file.num_classes,
            include_top=self.params_file.include_top,
            weights=self.params_file.weights,
            learning_rate=self.params_file.learning_rate
        )

        return prepare_base_model
    
    def get_prepare_callback(self) -> PrepareCallbackConfig:
        config=self.config_file.prepare_callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        create_directories([
            Path(model_ckpt_dir),
            Path(config.tensorboard_root_log_dir)
        ])

        prepare_callback=PrepareCallbackConfig(
            root_dir=config.root_dir,
            tensorboard_root_log_dir=config.tensorboard_root_log_dir,
            checkpoint_model_filepath=config.checkpoint_model_filepath,
        )

        return prepare_callback
    
    def get_model_training_config(self) -> ModelTrainingConfig:
        training=self.config_file.model_training
        prepared_base_model_path=self.config_file.prepare_base_model
        params=self.params_file
        training_data=os.path.join(self.config_file.data_ingestion.unzip_dir,"Dataset")

        create_directories([training.root_dir])

        model_training_config=ModelTrainingConfig(
            root_dir=training.root_dir,
            trained_model_path=training.trained_model_path,
            updated_base_model_path=prepared_base_model_path.updated_base_model_path,
            training_data=training_data,
            epochs=params.epochs,
            batch_size=params.batch_size,
            is_augmentation=params.is_augmentation,
            input_shape=params.input_shape
        )

        return model_training_config



        

