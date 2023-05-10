#All related to data reading and ingestion
import os
import sys
from src import logger,exception
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException


##directly define class variables
@dataclass #if there is only variables in the class
class DataIngestionConifg:
    #Any raw inputs will be transformed through this class
    #This class will be used to define the data ingestion config
    #artifacts is the folder and train.csv is the file
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts","data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConifg()

    #Read from the DB
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")
        try:
            df=pd.read_csv('notebook\stud.csv')
            logging.info("data read as dataframe")
            #Creating directory if not exists for artifacts
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            #Dumping the raw data
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train Test split")
            train,test=train_test_split(df,test_size=.2,random_state=42)
            #Dumping the train data
            train.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            #Dumping the test data
            test.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Data Ingestion completed")
            return self.ingestion_config.train_data_path,self.ingestion_config.test_data_path
        except Exception as e:

            raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()
    print("Data Ingestion completed")






#%%
