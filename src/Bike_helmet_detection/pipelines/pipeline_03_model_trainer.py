import sys  
from Bike_helmet_detection.utils.exception import CustomException
from Bike_helmet_detection.config.configuration import ConfigrationManager
from Bike_helmet_detection.components.model_trainer import ModelTrainer
from Bike_helmet_detection.utils.logger import logger

class ModelTrainerPipeline:
    def main(self):
        try:
            config = ConfigrationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(model_trainer_config)
            model_trainer.initiate_model_training()
        except Exception as e:
            raise CustomException(e,sys)
        

STAGE_NAME = "Model Trainer"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info("-"*70)
    except Exception as e:
        raise CustomException(e,sys)