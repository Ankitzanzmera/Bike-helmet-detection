import sys
from Bike_helmet_detection.config.configuration import ConfigrationManager
from Bike_helmet_detection.components.data_ingestion import DataIngestion
from Bike_helmet_detection.utils.exception import CustomException
from Bike_helmet_detection.utils.logger import logger

class DataIngestionPipeline:
    def main(self):
        try:
            config = ConfigrationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_file()
        except Exception as e:
            raise CustomException(e,sys)
        
STAGE_NAME = "Data_Ingestion"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info("-"*70)
    except Exception as e:
        raise CustomException(e,sys)
    
