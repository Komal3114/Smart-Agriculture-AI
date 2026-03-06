"""
OpenWeather API integration for weather data
"""
import requests
from utils.config import OPENWEATHER_API_KEY, OPENWEATHER_BASE_URL


def get_weather_by_city(city_name: str) -> dict:
    """
    Fetch current weather data for a city
    Returns: dict with temperature, humidity, rainfall, wind, description
    """
    if OPENWEATHER_API_KEY == "your_api_key_here":
        return _get_mock_weather(city_name)

    try:
        url = f"{OPENWEATHER_BASE_URL}/weather"
        params = {
            "q": city_name,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric"
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Fetch 5-day forecast for rainfall
        forecast_url = f"{OPENWEATHER_BASE_URL}/forecast"
        forecast_params = {"q": city_name, "appid": OPENWEATHER_API_KEY, "units": "metric"}
        forecast_resp = requests.get(forecast_url, params=forecast_params, timeout=10)
        rainfall = 0
        if forecast_resp.status_code == 200:
            forecast_data = forecast_resp.json()
            for item in forecast_data.get("list", [])[:8]:  # Next 24 hours
                rainfall += item.get("pop", 0) * item.get("rain", {}).get("3h", 0)

        return {
            "city": data.get("name", city_name),
            "temperature": round(data["main"]["temp"], 1),
            "feels_like": round(data["main"]["feels_like"], 1),
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"].title(),
            "rainfall_mm": round(rainfall, 2),
        }
    except Exception as e:
        return _get_mock_weather(city_name, str(e))


def _get_mock_weather(city_name: str, error_msg: str = None) -> dict:
    """Return mock weather data when API key is not set or API fails"""
    return {
        "city": city_name,
        "temperature": 25.5,
        "feels_like": 26.0,
        "humidity": 65,
        "pressure": 1013,
        "wind_speed": 3.2,
        "description": "Partly Cloudy",
        "rainfall_mm": 0,
        "note": f"(Demo data - Set OPENWEATHER_API_KEY for live data. {error_msg or ''})"
    }
