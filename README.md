# **InsightLens 🖼️🔍**

![InsightLens Logo](https://github.com/user-attachments/assets/8c9825be-d9de-4488-a770-24431601b571)

## Overview

**InsightLens** is an AI-powered image analysis tool designed to deliver quick, insightful, and contextually accurate information about images. Powered by **Google Generative AI (Gemini)**, **Streamlit**, and various AI libraries, InsightLens generates captions, offers detailed descriptions with emojis, and allows users to ask questions about image content. 

Whether you're using InsightLens to enhance **content creation**, explore **visual storytelling**, or **analyze images for insights**, this tool provides a seamless and interactive experience that’s both informative and engaging.

## Live Demo

Experience InsightLens in action! 👉🏻 [![Try InsightLens 🌟](https://insight-lens.streamlit.app/)

<br>

_Explore the story behind every image with InsightLens!_

<p align="center">
  <img src="https://github.com/user-attachments/assets/916a1a5c-888f-460e-bff1-ffca66e0fe14" alt="InsightLens Demo" width="500">
</p>


<br>

## Table of Contents

1. [Features](#features)
2. [How It Works](#how-it-works)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Technologies Used](#technologies-used)
6. [Results](#results)
7. [Conclusion](#conclusion)
8. [Future Enhancements](#future-enhancements)
9. [License](#license)
10. [Contact](#contact)

<br>

## Features🌟

- **Automatic Captioning**: Generates a brief, one-line caption for uploaded images.
- **Detailed Descriptions**: Provides concise summeries that highlight the primary content and context of the image.
- **Image Q&A**: Users can ask questions about the image's content, with responses powered by **Gemini AI**.
- **Interactive User Interface**: InsightLens is designed with animations, style effects, and balloons for a lively experience.
- **Privacy by Design**: InsightLens does not store any images or questions asked, ensuring a secure and private interaction every time.

<br>

## How It Works🧠

1. **Upload an Image**: The user uploads an image in `.jpg`, `.jpeg`, or `.png` format.
2. **Automatic Captioning**: InsightLens auto-generates a caption using **Gemini AI**.
3. **Detailed Summaries**: A structured, emoji-enhanced description provides a deeper understanding of the image.
4. **Interactive Q&A**: Users can ask specific questions about the image, and the AI responds with insightful answers.
5. **Visual Enhancements**: InsightLens offers a polished user experience with glowing titles, fade-in effects, and celebratory balloons upon successful interactions.

<br>

## Installation🛠

1. **Clone the repository**:
   ```bash
   git clone https://github.com/hk-kumawat/InsightLens.git
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup environment variables**:
   - Obtain an API key from **Google Generative AI**.
   - Create a `.env` file in the root directory and add:
     ```env
     GEMINI_API_KEY=your_gemini_api_key
     ```
   - Replace `your_gemini_api_key` with your actual **Gemini API Key**.

<br>

## Usage🚀

1. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

2. **Upload and Explore**: 
   - Upload an image and instantly receive a caption, detailed description, and engage in Q&A about the image.
   
<br>

## Technologies Used💻

- **Programming Language**: Python
- **Libraries**:
  - `streamlit` — For creating the user interface.
  - `Pillow` — For image processing.
  - `python-dotenv` — Manages environment variables.
  - `google-generativeai` — For generating captions, descriptions, and answering questions.
  
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

## Conclusion📚

The **InsightLens** project exemplifies the potential of AI in image analysis, creating a valuable tool for visually rich applications. By integrating **Google Generative AI (Gemini)** and **Streamlit**, InsightLens enables users to explore image content in a meaningful and interactive way.

Real-world applications for InsightLens include **content creation** (captions and descriptions for social media), **education** (visual storytelling) and **research** (image-based inquiries). This makes InsightLens a versatile tool for both personal and professional uses.

<br>

## Future Enhancements🚀

1. **Multi-turn Conversation**: Enable the assistant to maintain conversation context across multiple interactions.
2. **Advanced Emotion Detection**: Expand sentiment capabilities to identify a wider range of emotional tones in image context.
3. **Integration with External Services**: Extend InsightLens’s functionality to connect with APIs for additional insights (e.g., related news or facts about image objects).
4. **Voice Interaction**: Add voice input/output for a more dynamic user experience.

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

---

### **Where visuals meet intelligence—thank you for discovering what InsightLens can do! Let's keep exploring new horizons together. 🌍🔍**


> "Every image has a story; let InsightLens help you discover it, one image at a time." - Harshal Kumawat
