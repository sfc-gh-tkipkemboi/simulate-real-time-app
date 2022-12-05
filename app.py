import streamlit as st
import pandas as pd
from time import sleep

@st.cache
def load_data():
  data = {
  "calories": [420, 380, 390, 78, 90, 6565, 9845],
  "duration": [50, 40, 45, 50, 55, 56, 70]
  }
  df = pd.DataFrame(data)
  return df

df = load_data()

for i, row in df.iterrows():
  st.write(row)
  
  with st.spinner("Simulating real-time data..."):
    sleep(1)
