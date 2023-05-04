import streamlit as st
import pandas as pd

names_link = 'dataset.csv'
names_data = pd.read_csv(names_link)
st.title("Read CSV, Streamlit and pandas")

st.dataframe(names_data)

# streamlit run 2.-read_dataset.py --server.enableCORS false --server.enableXsrfProtection false