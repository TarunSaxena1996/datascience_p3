from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.data_ingestion import DataIngestion
import os





if __name__=="__main__":
    
    print(f"📍 Actually running: {__file__}")
    print(f"📁 Current working directory: {os.getcwd()}")
    print("Running pipeline file...")
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))