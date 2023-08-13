import streamlit as st
import pandas as pd
from urllib.error import URLError
import matplotlib.pyplot as plt

# Importar los datasets que vamos a utilizar
folder = 'data'
archivo_data = 'data.csv'
data = pd.read_csv(folder + '/' + archivo_data, sep=',')

# Definir las clases que vamos a utilizar y reemplazar su valor numérico
nombre_class = {0: "NM", 1: "EC"}
d = data.copy()
d['HeartDisease'] = d['HeartDisease'].replace(nombre_class)
caracteristicas = d.drop(['HeartDisease'], axis=1)
etiqueta = d['HeartDisease']

st.set_page_config(page_title="DataFrame Demo")

st.markdown("# DataFrame Demo")
st.sidebar.header("DataFrame Demo")
st.write(
    """
    Vamos a visualizar los datos que tiene la base de datos
    """
)
# Mostrar el DataFrame en streamlit
st.dataframe(d.head())

# Como realizar el conteo de las clases que hay en la base de datos
conteo = d["HeartDisease"].value_counts()
st.dataframe(conteo)

indices = conteo.index.tolist()  # Estas son las clases

# Graficar el conteo de las clases en un gráfico torta
fig, ax = plt.subplots()
ax.pie(list(conteo.values), labels=indices, autopct='%1.1f%%')
ax.axis('equal')  # Para asegurar que el gráfico sea circular

# Mostrar el gráfico en Streamlit
st.pyplot(fig)

# Graficar la distribución de edades
st.write("## Distribución de Edades")
plt.figure(figsize=(10, 6))
st.bar_chart(d['age'].value_counts())

