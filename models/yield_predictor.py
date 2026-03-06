"""
Crop Yield Prediction using Regression
Uses rainfall, temperature, soil N/P/K to predict yield.
"""
import numpy as np
import pickle
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor


CROP_OPTIONS = ["Rice", "Wheat", "Maize", "Cotton", "Sugarcane", "Soybean"]


def get_yield_model():
    """Load or create yield prediction model"""
    model_path = Path(__file__).parent / "yield_model.pkl"

    if model_path.exists():
        with open(model_path, "rb") as f:
            return pickle.load(f)

    model = _create_default_yield_model()
    Path(__file__).parent.mkdir(parents=True, exist_ok=True)
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    return model


def _create_default_yield_model() -> RandomForestRegressor:
    """Create regression model with synthetic crop data"""
    np.random.seed(42)
    n_samples = 600

    rainfall = np.random.uniform(500, 2000, n_samples)
    temperature = np.random.uniform(18, 35, n_samples)
    n_val = np.random.uniform(20, 100, n_samples)
    p_val = np.random.uniform(10, 80, n_samples)
    k_val = np.random.uniform(15, 90, n_samples)
    ph = np.random.uniform(5.5, 7.5, n_samples)

    # Synthetic yield (kg/ha) - simplified relationship
    yield_val = (
        1000 + rainfall * 0.5 + temperature * 20 +
        n_val * 2 + p_val * 1.5 + k_val * 1.2 - abs(ph - 6.5) * 100
        + np.random.normal(0, 200, n_samples)
    )
    yield_val = np.clip(yield_val, 500, 8000)

    X = np.column_stack([rainfall, temperature, n_val, p_val, k_val, ph])
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X, yield_val)
    return model


def predict_yield(
    rainfall: float,
    temperature: float,
    n_value: float,
    p_value: float,
    k_value: float,
    ph: float = 6.5
) -> float:
    """Predict crop yield in kg/ha"""
    model = get_yield_model()
    features = np.array([[rainfall, temperature, n_value, p_value, k_value, ph]])
    return float(model.predict(features)[0])
