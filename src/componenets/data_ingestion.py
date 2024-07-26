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
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info("Read the datasets as dataframe")
        except:
            pass