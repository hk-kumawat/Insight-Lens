import google.generativeai as genai
import PIL.Image
import streamlit as st
import os
from dotenv import load_dotenv

# Load the environment variables, including the API key
load_dotenv()
api_key = st.secrets["GEMINI_API_KEY"]  # Fetches the API key from Streamlit secrets

# Function to get the Gemini AI response
def get_gemini_response(api_key, prompt, image):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content([prompt, image])
    return response.text

# Function to auto-generate a caption and a structured description for the uploaded image
def generate_image_summary(api_key, image):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    # Generate a one-line caption and a concise description for the image
    caption_response = model.generate_content([image])
    description_response = model.generate_content(["Provide a concise and engaging summary with emojis.", image])
    return caption_response.text.strip().split('.')[0], description_response.text

# Initialize the Streamlit app
st.set_page_config(page_title="📸 InsightLens 🔍", layout="centered")

# Title and subtitle with animations
st.markdown("<h1 style='text-align: center; font-weight: bold;'>✨ InsightLens 🤖</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Upload an image to explore its details and ask questions! 🌟</h3>", unsafe_allow_html=True)
st.write("### Step 1: Upload a photo, get a quick overview, and dive into details!")

# File uploader to allow users to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None
caption = ""
description = ""

if uploaded_file is not None and api_key:
    try:
        # Open the uploaded image with a fade-in effect
        image = PIL.Image.open(uploaded_file)
        st.image(image, use_column_width=True)
        
        # Generate a brief caption and a structured description for the image
        caption, description = generate_image_summary(api_key, image)
        
        # Display the auto-generated caption with style
        st.markdown(f"<p style='color: #FF5733; font-size: 20px; text-align: center; font-weight: bold;'>{caption}</p>", unsafe_allow_html=True)
        
        # Display the structured and emoji-enhanced description
        st.markdown(f"**🔍 Image Details:**\n\n{description}", unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"An error occurred while generating the caption and description: {e}")

# Input prompt for the user's question, with a placeholder text
st.write("### Step 2: Ask a Question About the Image")
prompt = st.text_input("Ask something about the image (e.g., 'What is happening here?'):", key="input")

# Button to submit the request with an animation effect
submit = st.button("🔮 Get AI Insight")

# If the submit button is clicked, configure the API key and get the Gemini AI response
if submit and api_key and image is not None:
    try:
        response = get_gemini_response(api_key, prompt, image)
        st.subheader("💡 AI's Response:")
        st.write(response)
        st.balloons()  # Celebration balloons for an interactive touch!
    except Exception as e:
        st.error(f"An error occurred: {e}")