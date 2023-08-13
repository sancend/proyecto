import pickle
import streamlit as st
import pandas as pd
import requests

def solicitud_API(muestra: list):
    #URL de la API
    url = 'http://127.0.0.1:8000/predict'
    
    # Datos de entrada
    data = {
        "data": [muestra]
    }
    
    #Realizar la solicitud POST a la API
    response = requests.post(url, json=data)
    
    # Verificar el código de estado de la respuesta
    if response.status_code == 200:
        # Obtener la respuesta en formato JSON
        result = response.json()
        
        # Obtener la predicción
        prediction = result["prediction"]
        
        # Imprimir la predicción
        print("Predicción:", prediction)
        return prediction
    else:
        print("Error en la solicitud", response.status_code)
        return None
    
     
     
with open('models/modelo_enfermedad_corazon.pkl', 'rb') as gb:
    modelo = pickle.load(gb)


st.subheader("Machine learning modelo seleccionado")

st.subheader("Algoritmo de Machine Learning")
st.write("Definición del algoritmo implementado para predecir si una persona sufre enfermedad del corazón")

st.subheader("caracteristicas de entrada")
features = ['age', 'sex', 'cp', 'trestbps', 'chol','fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
st.write("A continuación, ingrese los valores de las características")

def user_input_parameters():
    inputs = {}
    for i, feature in enumerate(features):
        row, col = i // 3, i % 3
        with st.container():
            if i % 3 == 0:
                cols = st.columns(3)
            inputs[feature] = cols[col].text_input(feature)
    data_features = {
        'age' : inputs[features[0]],
        'sex' : inputs[features[1]],
        'cp' : inputs[features[2]],
        'trestbps' : inputs[features[3]],
        'chol' : inputs[features[4]],
        'fbs' : inputs[features[5]],
        'restecg' : inputs[features[6]],
        'thalach' : inputs[features[7]],
        'exang' : inputs[features[8]],
        'oldpeak' : inputs[features[9]],
        'slope' : inputs[features[10]],
        'ca' : inputs[features[11]],
        'thal' : inputs[features[12]]
         }
    features_df = pd.DataFrame(data_features, index = [0])
    return features_df

df = user_input_parameters()


st.subheader("Modelo enfermedad del corazon")

# Crear un nuevo DataFrame con una fila adicional 'Valor'
df = df.T.reset_index()
df.columns = ['Característica', 'Valor']
df = df.set_index('Característica').T

st.table(df)
    

# Crear dos botones 'PREDECIR' y 'LIMPIAR' en la misma fila
predict_button, clear_button = st.columns(2)
predict_clicked = predict_button.button('PREDECIR')
prediction = ''
if predict_clicked:
    inputs_validos = True
    
# Validar que todos los campos contengan valores numéricos
    for value in df.values.flatten():
        if not value or not value.isdigit():
            st.warning("Por favor, complete todos los datos con valores numéricos antes de hacer la predicción")
            break
        else:
            #prediction = modelo.predict(df)[0]
            prediction = solicitud_API(df.values.flatten().tolist())
    
    # Crear un diccionario para asociar las predicciones con 
    prediction_descriptions = {
        '0': 'Normal',
        '1': 'Enfermedad cardíaca'
    }
            
    # Mostrar la descripción completa de la predicción
    if prediction == 1:
        st.warning("Alerta: Presta atención posible fallo cardiaco")
    else:
        st.success("No se detectó enfermedad cardíaca")