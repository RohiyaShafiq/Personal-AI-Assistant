# 📚 Chat with Multiple PDFs  
> Interactively chat with your PDF documents using AI 🤖 

## 🚀 Overview  

**Chat with Multiple PDFs** is a Streamlit-based web application that allows users to upload multiple PDF files and ask questions about their contents.  
It extracts text from PDFs, splits them into chunks, embeds the text using **Hugging Face sentence-transformers**, stores them in a **FAISS** vector database, and uses a **Google Flan-T5** model to generate intelligent, context-aware responses.  

This project demonstrates how **Large Language Models (LLMs)** can be integrated with **retrieval-based systems** for document understanding.

---

## 🧩 Features  

- 📄 Upload and process multiple PDF documents simultaneously  
- 💬 Ask natural language questions and get AI-generated answers  
- ⚙️ Uses **FAISS** for vector storage and retrieval  
- 🧠 Supports **contextual conversation** using memory  
- 🤖 Powered by **Flan-T5** and **LangChain** for reasoning and text generation  
- 🌐 Built with a simple and responsive **Streamlit** UI  

---

## 🛠️ Tech Stack  

| Component | Technology |
|------------|-------------|
| **Frontend/UI** | Streamlit |
| **Text Extraction** | PyPDF2 |
| **Text Embedding** | Sentence Transformers (MiniLM-L6-v2) |
| **Vector Store** | FAISS |
| **LLM Model** | Google FLAN-T5 |
| **Framework** | LangChain |
| **Environment Management** | Python dotenv |

---
