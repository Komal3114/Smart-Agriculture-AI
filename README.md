# 🌾 Smart Agriculture AI Platform

An AI-powered Smart Agriculture Platform built with Python, Streamlit, and ML models for crop disease detection, fertilizer recommendations, yield prediction, weather monitoring, and farm analytics.

## Tech Stack

- **Python 3.8+**
- **Streamlit** - Frontend
- **TensorFlow** - CNN for disease detection
- **Scikit-learn** - Fertilizer & yield models
- **OpenWeather API** - Live weather data
- **SQLite** - Local database
- **Plotly** - Analytics charts

## Features

1. **🌿 Crop Disease Detection** - Upload plant leaf image, CNN predicts disease and suggests treatments
2. **🧪 Fertilizer Recommendation** - Input soil type, crop, and nutrients for ML-based recommendations
3. **📊 Crop Yield Prediction** - Regression model predicts yield from rainfall, temperature, soil data
4. **🌤️ Weather Dashboard** - Live temperature, humidity, rainfall via OpenWeather API
5. **🤖 AI Farmer Chatbot** - NLP chatbot for agriculture Q&A
6. **📈 Farm Analytics Dashboard** - Charts and insights from predictions

## Project Structure

```
smart-agriculture-ai/
├── app.py                 # Main Streamlit app
├── requirements.txt       # Dependencies
├── README.md
├── models/                # ML models
│   ├── disease_detector.py
│   ├── fertilizer_recommender.py
│   ├── yield_predictor.py
│   └── chatbot.py
├── datasets/              # Sample data
│   ├── crop_yield_sample.csv
│   └── fertilizer_sample.csv
├── utils/                 # Utilities
│   ├── config.py
│   ├── database.py
│   └── weather_api.py
├── pages/                 # Streamlit pages
│   ├── 1_🌿_Disease_Detection.py
│   ├── 2_🧪_Fertilizer_Recommendation.py
│   ├── 3_📊_Yield_Prediction.py
│   ├── 4_🌤️_Weather_Dashboard.py
│   ├── 5_🤖_AI_Chatbot.py
│   └── 6_📈_Analytics_Dashboard.py
├── scripts/               # Training scripts
│   └── train_disease_model.py
├── static/
└── templates/
```

## Setup & Run

### 1. Create virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# or: source venv/bin/activate  # Linux/Mac
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. (Optional) Train disease detection model

```bash
python scripts/train_disease_model.py
```

### 4. Set OpenWeather API key (optional, for live weather)

Create `.env` file or set environment variable:

```bash
set OPENWEATHER_API_KEY=your_api_key   # Windows
export OPENWEATHER_API_KEY=your_api_key  # Linux/Mac
```

Get free API key: https://openweathermap.org/api

### 5. Run the app

```bash
streamlit run app.py
```

Open http://localhost:8501 in your browser.

## Usage

- **Disease Detection**: Upload a plant leaf image (JPG/PNG) to get disease prediction and treatment.
- **Fertilizer**: Select soil type, crop, and adjust N-P-K sliders for recommendations.
- **Yield Prediction**: Enter rainfall, temperature, and soil values to predict yield.
- **Weather**: Enter city name for live weather data.
- **Chatbot**: Ask questions about fertilizers, pests, irrigation, etc.
- **Analytics**: View charts from sample data and prediction history.

## Notes

- Disease detection uses rule-based fallback when no CNN model is trained.
- For production, train CNN on [PlantVillage](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset) dataset.
- SQLite database (`farm_data.db`) is created automatically on first run.
