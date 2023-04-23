import os # for file creation
import sys # for errors that occour
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
## Initiliaze the data ingestion configuration

"""
Because here we will not have any function in the class that is why we are using dataclass.

The dataclasses module in Python  provides a decorator and a set of tools for quickly defining classes 
that are primarily intended to store data.

"""

@dataclass
class DataIngestionconfig:
    """os.path provides a set of functions for working with file and directory paths in a platform-independent way."""
    train_data_path:str=os.path.join('artifacts','train.csv')# this is the train data path
    # artifacts is a folder that will have all the files that we will store example:- pickle, train, test
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')
# THE ENTIRE CONFIG WILL BE SEND TO DATA INGESTION AND FOR THAT WE WILL CREATE A CLASS\


# CREATING CLASS FOR DATA INGESTION

## create a class for Data Ingestion
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion methods Starts')
        try:
            df=pd.read_csv(os.path.join('notebooks/data','gemstone.csv'))
            logging.info('Dataset read as pandas Dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info('Train test split')
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of Data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
  
            
        except Exception as e:
            logging.info('Exception occured at Data Ingestion stage')
            raise CustomException(e,sys)
        



    
