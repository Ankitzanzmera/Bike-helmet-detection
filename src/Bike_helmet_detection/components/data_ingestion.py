import os,sys
from zipfile import ZipFile
import gdown
from Bike_helmet_detection.utils.logger import logger
from Bike_helmet_detection.utils.exception import CustomException
from Bike_helmet_detection.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config : DataIngestionConfig) -> None:
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            gdown.download(self.config.source,self.config.local_data_file)
            logger.info(f"{self.config.local_data_file} Downloaded")
        else:
            logger.info(f"File Already Exists")
    
    def extract_file(self):
        with ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
        logger.info('zip file extracted successfully')


