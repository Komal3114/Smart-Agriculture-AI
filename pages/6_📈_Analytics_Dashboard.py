"""
Farm Analytics Dashboard
Charts and insights from predictions.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

from utils.database import get_recent_predictions, get_connection, init_database

init_database()

st.set_page_config(page_title="Analytics", page_icon="📈", layout="wide")
st.title("📈 Farm Analytics Dashboard")
st.markdown("Visualize predictions and farm insights.")

# Load sample yield data for demo chart
csv_path = Path(__file__).parent.parent / "datasets" / "crop_yield_sample.csv"
if csv_path.exists():
    df = pd.read_csv(csv_path)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Yield by Crop")
        crop_yield = df.groupby("crop")["yield_kg_per_ha"].mean().reset_index()
        fig = px.bar(crop_yield, x="crop", y="yield_kg_per_ha", color="yield_kg_per_ha")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Yield vs Rainfall")
        fig2 = px.scatter(df, x="rainfall", y="yield_kg_per_ha", color="crop", size="temperature")
        st.plotly_chart(fig2, use_container_width=True)

# Disease predictions from DB
try:
    predictions = get_recent_predictions(20)
    if predictions:
        st.subheader("Recent Disease Predictions")
        pred_df = pd.DataFrame(predictions)
        fig3 = px.pie(
            pred_df, values="confidence", names="predicted_disease",
            title="Disease Distribution"
        )
        st.plotly_chart(fig3, use_container_width=True)
        st.dataframe(pred_df, use_container_width=True)
except Exception as e:
    st.info("No prediction history yet. Use Disease Detection to build analytics.")
