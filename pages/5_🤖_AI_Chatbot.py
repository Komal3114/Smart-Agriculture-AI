"""
AI Farmer Chatbot
Answer agriculture-related questions using NLP.
"""
import streamlit as st
from models.chatbot import get_chatbot_response

st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")
st.title("🤖 AI Farmer Chatbot")
st.markdown("Ask any agriculture-related question!")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm your AI farming assistant. Ask me about fertilizers, pests, diseases, irrigation, soil, weather, or harvest tips!"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Ask about farming...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    response, _ = get_chatbot_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()
