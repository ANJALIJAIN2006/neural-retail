import streamlit as st
import pandas as pd

st.title("📦 Inventory Optimization")

inventory_df = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet", "Headphones"],
    "Stock": [5, 20, 8, 3],
    "Status": ["Low", "Good", "Low", "Critical"]
})

st.dataframe(inventory_df)

st.error("Inventory alert generated")