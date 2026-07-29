import streamlit as st
import random

st.title("NeuralRetail Dashboard")

if st.button("Predict Churn"):
    st.json({
        "customer_id": 101,
        "churn_score": round(random.uniform(0, 1), 2)
    })

if st.button("Predict Demand"):
    st.json({
        "sku": "SKU-001",
        "predicted_demand": random.randint(100, 500)
    })