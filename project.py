# app.py
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Use the latest supported model
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Define a function to get responses from Gemini
def get_gemini_response(question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Streamlit app UI
st.set_page_config(page_title="Q&A Demo")
st.header("💬 Gemini App")

# Input and button
user_input = st.text_input("Ask a question:", key="input")
submit = st.button("Submit")

# Handle response
if submit and user_input:
    st.subheader("Response:")
    st.write(get_gemini_response(user_input))
