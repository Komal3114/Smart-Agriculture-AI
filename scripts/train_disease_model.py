"""
Optional script to train a minimal CNN for plant disease detection.
Run this to create plant_disease_model.keras for improved predictions.
Uses synthetic/random data for demo - replace with PlantVillage dataset for production.
"""
import numpy as np
from pathlib import Path

try:
    import tensorflow as tf
except ImportError:
    print("TensorFlow not installed. Run: pip install tensorflow")
    exit(1)

from utils.config import DISEASE_CLASSES

NUM_CLASSES = min(10, len(DISEASE_CLASSES))  # Use subset for faster training
IMG_SIZE = 224


def create_model():
    """Create a simple CNN for disease classification"""
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, 3, activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(64, 3, activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(64, 3, activation='relu'),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(NUM_CLASSES, activation='softmax')
    ])
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    return model


def main():
    print("Creating synthetic training data...")
    np.random.seed(42)
    n_samples = 200
    X = np.random.rand(n_samples, IMG_SIZE, IMG_SIZE, 3).astype(np.float32)
    y = np.random.randint(0, NUM_CLASSES, n_samples)

    model = create_model()
    model.fit(X, y, epochs=3, batch_size=32, verbose=1)

    model_path = Path(__file__).parent.parent / "models" / "plant_disease_model.keras"
    model_path.parent.mkdir(parents=True, exist_ok=True)
    model.save(str(model_path))
    print(f"Model saved to {model_path}")


if __name__ == "__main__":
    main()
