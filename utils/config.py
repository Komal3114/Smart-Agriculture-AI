"""
Configuration settings for Smart Agriculture AI Platform
"""
import os
from pathlib import Path

# Load .env if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = BASE_DIR / "datasets"
MODELS_DIR = BASE_DIR / "models"
STATIC_DIR = BASE_DIR / "static"

# Database
DATABASE_PATH = BASE_DIR / "farm_data.db"

# OpenWeather API - Set your API key in environment variable OPENWEATHER_API_KEY
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "your_api_key_here")
OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5"

# Disease classes for plant leaf detection (PlantVillage dataset classes)
DISEASE_CLASSES = [
    "Apple_Apple_scab",
    "Apple_Black_rot",
    "Apple_Cedar_apple_rust",
    "Apple_healthy",
    "Blueberry_healthy",
    "Cherry_Powdery_mildew",
    "Cherry_healthy",
    "Corn_Cercospora_leaf_spot",
    "Corn_Common_rust",
    "Corn_Northern_Leaf_Blight",
    "Corn_healthy",
    "Grape_Black_rot",
    "Grape_Esca",
    "Grape_Leaf_blight",
    "Grape_healthy",
    "Peach_Bacterial_spot",
    "Peach_healthy",
    "Pepper_bacterial_spot",
    "Pepper_healthy",
    "Potato_Early_blight",
    "Potato_Late_blight",
    "Potato_healthy",
    "Raspberry_healthy",
    "Soybean_healthy",
    "Squash_Powdery_mildew",
    "Strawberry_Leaf_scorch",
    "Strawberry_healthy",
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_Spider_mites",
    "Tomato_Target_Spot",
    "Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato_mosaic_virus",
    "Tomato_healthy",
]

# Treatment suggestions mapping for common diseases
DISEASE_TREATMENTS = {
    "scab": "Apply fungicide (e.g., sulfur or lime-sulfur). Remove infected leaves. Ensure proper air circulation.",
    "rot": "Remove infected plant parts. Apply copper-based fungicide. Improve drainage.",
    "blight": "Apply fungicide containing chlorothalonil or copper. Remove infected leaves promptly.",
    "rust": "Apply sulfur or neem oil. Remove infected leaves. Avoid overhead watering.",
    "mildew": "Apply sulfur or potassium bicarbonate. Improve air circulation. Reduce humidity.",
    "healthy": "Plant appears healthy! Continue regular monitoring and preventive care.",
    "mosaic": "Remove infected plants. Control aphids. Use virus-free seeds.",
    "spot": "Apply copper-based fungicide. Remove infected leaves. Practice crop rotation.",
}
