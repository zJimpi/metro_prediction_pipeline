import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os
from src.utils import save_function


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('../../artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object(self):
        try:
            logging.info('Data Transformation initiated')
           
            #Segregating num and categorical cols 
            num_col =['TP2', 'TP3', 'H1','DV_pressure', 'Reservoirs','Oil_temperature','Motor_current']
            cat_col =['COMP', 'DV_eletric', 'Towers', 'MPG','LPS','Pressure_switch', 'Oil_level']
            
            
            logging.info('Pipeline Initiated')

            ## Numerical Pipeline
            num_pipe = Pipeline(
                steps = [
                ('imputer', SimpleImputer(strategy= 'median')), 
                ('scaler', StandardScaler())
                ]
            )

            cat_pipe = Pipeline(
                steps = [
                ('imputer', SimpleImputer(strategy='most_frequent')), 
                ('encoder', OneHotEncoder(handle_unknown='ignore'))  # to encode categorical features which are not in rank     
                ]

            )

            preprocessor = ColumnTransformer([
            ('num_pipe', num_pipe, num_col), 
            ('cat_pipe', cat_pipe, cat_col)
            ])
            
            return preprocessor

            logging.info('Pipeline Completed')

        except Exception as e:
            logging.info("Error in Data Trnasformation")
            raise CustomException(e,sys)


    def initiate_data_transformation(self,train_path,test_path):
        try:
            # Reading train and test data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('Read train and test data completed')
            logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head  : \n{test_df.head().to_string()}')

            logging.info('Obtaining preprocessing object')

            preprocessing_obj = self.get_data_transformation_object() # fetching preprocessor from previous method

            target_column_name = 'Caudal_impulses'
            drop_columns = [target_column_name,'id','timestamp']

            #EDA
            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_df[target_column_name]

            #EDA
            input_feature_test_df=test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df=test_df[target_column_name]
            
            ## Trnasformating using preprocessor obj
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            logging.info("Applying preprocessing object on training and testing datasets.")
            
            #converting to arrays in 2d format when columns are stacked
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_function(
                #path =artifacts/preprocesor.pkl 
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )
            logging.info('Preprocessor pickle file saved')

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
            
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise CustomException(e,sys)

#test
# obj =DataTransformation()
# obj.initiate_data_transformation('../../artifacts/train.csv','../../artifacts/test.csv')