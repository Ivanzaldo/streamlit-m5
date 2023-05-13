import streamlit as st
import pandas as pd
import numpy as np
# Titulos
st.title("San francisco Map")
st.header("Using Streamliot and Mapbox")
# Mapa
map_data = pd.DataFrame(np.random.randn(1000,2)/[50,50]+[37.76,-122.4], columns=['lat','lon'])
st.map(map_data)
