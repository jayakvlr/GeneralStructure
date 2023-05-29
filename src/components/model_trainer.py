#training model
import os
import sys
from  dataclasses import dataclass
import yaml
from catboost import CatBoostRegressor
from sklearn.ensemble import AdaBoostRegressor,RandomForestRegressor,GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.exception import CustomException
from src.logger import logging
from src.util import Utils

@dataclass
class ModelTrainerConfig:
    trained_model_path:str=os.path.join("artifacts","model.pkl")
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
    def initiate_model_trainer(self,train_ar,test_ar):
        try:
            logging.info("Initiating model training")
            logging.info("train test split")
            X_train,X_test,y_train,y_test=(train_ar[:,:-1],test_ar[:,:-1],train_ar[:,-1],test_ar[:,-1])
            models={
                "LinearRegression":LinearRegression(),
                "DecisionTreeRegressor":DecisionTreeRegressor(),
                "RandomForestRegressor":RandomForestRegressor(),
                "AdaBoostRegressor":AdaBoostRegressor(),
                "GradientBoostingRegressor":GradientBoostingRegressor(),
                "XGBRegressor":XGBRegressor(),
                "CatBoostRegressor":CatBoostRegressor(),
                "KNeighborsRegressor":KNeighborsRegressor(),
            }
            
            utils=Utils()
            model_report:dict=utils.eval_model(X_train,y_train,X_test,y_test,models,self.hyperparameter_tuning())
            best_model_score=max(sorted(model_report.values()))
            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model=models[best_model_name]
            if best_model_score<0.6:
                raise CustomException("None of the model is performing well")
            logging.info(f"Best model is {best_model_name} with score {best_model_score}")
            utils.save_object(self.model_trainer_config.trained_model_path,best_model)
            logging.info("Model saved")
            return best_model_name,best_model_score

        except Exception as e:
            logging.error(e)
            raise CustomException(e,sys)

    def hyperparameter_tuning(self):
        try:
            with open("src\hyperparams.yaml",'r') as f:
                hyperparams=yaml.safe_load(f)
            logging.info("Hyperparameter tuning started")
            return hyperparams
        except Exception as e:
            logging.error(e)
            raise CustomException(e,sys)
            
    def load_object(self,filepath):
        try:
            with open(filepath,"rb") as f:
                return dill.load(f)
        except Exception as e:
            raise CustomException(e,sys)