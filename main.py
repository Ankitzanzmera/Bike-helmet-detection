import sys
from Bike_helmet_detection.utils.logger import logger
from Bike_helmet_detection.utils.exception import CustomException
from Bike_helmet_detection.pipelines.pipeline_01_data_ingestion import DataIngestionPipeline

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