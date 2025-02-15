<a id="readme-top"></a>

# **InsightLens 🖼️🔍**

<p align="center">
  <img src="https://github.com/user-attachments/assets/3ec8fdf6-c725-4277-86e8-7e10c4ba6772" alt="InsightLens" width="500">
</p>

## Overview

**InsightLens** is an AI-powered image analysis tool designed to deliver quick, insightful, and contextually accurate information about images. Powered by **Google's Gemini-1.5-Flash model** and **Streamlit**. And InsightLens generates automatic captions, offers detailed insights, and answers to specific questions about the image content.

Whether you're using InsightLens to enhance **content creation**, explore **visual storytelling**, or **analyze images for insights**, this tool provides a seamless and interactive experience that’s both informative and engaging.

<br>


## Live Demo

Experience InsightLens in action! 👉🏻 [![Try InsightLens! 🌟](https://img.shields.io/badge/Try%20InsightLens!-blue)](https://insight-lens.streamlit.app/)

<br>

_Below is a preview of InsightLens analyzing an image and providing detailed insights! 👇_

<p align="center">
  <img src="https://github.com/user-attachments/assets/916a1a5c-888f-460e-bff1-ffca66e0fe14" alt="InsightLens Demo" width="500">
</p>


<br>


## Learning Journey 🗺️

Building InsightLens was an exciting exploration at the crossroads of generative AI and interactive web development. Here’s a snapshot of my journey:

- **Inspiration:**  
  Inspired by the potential of generative AI, I wanted to create a tool that could not only describe images but also engage users by answering their questions about the content.
  
- **Why I Made It:**  
  I aimed to blend art and technology by providing dynamic insights into images, using cutting-edge AI to generate both creative captions and structured, detailed descriptions.
  
- **Challenges Faced:**  
  - **API Integration:** Integrating with Google’s Gemini AI required careful handling of API keys and ensuring smooth communication with the service.
  - **Interactive Design:** Creating an engaging and intuitive Streamlit interface with custom animations and styling.
  - **Error Handling:** Building robust error handling to manage unexpected inputs and sensitive content.
  - **Performance Optimization:** Balancing quick response times with detailed analysis capabilities.

- **What I Learned:**  
  - Effective use of generative AI for multimedia content analysis.
  - How to build visually appealing, responsive apps with Streamlit.
  - Advanced techniques in API integration and user input processing.

Every step of the process has deepened my understanding of AI and web development, and reinforced my passion for creating tools that merge creativity with technology.

<br>


## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Technologies Used](#technologies-used)
5. [Results](#results)
6. [Directory Structure](#directory-structure)
7. [Future Enhancements](#future-enhancements)
8. [Contributing](#contributing)
9. [License](#license)
10. [Contact](#contact)

<br>


## Features🌟

- **Automatic Captioning**: Generates a brief, one-line caption for uploaded images.
  
- **Detailed Descriptions**: Provides concise summeries that highlight the primary content and context of the image.
  
- **Image Q&A**: Users can ask questions about the image's content, with responses powered by **Gemini AI**.

- **Easy-to-Use Interface:** A simple, intuitive layout designed for both casual users and tech enthusiasts.
  
- **Privacy by Design**: InsightLens does not store any images or questions asked, ensuring a secure and private interaction every time.

<br>


## Installation🛠

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/hk-kumawat/InsightLens.git
   cd hk-kumawat-insight-lens
   ```

2. **Create & Activate a Virtual Environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate       # On Windows: venv\Scripts\activate
   ```

3. **Install Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Your Gemini API Key:**
   - Create a `.streamlit/secrets.toml` file.
   - Add your Gemini API key:
     ```toml
     [GEMINI]
     api_key = "your_gemini_api_key_here"
     ```
   - Alternatively, set your API key as an environment variable.

5. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

<br>


## Usage🚀

1. **Launch the Application:**
   ```bash
   streamlit run app.py
   ```

2. **Using the App:**
   - Upload an image using the file uploader
   - View the auto-generated caption and structured description
   - Ask specific questions about the image
   - Get AI-powered responses and insights

3. **Features in Action:**
   - **Image Upload:** Supports JPG, JPEG, and PNG formats
   - **Auto Analysis:** Receives immediate caption and description
   - **Q&A:** Ask any question about the uploaded image
   - **Interactive Elements:** Enjoy animations and celebrations

<br>


## Technologies Used💻

- **Programming Language**: Python
- **Libraries**:
  - `streamlit` — For creating the user interface.
  - `Pillow` — For image processing.
  - `python-dotenv` — Manages environment variables.
  - `google-generativeai` — For generating captions, descriptions, and answering questions.

- **Frontend:**
  - `HTML/CSS`
  - `Custom animations`
 
- **API**:
  - **Gemini API** by Google Generative AI — Powers the core captioning, description generation, and Q&A functionalities.

<br>


## Results🏆

InsightLens successfully analyzes images, providing an insightful, one-line caption along with a structured, emoji-based description and engaging Q&A responses. This AI-powered analysis is useful in applications ranging from social media to education and creative design.

<p align="center">
  <img src="https://github.com/user-attachments/assets/916a1a5c-888f-460e-bff1-ffca66e0fe14" alt="InsightLens Example" width="500"/>
</p>

In the above example, InsightLens provides a brief caption, structured description, and accurate answers to user questions about the image content.

<br>


## Directory Structure📁

```plaintext
hk-kumawat-insight-lens/
├── README.md         # Project documentation
├── LICENSE           # License information
├── app.py            # Streamlit application for generating image insights
└── requirements.txt  # List of dependencies
```

<br>


## Future Enhancements🚀

1. **Multi-turn Conversation**:
  Enable the assistant to maintain conversation context across multiple interactions.
   
2. **Advanced Emotion Detection**:
  Expand sentiment capabilities to identify a wider range of emotional tones in image context.
   
3. **Integration with External Services**:
  Extend InsightLens’s functionality to connect with APIs for additional insights (e.g., related news or facts about image objects).
   
4. **Voice Interaction**:
  Add voice input/output for a more dynamic user experience.
   
5. **Multi-Model Integration:**  
  Integrate additional AI models to provide diverse perspectives on image analysis, such as object detection and sentiment analysis.

6. **Social Sharing:**  
  Allow users to easily share generated insights and images on social media platforms.

7. **User Feedback Loop:**  
  Integrate a mechanism for users to provide feedback on the AI's responses, helping to continuously improve accuracy and relevance.


<br>


## Contributing🤝
Contributions make the open source community such an amazing place to learn, inspire, and create. 🙌 Any contributions you make are greatly appreciated! 😊

Have an idea to improve this project? Go ahead and fork the repo to create a pull request, or open an issue with the tag **"enhancement"**. Don't forget to give the project a star! ⭐ Thanks again! 🙏

<br>

1. **Fork** the repository.

2. **Create** a new branch:
   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Commit** your changes with a descriptive message.

4. **Push** to your branch:
   ```bash
   git push origin feature/YourFeatureName
   ```

5. **Open** a Pull Request detailing your enhancements or bug fixes.

<br> 



## License📝

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for details.

<br>

## Contact

### 📬 Get in Touch!
Feel free to reach out for collaborations or questions:

- [![GitHub](https://img.shields.io/badge/GitHub-hk--kumawat-blue?logo=github)](https://github.com/hk-kumawat) 💻 — Explore more projects by Harshal Kumawat.
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-Harshal%20Kumawat-blue?logo=linkedin)](https://www.linkedin.com/in/harshal-kumawat/) 🌐 — Let's connect professionally.
- [![Email](https://img.shields.io/badge/Email-harshalkumawat100@gmail.com-blue?logo=gmail)](mailto:harshalkumawat100@gmail.com) 📧 — Reach out for inquiries or collaboration.

<br>


## Thanks for exploring—happy discovering! 📸

> "Every image tells a story, let AI help you discover it." - InsightLens

<p align="right">
  (<a href="#readme-top">back to top</a>)
</p>
