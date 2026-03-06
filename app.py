"""
Smart Agriculture AI - Main Application
AI-powered platform for crop disease detection, fertilizer recommendation,
yield prediction, weather, and farm analytics.
"""
import streamlit as st
from pathlib import Path
import sys

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

# Initialize database on startup
from utils.database import init_database
init_database()

# Page config
st.set_page_config(
    page_title="Smart Agriculture AI",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #2d5a27;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        color: #5a7d5a;
        text-align: center;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">🌾 Smart Agriculture AI</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="sub-header">AI-powered crop disease detection, fertilizer recommendations, '
    'yield prediction, weather, and farm analytics</p>',
    unsafe_allow_html=True
)

# Sidebar navigation info
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/agriculture.png", width=80)
    st.title("Navigation")
    st.markdown("Use the **pages** in the sidebar to access:")
    st.markdown("""
    - 🌿 **Disease Detection** - Upload leaf images
    - 🧪 **Fertilizer** - Get recommendations
    - 📊 **Yield Prediction** - Predict crop yield
    - 🌤️ **Weather** - Live weather dashboard
    - 🤖 **Chatbot** - AI farming assistant
    - 📈 **Analytics** - Charts and insights
    """)
    st.markdown("---")
    st.caption("Smart Agriculture AI v1.0")

# Welcome content on home
st.info(
    "👈 **Get started** by selecting a page from the sidebar. "
    "Upload a plant leaf for disease detection, get fertilizer advice, "
    "or chat with our AI farming assistant!"
)
