import os
from Bike_helmet_detection.utils.logger import logger
from Bike_helmet_detection.constants import *
from Bike_helmet_detection.utils.common import read_for_yolo,save_yaml,read_yaml_file
from Bike_helmet_detection.entity.config_entity import ModelTrainerConfig
import subprocess

class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig) -> None:
        self.model_trainer_config = config
        self.data_ingestion_config = read_yaml_file(CONFIG_FILEPATH).data_ingestion
        # self.data_ingestion_config = read_yaml(CONFIG_FILEPATH).data_ingestion
    
    def __clone_repository(self):
        os.system("git clone https://github.com/ultralytics/yolov5.git")

    def __get_num_classes(self):
        nc = read_for_yolo(self.model_trainer_config.dataset_yaml_file,check="nc")
        return nc

    def initiate_model_training(self):
        ###### Remove .git file from yolov5 manually using file explorer #######

        num_classes = self.__get_num_classes()
        logger.info('Got num_classes')

        if not "yolov5" in os.listdir(os.getcwd()):
            self.__clone_repository()
            logger.info('Cloned Yolov5 repository')
        else:
            logger.info('Yolov5 repository is already exist..')
        
        model_name = self.model_trainer_config.model_pretrained_weight_name.split(".")[0]
        yolo_model_config = read_for_yolo(f"yolov5/models/{model_name}.yaml")
        yolo_model_config['nc'] = num_classes

        save_yaml(f'yolov5/models/custom_{model_name}.yaml',yolo_model_config)
        logger.info('Saved Custom Yolo config')
        
        ##>>>>>>>>>>>>>>>>>>>>>>> Use Git Bash for following Commands <<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        os.system(f"cp {self.data_ingestion_config.local_data_file} {os.getcwd()}")
        os.system(f"unzip data.zip")


        os.system(f"cd yolov5/ && python train.py --img 416 --batch {self.model_trainer_config.BATCH_SIZE} --epochs {self.model_trainer_config.EPOCHS} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.model_trainer_config.model_pretrained_weight_name} --name yolov5_results --cache")
        os.system(f"cp yolov5/runs/train/yolov5_results/weights/best.pt {self.model_trainer_config.root_dir}")

        os.system("rm -rf test")
        os.system("rm -rf train")
        os.system("rm -rf valid")
        os.system("rm -rf data.yaml")
        os.system("rm -rf data.zip")
        os.system("rm -rf yolov5/runs")   






