import streamlit as st
import google.generativeai as genai
from PIL import Image
import os




# Configure Gemini
genai.configure(api_key="AIzaSyC8L1t_zZU-fQU3XFsaWGPOX1ZhJokwpz8")

model = genai.GenerativeModel("gemini-pro-vision")

st.set_page_config(page_title="Multimodal AI Chatbot")
st.title("🤖 Multimodal AI Chatbot (Text + Image)")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

uploaded_image = st.file_uploader(
    "Upload an image (optional)",
    type=["png", "jpg", "jpeg"]
)

user_prompt = st.chat_input("Ask something...")

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if user_prompt:
    st.chat_message("user").write(user_prompt)

    inputs = [user_prompt]

    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        inputs.append(image)

    response = model.generate_content(inputs)

    reply = response.text

    st.session_state.messages.append({"role": "user", "content": user_prompt})
    st.session_state.messages.append({"role": "assistant", "content": reply})

    st.chat_message("assistant").write(reply)
