# Data Ingestion is all about training, testing and splitting data

import pandas as pd
import os
import sys
from src.exception import CustomException
from src.logger import logging

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# inputs for data ingestion like inputting raw data so We should create a class

#decorator to directly define class variable
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")
    

class DataIngestion:
    def __init__(self):
        # to save the entire paths at DataIngesitonConfig in variable
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        
        try:
            #read the dataset
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info("Read the datasets as dataframe")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok = True)
            #converted to csv
            df.to_csv(self.ingestion_config.raw_data_path,index = False, header=True)
            
            logging.info("Train test split initiated")
            #train test and split
            train_set,test_set = train_test_split(df, test_size=0.2, random_state= 42)
            
            #saved the train file
            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            
            #saved the test file
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)
            
            #comments
            logging.info("Ingestion of data is completed")
            
            #returning test and train data
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    o = DataIngestion()
    o.initiate_data_ingestion()