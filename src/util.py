import os
import sys
import pandas as pd
import numpy as np
from src.exception import CustomException
from sklearn.metrics import r2_score
from skopt import BayesSearchCV
import dill
class Utils:
    def save_object(self,filepath,obj):
        try:
            dir_path=os.path.dirname(filepath)
            os.makedirs(dir_path,exist_ok=True)
            with open(filepath,"wb") as f:
                dill.dump(obj,f)
        except Exception as e:
            raise CustomException(e,sys)
    def eval_model(self,X_train,y_train,X_test,y_test,models,model_params):
        report={}
        try:
                
            for i in range(len(list(models))):
                model = list(models.values())[i]
                para=model_params[list(models.keys())[i]]
                if para=={}:
                    model.fit(X_train,y_train)
                    y_test_pred=model.predict(X_test)
                else:
                    bayes_cv=BayesSearchCV(model,para,cv=3, n_jobs=-1, n_points=15)
                    bayes_cv.fit(X_train,y_train)
                    model.set_params(**bayes_cv.best_params_)
                    model.fit(X_train,y_train)
                    y_test_pred=model.predict(X_test)
                    #train_r2_score=r2_score(y_train,y_train_pred)
                test_r2_score=r2_score(y_test,y_test_pred)
                report[list(models.keys())[i]] = test_r2_score
            return report
        except Exception as e:
            raise CustomException(e,sys)
    def load_object(self,filepath):
        try:
            with open(filepath,"rb") as f:
                return dill.load(f)
        except Exception as e:
            raise CustomException(e,sys)