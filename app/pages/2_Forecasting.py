import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from src.neuralretail.forecast import predict_sales

st.title("📈 Demand Forecasting")

prediction = predict_sales()

st.metric("Predicted Sales", prediction)

forecast_df = pd.DataFrame({
    "Day": range(1, 31),
    "Forecast": np.random.randint(150, 600, 30)
})

fig = px.line(
    forecast_df,
    x="Day",
    y="Forecast",
    title="Demand Forecast"
)

st.plotly_chart(fig, use_container_width=True)