from sklearn.ensemble import GradientBoostingRegressor
import pickle

def get_prediction(model, data):
    prediction = model.predict(data)
    return prediction

def deserialize_model(serialized_model):
    deserialized_model = pickle.loads(serialized_model)
    return deserialized_model
