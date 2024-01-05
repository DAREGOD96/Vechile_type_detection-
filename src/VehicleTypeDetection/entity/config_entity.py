from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir:Path
    local_data_file:Path
    unzip_dir:Path

@dataclass
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    input_shape: list
    num_classes: int
    include_top: bool
    weights: str
    learning_rate: float


@dataclass
class PrepareCallbackConfig:
    root_dir:Path
    tensorboard_root_log_dir:Path
    checkpoint_model_filepath:Path

@dataclass
class ModelTrainingConfig:
    root_dir: Path
    trained_model_path:Path
    updated_base_model_path: Path
    training_data: Path
    epochs: int
    batch_size: int
    is_augmentation: bool
    input_shape: list


@dataclass
class ModelEvaluationConfig:
    model_path:Path
    training_data:Path
    all_params:dict
    input_shape:list
    batch_size:int