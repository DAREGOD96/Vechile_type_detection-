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
    input_shape: list
    num_classes: int
    kernel_size: int
    learning_rate: float

