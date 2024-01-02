import sys
from Bike_helmet_detection.config.configuration import ConfigrationManager
from Bike_helmet_detection.components.data_validation import DataValidation
from Bike_helmet_detection.utils.exception import CustomException
from Bike_helmet_detection.utils.logger import logger


class DataValidationPipeline:
    def main(self):
        try:
            config = ConfigrationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(data_validation_config)
            data_validation.validate_all_file_exist()
        except Exception as e:
            CustomException(e,sys)
        
STAGE_NAME = "Data_Validation"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info("-"*70)
    except Exception as e:
        raise CustomException(e,sys)