from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source:str
    local_data_file:Path
    unzip_dir:Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir:Path
    data_validation_status_file:Path
    data_validation_required_file:list

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir:Path
    model_pretrained_weight_name: str
    dataset_yaml_file:Path
    EPOCHS:int
    BATCH_SIZE:int