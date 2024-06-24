import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import CustomException
import os
import sys
from sklearn.model_selection import train_test_split

from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join('artifacts','raw.csv')
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    
    


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info('Data Ingestion initiated')
        try:
            data="data/train.csv"
            # if not os.path.exists(data):
            #     raise FileNotFoundError('Data not found')
            data = pd.read_csv(data)
            logging.info('Importing and Reading Data')

            
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info('Saved the raw data in the artifact folder')
            
            logging.info('Splitting the data into train and test')
            
            train_data,test_data = train_test_split(data, test_size=0.25, random_state=42)
            logging.info('Data Splitting Completed')
            
            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)
            
            logging.info('Data Ingestion Completed')
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path)
        
        except Exception as e:
            logging.info('Data Ingestion Error')
            raise CustomException(e,sys)
    
    


if __name__=='main':
    obj = DataIngestion()
    
    obj.initiate_data_ingestion()
