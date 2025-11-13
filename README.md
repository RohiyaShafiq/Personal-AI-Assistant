 # 🧠 Nova AI – Your Personal AI Assistant

A Real-Time Voice and Vision-Powered Chatbot built with **Python**, **Gradio**, and **OpenCV**

---

## 🚀 Overview

Nova AI is a personal AI assistant capable of:

- Listening to your voice continuously  
- Understanding your queries using **Groq’s transcription API**  
- Responding intelligently using a **custom AI Agent**  
- Speaking back to you using **Google Text-to-Speech (gTTS)**  
- Showing live webcam feed for real-time interaction  

Built using **Gradio**, it provides an elegant web interface combining chat + live video + voice assistant in **one app**.  

---

## 🧩 Features

- ✅ **Real-time Speech Recognition** – Converts your voice into text using `transcribe_with_groq()`  
- ✅ **AI Chat Agent** – Generates intelligent replies using `ask_agent()`  
- ✅ **Text-to-Speech (TTS)** – Speaks responses aloud with gTTS  
- ✅ **Live Webcam Integration** – Displays real-time camera feed using OpenCV  
- ✅ **Continuous Listening Mode** – No need to press record; it keeps listening and responding  
- ✅ **Interactive Gradio Interface** – Simple UI for both chat and camera interaction  

---

## 🛠️ Tech Stack

| Component       | Description                             |
|-----------------|-----------------------------------------|
| Python          | Core programming language               |
| Gradio          | Web interface for chatbot + camera      |
| Groq API        | For speech-to-text transcription        |
| OpenCV          | Webcam integration                       |
| gTTS            | Google Text-to-Speech for voice output  |
| Custom AI Agent | Generates intelligent chat responses    |

---

## ⚙️ How It Works

Nova AI combines **speech, AI, and vision** to provide a seamless personal assistant experience:

1. **Continuous Audio Recording**  
   - The app continuously listens through your microphone using `record_audio()`.  
   - Audio is saved as a temporary file (`audio_question.mp3`) for processing.  

2. **Speech-to-Text Conversion**  
   - Nova AI uses **Groq’s transcription API** (`transcribe_with_groq()`) to convert your spoken words into text.  
   - This allows the AI to understand your queries in real-time.  

3. **AI Response Generation**  
   - The transcribed text is sent to a **custom AI Agent** (`ask_agent()`), which generates intelligent responses.  
   - The AI can answer questions, provide recommendations, or chat naturally with the user.  

4. **Text-to-Speech (TTS) Output**  
   - The AI response text is converted to audio using **Google Text-to-Speech (gTTS)**.  
   - Nova AI plays the audio, allowing you to hear the response instead of just reading it.  

5. **Webcam Integration**  
   - A live webcam feed is displayed using **OpenCV**.  
   - The webcam interface is optimized for smooth performance, low latency, and real-time interaction.  

6. **Gradio Web Interface**  
   - The entire system runs in a **Gradio Blocks interface**.  
   - The interface combines:  
     - Live webcam feed  
     - Chatbot conversation window  
     - Continuous voice interaction  
     - Buttons to start/stop camera and clear chat  

7. **Event Loop & Continuous Listening**  
   - The system continuously records, transcribes, generates responses, and plays audio in a loop.  
   - The conversation persists in the chat window, and you can clear it at any time.  

**In short:** Nova AI listens to your voice, understands your query, responds intelligently, speaks aloud, and shows a live webcam feed — all in real-time.

---

---
