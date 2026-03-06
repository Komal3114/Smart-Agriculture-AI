"""
AI Farmer Chatbot using NLP
Answers agriculture-related questions using rule-based + optional transformers.
"""
import re
from typing import Tuple


# Agricultural knowledge base - rules and responses
AGRICULTURE_KB = {
    "fertilizer": {
        "keywords": ["fertilizer", "npk", "urea", "dap", "mop", "nutrient"],
        "response": "Fertilizers provide essential nutrients (N-P-K: Nitrogen, Phosphorus, Potassium). "
                    "Use soil testing to determine requirements. Organic options include compost and manure. "
                    "Apply based on crop growth stage."
    },
    "pest": {
        "keywords": ["pest", "insect", "aphid", "caterpillar", "bug"],
        "response": "For pest control: use integrated pest management (IPM). Consider neem oil, "
                    "companion planting, and biological controls. Avoid excessive pesticides."
    },
    "irrigation": {
        "keywords": ["irrigation", "water", "drip", "sprinkler"],
        "response": "Efficient irrigation: drip irrigation saves water. Water early morning or late evening. "
                    "Monitor soil moisture. Mulching helps retain moisture."
    },
    "disease": {
        "keywords": ["disease", "fungus", "blight", "rot", "mildew", "leaf spot"],
        "response": "For plant diseases: remove infected parts, ensure good air circulation, "
                    "use fungicides sparingly. Crop rotation and resistant varieties help prevent diseases."
    },
    "weather": {
        "keywords": ["weather", "rain", "frost", "drought", "temperature"],
        "response": "Monitor weather for farming: use forecasts for irrigation and harvest. "
                    "Frost protection: cover plants or use sprinklers. During drought, prioritize water-efficient crops."
    },
    "soil": {
        "keywords": ["soil", "ph", "sandy", "clay", "loam"],
        "response": "Healthy soil: test pH (6-7 for most crops). Add organic matter, practice crop rotation. "
                    "Different soil types need different management - loamy soil is ideal for most crops."
    },
    "harvest": {
        "keywords": ["harvest", "harvesting", "when to harvest"],
        "response": "Harvest at optimal maturity. Check crop-specific indicators: color, size, moisture. "
                    "Harvest in cool morning hours for better quality."
    },
    "organic": {
        "keywords": ["organic", "organic farming", "chemical-free"],
        "response": "Organic farming: use compost, green manure, crop rotation. Avoid synthetic pesticides. "
                    "Certification requirements vary by region."
    },
    "greeting": {
        "keywords": ["hi", "hello", "hey"],
        "response": "Hello! I'm your AI farming assistant. Ask me about fertilizers, pests, diseases, "
                    "irrigation, soil, weather, or harvest tips!"
    },
    "thanks": {
        "keywords": ["thank", "thanks"],
        "response": "You're welcome! Happy farming! 🌱"
    },
}


def get_chatbot_response(user_input: str) -> Tuple[str, float]:
    """
    Get response from AI farmer chatbot
    Returns: (response_text, confidence)
    """
    if not user_input or not user_input.strip():
        return "Please ask an agriculture-related question.", 0.5

    text = user_input.lower().strip()

    for category, data in AGRICULTURE_KB.items():
        for kw in data["keywords"]:
            if kw in text:
                return data["response"], 0.9

    # Default fallback
    return (
        "I'm not sure about that specific question. Try asking about: fertilizers, pests, "
        "diseases, irrigation, soil, weather, or harvest tips. I'm here to help with farming!",
        0.6
    )
