import os
import sys
from src.logger import logging
from src.exception import CustomException
#from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import pandas as pd
import numpy as np
#from pymongo import MongoClient
from src.utils import split_data

@dataclass                          #no need of init to define class variables
class DataIngestionConfig:
    train_data_path:str=os.path.join("artifact",'train.csv')
    test_data_path:str=os.path.join("artifact",'test.csv')
    raw_data_path:str=os.path.join("artifact",'data.csv')

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered iniate_data_ingestion method")
        try:
            #df=pd.read_csv('C:\Users\pende\OneDrive\Desktop\mlpjct\notebook\data\stud.csv')
            df=pd.read_csv('notebook/data/stud.csv')

            logging.info("Read the data(csv) as dataframe")

            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True)
            os.makedirs(os.path.dirname(self.data_ingestion_config.test_data_path),exist_ok=True)
            os.makedirs(os.path.dirname(self.data_ingestion_config.test_data_path),exist_ok=True)

            #df.to_csv(os.path.dirname(self.data_ingestion_config.raw_data_path))
            df.to_csv(self.data_ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")

            train_set,test_set=split_data(df)
            train_set.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of data completed")

            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info("Error in iniate_data_ingestion method")
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()