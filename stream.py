# streamlit_app.py
import streamlit as st
import pandas as pd
import requests

# API endpoint URL hosted by FastAPI
API_URL = "http://localhost:8000/employees"

# Make a request to the FastAPI endpoint
response = requests.get(API_URL)


# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    col1, col2 = st.columns(2)
    with col1: st.header('Employees Details') 
    st.write(df)
    with col2: st.header('Data in Column 2') 
    st.bar_chart(df['name'])
    











