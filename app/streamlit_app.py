import streamlit as st

st.set_page_config(
    page_title="NeuralRetail",
    layout="wide"
)

st.title("🛒 NeuralRetail AI Platform")

st.markdown("""
Welcome to NeuralRetail.

Use the sidebar to navigate through modules.
""")

st.sidebar.title("Navigation")
st.sidebar.success("Select a module")
