import google.generativeai as genai
import PIL.Image
import streamlit as st
import os
from dotenv import load_dotenv

# Load the environment variables, including the API key
load_dotenv()
#api_key = os.getenv("API_KEY")  # Fetches the API key from the .env file

api_key = st.secrets["GEMINI_API_KEY"]

# Function to get the Gemini AI response
def get_gemini_response(api_key, prompt, image):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content([prompt, image])
    return response.text

# Function to auto-generate a caption and a description for the uploaded image
def generate_image_summary(api_key, image):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    # Generate a caption and description based on the image content
    caption_response = model.generate_content([image])
    description_response = model.generate_content(["Give a detailed summary of the image.", image])
    return caption_response.text, description_response.text

# Initialize the Streamlit app
st.set_page_config(page_title="📸 Gemini Vision Bot 🔍")

# Title and subtitle
st.title("Gemini Vision Bot 🤖")
st.subheader("Upload an image and let AI describe it! 📷🖼️")
st.write("Simply upload a photo, get a brief overview, then ask any question! 🌟")

# File uploader to allow users to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None
caption = ""
description = ""

if uploaded_file is not None and api_key:
    try:
        # Open the uploaded image
        image = PIL.Image.open(uploaded_file)
        st.image(image, use_column_width=True)
        
        # Generate a brief caption and description for the image
        caption, description = generate_image_summary(api_key, image)
        
        # Display the auto-generated caption and description
        st.markdown(f"**Image Caption:** {caption}")
        st.markdown(f"**Image Description:** {description}")
        
    except Exception as e:
        st.error(f"An error occurred while generating the caption and description: {e}")

# Input prompt for the user's question, with a placeholder text
st.write("### Your Question:")
prompt = st.text_input("Ask something about the image (e.g., 'What is happening here?'):", key="input")

# Button to submit the request
submit = st.button("Get AI Answer")

# If the submit button is clicked, configure the API key and get the Gemini AI response
if submit and api_key and image is not None:
    try:
        response = get_gemini_response(api_key, prompt, image)
        st.subheader("AI's Response:")
        st.write(response)
        st.balloons()
    except Exception as e:
        st.error(f"An error occurred: {e}")
