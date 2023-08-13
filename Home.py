import streamlit as st



st.set_page_config(
    page_title="Clasificador de enfermedad del corazón",
)

st.write("# Bienvenido a tu primer clasificador")

st.sidebar.success("Select a demo above")
st.markdown(
    """
    Descripción de una base de datos de predicción de insuficiencia cardíaca
  
Esta base de datos contiene información clínica relevante de pacientes que han sido evaluados para enfermedades cardíacas. Los datos incluyen características demográficas, síntomas, resultados de pruebas médicas y la presencia o ausencia de enfermedad cardíaca. Esta base de datos es utilizada para desarrollar modelos predictivos y analizar patrones relacionados con enfermedades cardíacas.

| Característica      | Descripción                                                                                                                                                          |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age                 | Edad del paciente en años.                                                                                                                                           |
| sex                 | Género del paciente (1 = masculino; 0 = femenino).                                                                                                                       |
| cp                  | Tipo de dolor en el pecho1: angina típica, 2: angina atípica, 3: dolor no anginoso, 4: asintomático                                                         |
| trestbps	          | Presión arterial en reposo en mm Hg.                                                                                                                                |
| chol                | Colesterol sérico en mm/dl.                                                                                                                                         |
| fbs                 | Azúcar en sangre en ayunas > 120 mg/dL (probablemente diabético) 1 = verdadero; 0 = falso.                                                                                 |
| restecg             | Resultados del electrocardiograma en reposo Valor 0: normal, Valor 1: con anomalías en la onda ST-T (inversiones de la onda T y/o elevación o depresión del ST > 0,05 mV), Valor 2: muestra probable o hipertrofia ventricular izquierda definida según los criterios de Estres.                                  |
| thalach	          | Frecuencia cardíaca máxima alcanzada (valor numérico entre 60 y 202).                                                                                              |
| exang               | Angina inducida por el ejercicio (1 = sí; 0 = no).                                                                                                                   |
| oldpeak             | Depresión del segmento ST inducida por el ejercicio en relación con el reposo.                                                                                                    |
| slope               | Pendiente del segmento ST durante el ejercicio máximo Valor 1: ascendente, Valor 2: plano, Valor 3: descendente.                                                      |
| ca                  | Número de vasos principales (0-3) coloreado por fluoroscopia. Los principales vasos cardíacos son: aorta, vena cava superior, vena cava inferior, arteria pulmonar                                                                            |
| thal                | Frecuencia cardíaca máxima alcanzada.                                                                                                    |
| HeartDisease        | Clase de salida (1: enfermedad cardíaca, 0: normal).                                                                                                               |
"""
)