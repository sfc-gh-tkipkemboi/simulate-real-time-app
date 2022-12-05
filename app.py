import streamlit as st
import pandas as pd

@st.cache
def load_data():
  return df

df = load_data()

for i, row in df.iterrows():
  st.write(row)
  
  with st.spinner("Simulating real-time data..."):
    st.cache(st.sleep(1))
