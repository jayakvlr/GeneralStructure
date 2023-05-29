import pickle
from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import PredictPipeline,CustomData
from sklearn.preprocessing import StandardScaler

application=Flask(__name__)

app=application
##Route for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predictdata():
    if request.method=='GET':
        return render_template('home.html')
    else :
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethinicity=request.form.get('race_ethinicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=request.form.get('reading_score'),
            writing_score=request.form.get('writing_score')
        )
    preddf=data.getdataasdf()
    print("dff",preddf)
    pred_pipeline=PredictPipeline()
    results=pred_pipeline.predict(preddf)
    print("pred_score",results)
    return render_template('home.html',results=results[0])
if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)


