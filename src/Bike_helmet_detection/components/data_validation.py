import os,sys
from Bike_helmet_detection.utils.logger import logger
from Bike_helmet_detection.utils.exception import CustomException
from Bike_helmet_detection.utils.common import read_yaml
from Bike_helmet_detection.constants import *
from Bike_helmet_detection.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self,data_validation_config:DataValidationConfig):
        self.data_validation_config = data_validation_config
        self.data_ingestion_config = read_yaml(CONFIG_FILEPATH).data_ingestion

    def validate_all_file_exist(self) -> bool:
        try:
            validation_status = None
            files_that_exists = os.listdir(self.data_ingestion_config.unzip_dir)
            required_file_list = self.data_validation_config.data_validation_required_file
            for file in required_file_list:
                if file not in files_that_exists:
                    validation_status  = False
                    with open(self.data_validation_config.data_validation_status_file,'w') as f:
                        f.write(f'Validation_status : {validation_status}')
                else:
                    validation_status  = True
                    with open(self.data_validation_config.data_validation_status_file,'w') as f:
                        f.write(f'Validation_status : {validation_status}')
            logger.info(f"Validation status file Created Successfully")
            if not validation_status:
                sys.exit("Exiting Due to Validation Failed")
        except Exception as e:
            raise CustomException(e,sys)