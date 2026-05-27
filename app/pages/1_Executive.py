import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("📊 Executive Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Revenue", "$125,000")
col2.metric("Forecast Accuracy", "91%")
col3.metric("Churn Risk", "12%")
col4.metric("Customers", "4,521")

sales = np.random.randint(100, 500, 30)

chart_df = pd.DataFrame({
    "Day": range(1, 31),
    "Sales": sales
})

fig = px.line(
    chart_df,
    x="Day",
    y="Sales",
    title="Monthly Revenue Trend",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

st.success("Executive dashboard loaded successfully")