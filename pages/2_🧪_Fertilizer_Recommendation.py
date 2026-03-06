"""
Fertilizer Recommendation System
Input soil type, crop type, and N/P/K values for personalized recommendations.
"""
import streamlit as st
from models.fertilizer_recommender import recommend_fertilizer, SOIL_TYPES, CROP_TYPES
from utils.weather_api import get_weather_by_city
from utils.database import save_fertilizer_recommendation, init_database

init_database()

st.set_page_config(page_title="Fertilizer Recommendation", page_icon="🧪", layout="wide")
st.title("🧪 Fertilizer Recommendation System")
st.markdown("Get AI-powered fertilizer recommendations based on your soil and crop conditions.")

col1, col2 = st.columns(2)

with col1:
    soil_type = st.selectbox("Soil Type", list(SOIL_TYPES.keys()))
    crop_type = st.selectbox("Crop Type", list(CROP_TYPES.keys()))
    location = st.text_input("Location (for weather)", "Mumbai", help="Used for temperature/humidity")

    st.subheader("Soil Nutrient Levels (ppm)")
    n_value = st.slider("Nitrogen (N)", 0, 100, 50)
    p_value = st.slider("Phosphorus (P)", 0, 100, 35)
    k_value = st.slider("Potassium (K)", 0, 100, 45)

with col2:
    if st.button("🌱 Get Recommendation", type="primary"):
        # Fetch weather for temp/humidity
        weather = get_weather_by_city(location)
        temp = weather.get("temperature", 25)
        humidity = weather.get("humidity", 60)

        fertilizer, confidence = recommend_fertilizer(
            soil_type=soil_type,
            crop_type=crop_type,
            n_value=float(n_value),
            p_value=float(p_value),
            k_value=float(k_value),
            temperature=temp,
            humidity=humidity,
        )

        st.success(f"**Recommended Fertilizer:** {fertilizer}")
        st.metric("Model Confidence", f"{confidence * 100:.1f}%")
        save_fertilizer_recommendation(soil_type, crop_type, location, fertilizer)

        st.markdown("**Tip:** Conduct soil testing for accurate N-P-K values.")
