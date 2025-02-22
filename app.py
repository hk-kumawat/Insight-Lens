import google.generativeai as genai
import PIL.Image
import streamlit as st
import io

api_key = st.secrets["GEMINI_API_KEY"]  # Fetches the API key from Streamlit secrets

# Function to get the Gemini AI response
def get_gemini_response(api_key, prompt, image_bytes):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content([prompt, image_bytes])
    return response.text

# Function to auto-generate a caption and a structured description for the uploaded image
def generate_image_summary(api_key, image_bytes):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    # Generate a one-line caption and a concise description for the image
    caption_response = model.generate_content(["Provide a short, one-line caption describing the image.", image_bytes])
    description_response = model.generate_content(["Provide a detailed yet brief, structured summary with appropriate emojis to make it engaging and easy to read.", image_bytes])
    return caption_response.text, description_response.text

# Initialize the Streamlit app
st.set_page_config(page_title="📸 InsightLens 🔍", layout="centered")

# Title and subtitle with animations (fade-in and glowing effect)
title_color = "#1c4966"  # Static color for both light and dark themes

st.markdown(f"""
    <style>
        @keyframes fadeIn {{
            0% {{ opacity: 0; }}
            100% {{ opacity: 1; }}
        }}
        .fade-in {{
            animation: fadeIn 2s ease-in-out;
        }}
        .glowing {{
            color: {title_color};  /* Title color dynamically set */
            text-shadow: 
                0 0 10px #00A6FF, /* Bright blue glow */
                0 0 20px #00A6FF, 
                0 0 30px #00A6FF, 
                0 0 40px #00A6FF, 
                0 0 50px #00A6FF, 
                0 0 60px #00A6FF;
            animation: glowing 1.5s infinite alternate;
        }}
        @keyframes glowing {{
            0% {{ text-shadow: 0 0 10px #00A6FF, 0 0 20px #00A6FF, 0 0 30px #00A6FF, 0 0 40px #00A6FF; }}
            50% {{ text-shadow: 0 0 20px #00A6FF, 0 0 30px #00A6FF, 0 0 40px #00A6FF, 0 0 50px #00A6FF; }}
            100% {{ text-shadow: 0 0 10px #00A6FF, 0 0 20px #00A6FF, 0 0 30px #00A6FF, 0 0 40px #00A6FF; }}
        }}
    </style>
    <h1 class="fade-in glowing" style="text-align: center; font-weight: bold;">🖼️ InsightLens 🤖</h1>
    <h3 class="fade-in" style="text-align: center; color: #FF5722;">Upload an image to explore its details and ask questions!</h3>
""", unsafe_allow_html=True)

st.write("---")
st.write("### Step 1: Upload a photo, get a quick overview, and dive into details! 🌟")

# File uploader to allow users to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None

# Create session state to hold caption and description to prevent re-generation
if "caption" not in st.session_state:
    st.session_state.caption = ""
if "description" not in st.session_state:
    st.session_state.description = ""

if uploaded_file is not None and api_key:
    try:
        # Open the uploaded image with a fade-in effect
        image = PIL.Image.open(uploaded_file)
        st.image(image, use_container_width=True)

        # Convert image to bytes
        image_bytes = io.BytesIO()
        image.save(image_bytes, format="PNG")
        image_bytes = image_bytes.getvalue()

        # Generate a brief caption and a structured description only once
        if not st.session_state.caption and not st.session_state.description:
            caption, description = generate_image_summary(api_key, image_bytes)
            st.session_state.caption = caption
            st.session_state.description = description

        # Display the caption and description from session state
        st.markdown(f"<p class='fade-in' style='color: #FF5733; font-size: 24px; text-align: center; font-weight: bold;'>{st.session_state.caption}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='fade-in' style='color: #4CAF50; font-size: 18px;'>🔍 Image Details:\n\n{st.session_state.description}</p>", unsafe_allow_html=True)

    except Exception as e:
        if "HARM_CATEGORY_SEXUALLY_EXPLICIT" in str(e):
            st.error("🚫 InsightLens couldn't generate details due to sensitive content detected. Try a different image!")
        else:
            st.error(f"🔄 Something went wrong! Error: {e}")

st.write("---")
# Input prompt for the user's question, with a placeholder text
st.write("### Step 2: Ask a Question About the Image")
prompt = st.text_input("Ask something about the image (e.g., 'What is happening here?'):", key="input")

# Button to submit the request with an animation effect
submit = st.button("🔍 Get Answer")

# If the submit button is clicked, configure the API key and get the Gemini AI response
if submit and api_key and image is not None:
    try:
        # Convert image to bytes
        image_bytes = io.BytesIO()
        image.save(image_bytes, format="PNG")
        image_bytes = image_bytes.getvalue()

        response = get_gemini_response(api_key, prompt, image_bytes)
        st.subheader("💡 AI's Response:")
        st.write(response)
        st.balloons()  # Celebration balloons for an interactive touch!
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Show footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #7f8c8d; font-size: 16px;'>"
    "<p style='text-align: center;'>🔮 <strong>|Brought to Life By</strong> - Harshal Kumawat| 🤖</p>"
    "</div>",
    unsafe_allow_html=True
)
