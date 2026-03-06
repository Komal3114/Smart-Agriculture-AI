"""
Crop Disease Detection Page
Upload plant leaf image, get disease prediction and treatment suggestions.
"""
import streamlit as st
from PIL import Image
import tempfile
import os

from models.disease_detector import predict_disease, DISEASE_CLASSES
from utils.database import save_disease_prediction, init_database

# Initialize database
init_database()

st.set_page_config(page_title="Disease Detection", page_icon="🌿", layout="wide")
st.title("🌿 Crop Disease Detection")
st.markdown("Upload a plant leaf image to detect diseases using our CNN model.")

col1, col2 = st.columns([1, 1])

with col1:
    uploaded_file = st.file_uploader(
        "Choose a leaf image",
        type=["jpg", "jpeg", "png"],
        help="Upload an image of a plant leaf (tomato, potato, corn, etc.)"
    )

    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Leaf Image", use_container_width=True)

with col2:
    if uploaded_file and st.button("🔍 Detect Disease", type="primary"):
        with st.spinner("Analyzing image..."):
            disease_name, confidence, treatment = predict_disease(image)

        st.success("Analysis Complete!")
        st.metric("Predicted Disease", disease_name.replace("_", " ").title())
        st.metric("Confidence", f"{confidence * 100:.1f}%")

        st.subheader("💊 Treatment Suggestions")
        st.info(treatment)

        # Save to database
        save_disease_prediction(uploaded_file.name, disease_name, confidence)

st.markdown("---")
st.markdown("**Supported crops:** Tomato, Potato, Corn, Grape, Apple, and more (PlantVillage dataset)")
