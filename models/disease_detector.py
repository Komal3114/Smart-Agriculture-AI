"""
Crop Disease Detection using CNN
Uses TensorFlow/Keras for inference. Model trained on PlantVillage-style dataset.
"""
import numpy as np
from PIL import Image
import os
from pathlib import Path

# Use TensorFlow for CNN
try:
    import tensorflow as tf
    TF_AVAILABLE = True
except ImportError:
    TF_AVAILABLE = False

from utils.config import DISEASE_CLASSES, DISEASE_TREATMENTS


def load_disease_model():
    """Load the disease detection CNN model if available, else return None"""
    models_dir = Path(__file__).parent.parent / "models"
    model_path = models_dir / "plant_disease_model.keras"

    if TF_AVAILABLE and model_path.exists():
        return tf.keras.models.load_model(str(model_path))
    return None


def preprocess_image(image: Image.Image, target_size=(224, 224)) -> np.ndarray:
    """Preprocess image for CNN input"""
    image = image.convert("RGB")
    image = image.resize(target_size)
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def get_disease_treatment(disease_name: str) -> str:
    """Get treatment suggestion based on disease name"""
    disease_lower = disease_name.lower()
    for key, treatment in DISEASE_TREATMENTS.items():
        if key in disease_lower:
            return treatment
    return "Consult a local agricultural extension for specific treatment recommendations. Practice good crop hygiene."


def predict_disease(image: Image.Image) -> tuple:
    """
    Predict disease from plant leaf image
    Returns: (disease_name, confidence, treatment)
    """
    model = load_disease_model()

    if model is None:
        # Rule-based fallback when no trained model exists
        return _rule_based_prediction(image)

    img_array = preprocess_image(image)
    predictions = model.predict(img_array, verbose=0)[0]
    class_idx = np.argmax(predictions)
    confidence = float(predictions[class_idx])

    disease_name = DISEASE_CLASSES[class_idx] if class_idx < len(DISEASE_CLASSES) else "Unknown"
    treatment = get_disease_treatment(disease_name)

    return disease_name, confidence, treatment


def _rule_based_prediction(image: Image.Image) -> tuple:
    """
    Simple rule-based prediction when no ML model is available.
    Analyzes basic image features as heuristic.
    """
    img_array = np.array(image.convert("RGB"))
    # Simple heuristic: avg brightness, color distribution
    avg_brightness = np.mean(img_array)
    green_ratio = np.mean(img_array[:, :, 1]) / (np.mean(img_array) + 1e-6)

    if green_ratio > 0.9 and avg_brightness > 100:
        return "Tomato_healthy", 0.75, DISEASE_TREATMENTS["healthy"]
    if avg_brightness < 80:
        return "Tomato_Early_blight", 0.65, DISEASE_TREATMENTS["blight"]
    return "Potato_healthy", 0.70, DISEASE_TREATMENTS["healthy"]
