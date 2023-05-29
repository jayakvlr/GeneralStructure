import sys
import pandas as pd
from src.exception import CustomException
from src.util import Utils

class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            model_path="artifacts/model.pkl"
            preprocessor_path="artifacts/proprocessor.pkl"
            model=Utils().load_object(model_path)
            preprocessor=Utils().load_object(preprocessor_path)
            data_scales=preprocessor.transform(features)
            return model.predict(data_scales)
        except Exception as e:
            raise CustomException(e,sys)
class CustomData:
    def __init__(self,gender :str,
    race_ethinicity:str,parental_level_of_education:str,
    lunch:str,test_preparation_course:str,reading_score:int,
    writing_score:int):
        self.gender=gender
        self.race_ethinicity=race_ethinicity
        self.parental_level_of_education=parental_level_of_education
        self.lunch=lunch
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score
    


    def getdataasdf(self):
        try:
            custon_datainput_dict={
                "gender":[self.gender],
                "race_ethnicity":[self.race_ethinicity],
                "parental_level_of_education":[self.parental_level_of_education],
                "lunch":[self.lunch],
                "test_preparation_course":[self.test_preparation_course],
                "reading_score":[self.reading_score],
                "writing_score":[self.writing_score]
                }

            return pd.DataFrame(custon_datainput_dict)

            
        except Exception as e:
            pass   

    