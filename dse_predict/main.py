from flask import Flask, jsonify, request
import model_datastore
import storage
import datascience
import json

app = Flask(__name__)

@app.route('/')
def check_online():    

    return 'DSE prediction app is online!'

@app.route('/',  methods=['GET'])
def gcheck_online_rest():    

    return 'DSE prediction app is online!'

@app.route('/predict', methods=['POST'])
def predict_modell():
    
    request_json = request.get_json()
    parameter_runid = request_json['runid']
    parameter_postalcode = request_json['postalcode']
    parameter_horizon = request_json['horizon']
    parameter_data = request_json['data']
    
    model_metadata = model_datastore.query(parameter_runid, parameter_postalcode, parameter_horizon)
    serialized_model = storage.download_model(model_metadata['model_url'])
    deserialized_model = datascience.deserialize_model(serialized_model)
    prediction = datascience.get_prediction(deserialized_model, parameter_data)
    return str(prediction[0])

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
