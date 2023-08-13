from fastapi import FastAPI
import pandas as pd
import pickle
import numpy as np


# Cargamos el modelo previamente entrenado
with open('models/modelo_enfermedad_corazon.pkl', 'rb') as gb:
    modelo = pickle.load(gb)
    
    
app = FastAPI()
    
@app.get('/')
def hello():
    return {'message': 'Hello World'}
    
@app.post('/predict')
def predict(request:dict):
    #Get the dat from the POST request
    data = request['data']
    input_data = np.array(data)
    input_data = input_data.reshape(1, -1)
    #Make prediction using model loaded from disk as per the data
    prediction = modelo.predict(input_data)
    #Take the first value of prediction
    output = int(prediction[0])
    
    return {'prediction':output}