import google.generativeai as genai
import PIL.Image
import streamlit as st

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
    caption_response = model.generate_content(["Provide a short, one-line caption describing the image.", image])
    description_response = model.generate_content(["Provide a detailed yet brief, structured summary with appropriate emojis to make it engaging and easy to read.", image])
    return caption_response.text, description_response.text

# Initialize Streamlit app
st.set_page_config(page_title="📸 InsightLens 🔍", layout="centered")

# Title and subtitle
st.markdown("""
    <h1 style="text-align: center; color: #00A6FF;">🖼️ InsightLens 🤖</h1>
    <h3 style="text-align: center; color: #FF5722;">Upload an image to explore its details and ask questions!</h3>
""", unsafe_allow_html=True)

st.write("---")
st.write("### Step 1: Upload a photo, get a quick overview, and dive into details! 🌟")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Store uploaded image in session state
if uploaded_file is not None:
    if "image" not in st.session_state:
        st.session_state.image = PIL.Image.open(uploaded_file)
    image = st.session_state.image
else:
    image = None

# Store caption and description in session state
if "caption" not in st.session_state:
    st.session_state.caption = ""
if "description" not in st.session_state:
    st.session_state.description = ""

# Display the uploaded image and generate details
if image is not None and api_key:
    st.image(image, use_container_width=True)
    
    if not st.session_state.caption and not st.session_state.description:
        caption, description = generate_image_summary(api_key, image)
        st.session_state.caption = caption
        st.session_state.description = description

    st.markdown(f"<p style='color: #FF5733; font-size: 24px; text-align: center; font-weight: bold;'>{st.session_state.caption}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #4CAF50; font-size: 18px;'>🔍 Image Details:\n\n{st.session_state.description}</p>", unsafe_allow_html=True)

st.write("---")
# Input prompt for the user's question
st.write("### Step 2: Ask a Question About the Image")
prompt = st.text_input("Ask something about the image (e.g., 'What is happening here?'):", key="input")

# If the button is clicked, store response in session state
if st.button("🔍 Get Answer") and api_key and image is not None:
    if "response" not in st.session_state or st.session_state.prompt != prompt:
        st.session_state.response = get_gemini_response(api_key, prompt, image)
        st.session_state.prompt = prompt  # Store the latest prompt

    st.subheader("💡 AI's Response:")
    st.write(st.session_state.response)
    st.balloons()  # Celebration effect!

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #7f8c8d; font-size: 16px;'>"
    "<p><strong>🔮 | Brought to Life By - Harshal Kumawat | 🤖</strong></p>"
    "</div>",
    unsafe_allow_html=True
)
