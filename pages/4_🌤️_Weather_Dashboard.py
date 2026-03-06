"""
Weather Dashboard
Display live weather data using OpenWeather API.
"""
import streamlit as st
from utils.weather_api import get_weather_by_city

st.set_page_config(page_title="Weather Dashboard", page_icon="🌤️", layout="wide")
st.title("🌤️ Weather Dashboard")
st.markdown("Fetch live weather data for your farm location.")

city = st.text_input("Enter city name", "Mumbai")
if st.button("Get Weather"):
    with st.spinner("Fetching weather..."):
        weather = get_weather_by_city(city)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Temperature", f"{weather['temperature']}°C", f"Feels like {weather['feels_like']}°C")
    col2.metric("Humidity", f"{weather['humidity']}%", "")
    col3.metric("Wind Speed", f"{weather['wind_speed']} m/s", "")
    col4.metric("Rainfall", f"{weather.get('rainfall_mm', 0)} mm", "")

    st.info(f"**Conditions:** {weather['description']} | **Pressure:** {weather['pressure']} hPa")
    if "note" in weather:
        st.caption(weather["note"])
