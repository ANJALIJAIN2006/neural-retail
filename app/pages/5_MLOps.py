import streamlit as st

st.title("🤖 MLOps Monitoring")

col1, col2 = st.columns(2)

col1.metric("Model Accuracy", "91%")
col2.metric("Drift Score", "0.08")

st.success("All systems operational")