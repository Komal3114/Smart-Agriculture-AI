"""
Crop Yield Prediction
Predict yield based on rainfall, temperature, and soil data.
"""
import streamlit as st
import pandas as pd
from pathlib import Path

from models.yield_predictor import predict_yield, CROP_OPTIONS
from utils.database import save_yield_prediction, init_database

init_database()

st.set_page_config(page_title="Yield Prediction", page_icon="📊", layout="wide")
st.title("📊 Crop Yield Prediction")
st.markdown("Predict crop yield using rainfall, temperature, and soil parameters.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Input Parameters")
    rainfall = st.number_input("Annual Rainfall (mm)", 100.0, 3000.0, 1000.0, 50.0)
    temperature = st.number_input("Average Temperature (°C)", 15.0, 40.0, 28.0, 1.0)
    n_value = st.number_input("Soil Nitrogen (ppm)", 10.0, 150.0, 50.0, 5.0)
    p_value = st.number_input("Soil Phosphorus (ppm)", 5.0, 100.0, 35.0, 5.0)
    k_value = st.number_input("Soil Potassium (ppm)", 10.0, 120.0, 45.0, 5.0)
    ph = st.slider("Soil pH", 5.0, 8.0, 6.5, 0.1)

with col2:
    if st.button("📈 Predict Yield", type="primary"):
        yield_pred = predict_yield(
            rainfall=rainfall,
            temperature=temperature,
            n_value=n_value,
            p_value=p_value,
            k_value=k_value,
            ph=ph,
        )
        st.success(f"**Predicted Yield:** {yield_pred:,.0f} kg/ha")
        save_yield_prediction("General", yield_pred, rainfall, temperature)

st.markdown("---")
st.subheader("Sample Dataset")
csv_path = Path(__file__).parent.parent / "datasets" / "crop_yield_sample.csv"
if csv_path.exists():
    df = pd.read_csv(csv_path)
    st.dataframe(df.head(10), use_container_width=True)
