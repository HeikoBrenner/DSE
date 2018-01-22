from flask import Flask, jsonify, request
#from flask_sqlalchemy import SQLAlchemy
import model_datastore
import storage
import datascience
import pandas
import json
from pandas.io.json import json_normalize
import config
import model_cloudsql
#import time

#import os


app = Flask(__name__)

def get_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
    names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'Class']
    dataframe = pandas.read_csv(url, names=names)
    return dataframe

@app.route('/uploaddata')
def insert_data_intodb():

    dataframe = get_data()
    dataframe.preg = dataframe.preg.astype(str)
    dataframe.plas = dataframe.plas.astype(str)
    dataframe.pres = dataframe.pres.astype(str)
    dataframe.skin = dataframe.skin.astype(str)
    dataframe.test = dataframe.test.astype(str)
    dataframe.mass = dataframe.mass.astype(str)
    dataframe.pedi = dataframe.pedi.astype(str)
    dataframe.age = dataframe.age.astype(str)
    dataframe.Class = dataframe.Class.astype(str)
    model_cloudsql.create(dataframe)
    
    return "success!"

@app.route('/')
def check_online():    

    return 'DSE train app is online!'

@app.route('/',  methods=['GET'])
def check_online_rest():    

    return 'DSE train app is online!'

@app.route('/train', methods=['POST'])
def train_modell():
    request_json = request.get_json()
    parameter_runid = request_json['runid']
    parameter_postalcode = request_json['postalcode']
    parameter_horizon = request_json['horizon']
    
    # if parameter_postalcode == '1010' and parameter_horizon == '2':
    #     data = model_cloudsql.getdata(0, 10)
    # elif parameter_postalcode == '1020' and parameter_horizon == '2':
    #     data = model_cloudsql.getdata(10, 20)
    # elif parameter_postalcode == '1030' and parameter_horizon == '2':
    #     data = model_cloudsql.getdata(20, 30)
    # elif parameter_postalcode == '1040' and parameter_horizon == '2':
    #     data = model_cloudsql.getdata(30, 40)
    # elif parameter_postalcode == '1050' and parameter_horizon == '2':
    #     data = model_cloudsql.getdata(40, 50)
    # else:
    #     data = model_cloudsql.getdata(0, 100)

    # ds_dataframe = pandas.DataFrame(data)
    
    time.sleep(120)
    dataframe = get_data()
    model = datascience.trainmodel(dataframe)
    model = datascience.trainmodel(dataframe)
    model = datascience.trainmodel(dataframe)
    model = datascience.trainmodel(dataframe)
    model = datascience.trainmodel(dataframe)
    model = datascience.trainmodel(dataframe)
    model = datascience.trainmodel(dataframe)
    model = datascience.trainmodel(dataframe)
    model = datascience.trainmodel(dataframe)
    model = datascience.trainmodel(dataframe)
    model = datascience.trainmodel(dataframe)
    
    serialized_model = datascience.serialize_model(model)
    storage.create_bucket(parameter_runid)
    storage_file_name = parameter_runid + '_' + parameter_postalcode + '_' + parameter_horizon + '.p'
    storage_file_url = storage.upload_file(serialized_model, storage_file_name, parameter_runid)
    model_datastore.update(storage_file_url, parameter_runid, parameter_postalcode, parameter_horizon)
    
    return "success"

if __name__ == "__main__":
    #app.run(host='0.0.0.0', debug=True)
    app.run()