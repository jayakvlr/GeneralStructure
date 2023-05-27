import os
import sys
import pandas as pd
import numpy as np
from src.exception import CustomException
from sklearn.metrics import r2_score
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
    def eval_model(self,X_train,y_train,X_test,y_test,models):
        report={}
        try:
            
            for key,model in models.items():
                model=model.fit(X_train,y_train)
                y_train_pred=model.predict(X_train)
                y_test_pred=model.predict(X_test)
                #train_r2_score=r2_score(y_train,y_train_pred)
                test_r2_score=r2_score(y_test,y_test_pred)
                report[key]=test_r2_score
            return report
        except Exception as e:
            raise CustomException(e,sys)