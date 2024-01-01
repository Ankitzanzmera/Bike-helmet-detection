from Bike_helmet_detection.constants import *
from Bike_helmet_detection.utils.common import create_directories,read_yaml
from Bike_helmet_detection.entity.config_entity import (DataIngestionConfig)

class ConfigrationManager:
    def __init__(self,config_filepath = CONFIG_FILEPATH) -> None:
        self.config = read_yaml(config_filepath)
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        temp_config = self.config.data_ingestion

        create_directories([temp_config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = temp_config.root_dir,
            source = temp_config.source,
            local_data_file = temp_config.local_data_file,
            unzip_dir = temp_config.unzip_dir
        )

        return data_ingestion_config