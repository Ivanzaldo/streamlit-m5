import streamlit as st
# Crear el titulo para la aplicacion web
st.title("Mi Primera App con Streamlit")
sidebar = st.sidebar
sidebar.title("Esta es la barra lateral.")
sidebar.write("Aqui van los elementos de entrada.")


st.header("Informacion sobre el Conjunto de Datos")

st.header("Descripcion de los datos ")

st.write(""" 
Este es un simple ejemplo de una app para predecir

Esta app predice mis datos!
""")

