import os 
import sys 
import csv
import pickle 
import mysql.connector

from src.exception import CustomException
from sklearn.metrics import r2_score
from src.logger import logging

#import data from sql
def import_sqlData():
    mydb = mysql.connector.connect(host='localhost',user='root',password='',database='metro')
    query = "select * from metro_data;"
    mycursor= mydb.cursor()
    mycursor.execute(query)
    result= mycursor.fetchall()
    
    data_folder_path = "../data"
    os.makedirs(data_folder_path, exist_ok=True)
    file_path = os.path.join(data_folder_path, "metro.csv")

    #func to convert dat stored in result to csv format
    with open(file_path, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in mycursor.description])  # for column headers
        csv_writer.writerows(result) # for data




# this file is sused by everyone
def save_function(file_path, obj): 
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok= True)
    with open (file_path, "wb") as file_obj: 
        pickle.dump(obj, file_obj)

def model_performance(X_train, y_train, X_test, y_test, models): 
    try: 
        report = {}
        for i in range(len(models)): 
            model = list(models.values())[i]
            # Train models
            model.fit(X_train, y_train)
            # Test data
            y_test_pred = model.predict(X_test)
            #R2 Score 
            test_model_score = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = test_model_score
        return report

    except Exception as e: 
        raise CustomException(e,sys)

# Function to load a particular object 
def load_obj(file_path):
    try: 
        with open(file_path, 'rb') as file_obj: 
            return pickle.load(file_obj)
    except Exception as e: 
        logging.info("Error in load_object fuction in utils")
        raise CustomException(e,sys)

