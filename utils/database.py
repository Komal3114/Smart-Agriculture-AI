"""
SQLite database utilities for Smart Agriculture AI
"""
import sqlite3
from pathlib import Path
from utils.config import DATABASE_PATH


def get_connection():
    """Create and return database connection"""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    return conn


def init_database():
    """Initialize database tables"""
    conn = get_connection()
    cursor = conn.cursor()

    # Predictions history table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS disease_predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_path TEXT,
            predicted_disease TEXT,
            confidence REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Fertilizer recommendations
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fertilizer_recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            soil_type TEXT,
            crop_type TEXT,
            location TEXT,
            recommendation TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Yield predictions
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS yield_predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            crop TEXT,
            predicted_yield REAL,
            rainfall REAL,
            temperature REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_disease_prediction(image_path, disease, confidence):
    """Save disease prediction to database"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO disease_predictions (image_path, predicted_disease, confidence) VALUES (?, ?, ?)",
        (image_path, disease, confidence)
    )
    conn.commit()
    conn.close()


def save_fertilizer_recommendation(soil_type, crop_type, location, recommendation):
    """Save fertilizer recommendation to database"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO fertilizer_recommendations 
           (soil_type, crop_type, location, recommendation) VALUES (?, ?, ?, ?)""",
        (soil_type, crop_type, location, recommendation)
    )
    conn.commit()
    conn.close()


def save_yield_prediction(crop, yield_value, rainfall, temperature):
    """Save yield prediction to database"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO yield_predictions (crop, predicted_yield, rainfall, temperature) 
           VALUES (?, ?, ?, ?)""",
        (crop, yield_value, rainfall, temperature)
    )
    conn.commit()
    conn.close()


def get_recent_predictions(limit=10):
    """Get recent predictions for analytics"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT * FROM disease_predictions 
           ORDER BY created_at DESC LIMIT ?""",
        (limit,)
    )
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]
