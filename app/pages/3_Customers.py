import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from src.neuralretail.churn import churn_score

st.title("Customer Churn Prediction")

st.write("Predict whether a customer may leave.")

# Example inputs
tenure = st.slider("Customer Tenure (months)", 1, 72, 12)
monthly_charges = st.number_input("Monthly Charges", 0.0, 10000.0, 500.0)

# Predict button
if st.button("Predict Churn"):
    result = churn_score(tenure, monthly_charges)

    st.success(f"Churn Score: {result}")