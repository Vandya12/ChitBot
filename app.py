import streamlit as st
from google import genai
from PIL import Image 
#  Gemini API key
api_key = st.secrets["GOOGLE_API_KEY"]

client = genai.Client(api_key=api_key)


icon = Image.open("logo.png")

st.set_page_config(
    page_title="ChitBot",
    page_icon=icon
)

st.image("download.png", width=170)
st.title("Chit Bot")
prompt = st.chat_input("Ask something...")

if prompt:
    st.chat_message("user").write(prompt)

    response = client.models.generate_content(
        model="models/gemini-pro-latest", 
        contents=prompt
    )

    st.chat_message("assistant").write(response.text)
