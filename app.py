import google.generativeai as genai
import PIL.Image
import streamlit as st
from dotenv import load_dotenv
#import os

# Load environment variables, including separate API keys for each task
load_dotenv()

#api_key = os.environ["API_KEY"]  

 
caption_api_key = st.secrets["CAPTION_API_KEY"]  # API key for caption generation
description_api_key = st.secrets["DESCRIPTION_API_KEY"]  # API key for description generation
answer_api_key = st.secrets["ANSWER_API_KEY"]  # API key for answering questions about the image

# Function to get a caption with a specific API key
def generate_caption(api_key, image):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    # Prompt to generate a short, one-line caption for the image
    caption_response = model.generate_content(["Provide a short, one-line caption describing the image.", image])
    return caption_response.text

# Function to get a description with a different API key
def generate_description(api_key, image):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    # Prompt to generate a structured summary with emojis
    description_response = model.generate_content(["Provide a detailed yet brief, structured summary with appropriate emojis to make it engaging and easy to read.", image])
    return description_response.text

# Function to get an answer to a user’s question about the image using a third API key
def get_answer(api_key, prompt, image):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content([prompt, image])
    return response.text

# Streamlit app setup
st.set_page_config(page_title="📸 InsightLens 🔍", layout="centered")

# Display title and subtitle
st.markdown("<h1 style='text-align: center;'>🖼️ InsightLens 🤖</h1>", unsafe_allow_html=True)
st.write("### Step 1: Upload an image to generate a caption and details! 🌟")

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None
caption = ""
description = ""

if uploaded_file is not None and caption_api_key and description_api_key:
    try:
        # Open the uploaded image
        image = PIL.Image.open(uploaded_file)
        st.image(image, use_container_width=True)
        
        # Generate caption using the first API key
        caption = generate_caption(caption_api_key, image)
        
        # Generate description using the second API key
        description = generate_description(description_api_key, image)
        
        # Display caption and description
        st.markdown(f"<p style='color: #FF5733; font-size: 24px; text-align: center;'>{caption}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #4CAF50; font-size: 18px;'>🔍 Image Details:\n\n{description}</p>", unsafe_allow_html=True)
        
    except Exception as e:
        if "HARM_CATEGORY_SEXUALLY_EXPLICIT" in str(e):
            st.error("🚫 InsightLens couldn't generate details due to sensitive content detected. Try a different image!")
        else:
            st.error("🔄 Something went wrong! Try refreshing or using another image.")

st.write("### Step 2: Ask a question about the image")
prompt = st.text_input("Ask something about the image (e.g., 'What is happening here?'):", key="input")
submit = st.button("🔍 Get Answer")

# Use a third API key for answering questions
if submit and answer_api_key and image is not None:
    try:
        response = get_answer(answer_api_key, prompt, image)
        st.subheader("💡 AI's Response:")
        st.write(response)
        st.balloons()
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #7f8c8d; font-size: 16px;'>"
    "<p>🔮 <strong>Brought to Life By Harshal Kumawat</strong> 🤖</p>"
    "</div>",
    unsafe_allow_html=True
)
