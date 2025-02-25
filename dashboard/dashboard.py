import streamlit as st
import pandas as pd
import requests

st.title("Data Quality Monitoring Dashboard")
response = requests.get("http://localhost:8000/data-quality")
data = pd.DataFrame(response.json())
st.write(data)

st.line_chart(data['accuracy'])
st.bar_chart(data['anomalies'])
