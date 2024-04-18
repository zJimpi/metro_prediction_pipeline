import sys 
import os 
from src.exception import CustomException 
from src.logger import logging 
from src.utils import load_obj
import pandas as pd

class PredictPipeline: 
    def __init__(self) -> None:
        pass

    #for prediction of new unseen data this is called by app.py 
    def predict(self, features): 
        try: 
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            model_path = os.path.join("artifacts", "model.pkl")

            preprocessor = load_obj(preprocessor_path)
            model = load_obj(model_path)
            #debugging
            # print("Input data shape:", features.shape)
            # print("Input data:", features)

            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        except Exception as e: 
            logging.info("Error occured in predict function in prediction_pipeline location")
            raise CustomException(e,sys)
        
class CustomData: 
        def __init__(self,TP2:float,TP3:float, H1:float,DV_pressure:float,Reservoirs:float,Oil_temperature:float,Motor_current:float,COMP:float,DV_eletric:float,Towers:float,MPG:float,LPS:float,Pressure_switch:float,Oil_level:float): 
            self.TP2 = TP2
            self.TP3 = TP3
            self.H1 = H1
            self.DV_pressure = DV_pressure
            self.Reservoirs = Reservoirs
            self.Oil_temperature = Oil_temperature
            self.Motor_current = Motor_current
            self.COMP = COMP
            self.DV_eletric = DV_eletric
            self.Towers = Towers
            self.MPG = MPG
            self.LPS = LPS
            self.Pressure_switch = Pressure_switch
            self.Oil_level = Oil_level
             
        
        def get_data_as_dataframe(self): 
            try: 
                custom_data_input_dict = {
                    'TP2':[self.TP2], 
                    'TP3':[self.TP3], 
                    'H1':[self.H1], 
                    'DV_pressure':[self.DV_pressure], 
                    'Reservoirs':[self.Reservoirs], 
                    'Oil_temperature':[self.Oil_temperature],
                    'Motor_current':[self.Motor_current], 
                    'COMP':[self.COMP], 
                    'DV_eletric':[self.DV_eletric], 
                    'Towers':[self.Towers], 
                    'MPG':[self.MPG], 
                    'LPS':[self.LPS],
                    'Pressure_switch':[self.Pressure_switch], 
                    'Oil_level':[self.Oil_level], 
                }
                df = pd.DataFrame(custom_data_input_dict)
                logging.info("Dataframe created")
                return df

            except Exception as e:
                logging.info("Error occured in get_data_as_dataframe function in prediction_pipeline")
                raise CustomException(e,sys) 

#testing
# Sample data
# sample_data = {
#     'TP2': -0.012,
#     'TP3': 9.148,
#     'H1': 9.136,
#     'DV_pressure': -0.021,
#     'Reservoirs': 9.148,
#     'Oil_temperature': 57.89,
#     'Motor_current': 0.042,
#     'COMP': 1.0,
#     'DV_eletric': 0.0,
#     'Towers': 1.0,
#     'MPG': 1.0,
#     'LPS': 0.0,
#     'Pressure_switch': 1.0,
#     'Oil_level': 1.0
# }

# # Instantiate CustomData
# custom_data = CustomData(**sample_data)

# # Convert to DataFrame
# sample_df = custom_data.get_data_as_dataframe()

# # Instantiate PredictPipeline
# predict_pipeline = PredictPipeline()

# # Call predict method
# predictions = predict_pipeline.predict(sample_df)

# # Inspect results
# print("Predictions:", predictions)
