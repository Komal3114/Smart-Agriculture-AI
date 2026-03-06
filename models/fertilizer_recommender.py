"""
Fertilizer Recommendation System using ML
Uses soil type, crop type, and location (N, P, K values) to recommend fertilizer.
"""
import numpy as np
import pickle
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier


# Default fertilizer classes
FERTILIZER_LABELS = [
    "Urea", "DAP", "MOP", "NPK", "SSP",
    "Ammonium Sulphate", "Calcium Nitrate", "Magnesium Sulphate"
]

# Mapping for soil and crop to numeric
SOIL_TYPES = {"Sandy": 0, "Loamy": 1, "Black": 2, "Red": 3, "Clayey": 4}
CROP_TYPES = {
    "Rice": 0, "Wheat": 1, "Cotton": 2, "Sugarcane": 3, "Maize": 4,
    "Soybean": 5, "Barley": 6, "Millets": 7, "Groundnut": 8, "Pulses": 9
}


def get_fertilizer_model():
    """Load or create fertilizer recommendation model"""
    model_path = Path(__file__).parent / "fertilizer_model.pkl"

    if model_path.exists():
        with open(model_path, "rb") as f:
            return pickle.load(f)

    # Create and train a simple model with synthetic data
    model = _create_default_model()
    model_path.parent.mkdir(parents=True, exist_ok=True)
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    return model


def _create_default_model() -> RandomForestClassifier:
    """Create a model trained on synthetic fertilizer data"""
    np.random.seed(42)
    n_samples = 500

    # Synthetic data: N, P, K, Temperature, Humidity, soil_type, crop_type, moisture
    X = np.random.rand(n_samples, 8) * 100
    X[:, 5] = np.random.randint(0, 5, n_samples)  # soil
    X[:, 6] = np.random.randint(0, 10, n_samples)  # crop
    y = np.random.randint(0, len(FERTILIZER_LABELS), n_samples)

    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X, y)
    return model


def recommend_fertilizer(
    soil_type: str,
    crop_type: str,
    n_value: float,
    p_value: float,
    k_value: float,
    temperature: float = 25,
    humidity: float = 60,
    moisture: float = 50
) -> tuple:
    """
    Get fertilizer recommendation
    Returns: (fertilizer_name, confidence)
    """
    soil_num = SOIL_TYPES.get(soil_type, 1)
    crop_num = CROP_TYPES.get(crop_type, 0)

    features = np.array([[
        n_value, p_value, k_value, temperature, humidity,
        soil_num, crop_num, moisture
    ]])

    model = get_fertilizer_model()
    pred = model.predict(features)[0]
    proba = model.predict_proba(features)[0]
    confidence = float(proba[pred])

    fertilizer = FERTILIZER_LABELS[pred] if pred < len(FERTILIZER_LABELS) else "NPK"
    return fertilizer, confidence
