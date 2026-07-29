import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("NeuralRetail Dashboard")

if st.button("Predict Churn"):
    response = requests.get(f"{API_URL}/predict/churn")
    st.json(response.json())

if st.button("Predict Demand"):
    response = requests.get(f"{API_URL}/predict/demand")
    st.json(response.json())