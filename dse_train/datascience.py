import pandas
from sklearn import model_selection
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle
from sklearn import datasets
#import numpy as np

def trainmodel(dataframe):
   # array = np.asarray(dataframe)
    array = dataframe.values
    X = array[:,0:8]
    Y = array[:,8]
    test_size = 0.33
    seed = 7
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
    # Fit the model on 33%
    model = GradientBoostingRegressor()
    model2 = GradientBoostingClassifier()
    model3 = LogisticRegression()
    model.fit(X_train, Y_train)
    model2.fit(X_train, Y_train)
    model3.fit(X_train, Y_train)
    model.fit(X_train, Y_train)
    model.fit(X_train, Y_train)
    model.fit(X_train, Y_train)
    model.fit(X_train, Y_train)
    model.fit(X_train, Y_train)
    model.fit(X_train, Y_train)
    model.fit(X_train, Y_train)
    model.fit(X_train, Y_train)
    model.fit(X_train, Y_train)

    return model

def get_prediction(model, data):
    prediction = model.predict(data)
    return prediction

def serialize_model(model):
    serialized_model = pickle.dumps(model)
    return serialized_model

def deserialize_model(serialized_model):
    deserialized_model = pickle.loads(serialized_model)
    return deserialized_model