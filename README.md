# 🧠 NLP InsightHub

### 🚀 Multi-Task Text Intelligence Platform

<p align="center">
  <b>Transform raw text into meaningful insights using modern NLP & Transformer-based AI.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14-blue?logo=python">
  <img src="https://img.shields.io/badge/NLP-Text%20Intelligence-purple">
  <img src="https://img.shields.io/badge/Streamlit-Interactive%20UI-red?logo=streamlit">
  <img src="https://img.shields.io/badge/HuggingFace-Transformers-yellow?logo=huggingface">
  <img src="https://img.shields.io/badge/spaCy-NER-orange">
  <img src="https://img.shields.io/badge/License-MIT-green">
</p>

---

## 🌟 Overview

**NLP InsightHub** is an interactive Natural Language Processing platform designed to analyze unstructured text and generate meaningful insights through a modern Streamlit dashboard.

The platform combines **traditional NLP techniques**, **machine learning utilities**, and **Transformer-based models** to perform multiple text intelligence tasks from a single interface.

> 💡 **One platform. Multiple NLP tasks. Actionable text insights.**

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🧹 **Text Preprocessing** | Tokenization, stop-word removal, lemmatization and text cleaning |
| 📊 **Text Statistics** | Word count, sentence count, character count and text metrics |
| 😊 **Sentiment Analysis** | Detects the emotional tone of text |
| 🔍 **Named Entity Recognition** | Extracts people, organizations, locations, dates and other entities |
| 🏷️ **Zero-Shot Classification** | Classifies text into user-defined categories |
| 🔑 **Keyword Analysis** | Identifies frequently occurring meaningful words |
| ☁️ **Word Cloud** | Visualizes important words from the text |
| 📈 **Interactive Visualizations** | Charts and graphical text insights |
| 📥 **Analysis Report** | Downloadable analysis results |
| 🎨 **Streamlit Dashboard** | Interactive and user-friendly web interface |

---

## 🧠 NLP Pipeline

```text
                    👤 User Input
                         │
                         ▼
              ┌─────────────────────┐
              │    Streamlit UI     │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Text Preprocessing  │
              │ • Tokenization      │
              │ • Stopword Removal  │
              │ • Lemmatization     │
              │ • Text Cleaning     │
              └──────────┬──────────┘
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
   😊 Sentiment      🔍 NER       🏷️ Classification
          │              │              │
          └──────────────┼──────────────┘
                         ▼
              ┌─────────────────────┐
              │ Keyword & Statistics│
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   Visualization     │
              │ Charts + Word Cloud │
              └──────────┬──────────┘
                         │
                         ▼
                  📄 Final Report

🔬 NLP Techniques
1. 🧹 Text Preprocessing

The system cleans and prepares input text using:

🔤 Tokenization
🔡 Lowercase conversion
🛑 Stop-word removal
🌱 Lemmatization
🔗 URL removal
✨ Special-character removal
2. 😊 Sentiment Analysis

A Transformer-based sentiment model analyzes the emotional tone of the input text.

Possible outputs:

🟢 Positive
🔴 Negative
3. 🔍 Named Entity Recognition

Using spaCy, the system identifies important entities such as:

👤 PERSON
🏢 ORGANIZATION
📍 LOCATION
📅 DATE
💰 MONEY
4. 🏷️ Zero-Shot Text Classification

The Transformer model can classify text without requiring task-specific training.

Example categories:

💻 Technology
💼 Business
⚽ Sports
🏛️ Politics
🎬 Entertainment
🎓 Education
5. 🔑 Keyword Analysis

The system identifies frequently occurring meaningful words from processed text to highlight the main topics and important terms.

6. ☁️ Word Cloud

Frequently occurring words are visualized using a Word Cloud, making dominant topics easy to identify at a glance.

🛠️ Tech Stack
Technology	Purpose
🐍 Python	Core Programming
🧹 NLTK	Text Processing
🔍 spaCy	Named Entity Recognition
🤗 Hugging Face Transformers	Transformer-based NLP Models
🔥 PyTorch	Deep Learning Backend
📊 Scikit-learn	Machine Learning Utilities
🐼 Pandas	Data Processing
📈 Matplotlib	Data Visualization
☁️ WordCloud	Keyword Visualization
🎨 Streamlit	Interactive Web Interface
📸 Application Screenshots

All 16 project screenshots are available in the screenshots folder.

🖥️ NLP InsightHub Dashboard

😊 Sentiment Analysis

🔍 Text Analysis

☁️ Visualization

📌 Additional screenshots demonstrating the complete application workflow are available in the screenshots folder.

📁 Project Structure
NLP_InsightHub/
│
├── 📂 data/
│   └── nlp_dataset.csv
│
├── 📂 models/
│
├── 📂 screenshots/
│   ├── Screenshot (2).png
│   ├── Screenshot (3).png
│   ├── Screenshot (4).png
│   ├── Screenshot (5).png
│   ├── Screenshot (6).png
│   ├── Screenshot (7).png
│   ├── Screenshot (8).png
│   ├── Screenshot (9).png
│   ├── Screenshot (10).png
│   ├── Screenshot (11).png
│   ├── Screenshot (12).png
│   ├── Screenshot (13).png
│   ├── Screenshot (14).png
│   ├── Screenshot (15).png
│   ├── Screenshot (16).png
│   └── Screenshot (17).png
│
├── 📓 NLP_InsightHub_Development.ipynb
├── 🐍 app.py
├── 📄 requirements.txt
├── 📖 README.md
└── 🚫 .gitignore

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/revarao31/NLP_InsightHub.git
2️⃣ Open the Project
cd NLP_InsightHub
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Download NLP Resources

Run:

import nltk

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
▶️ Run the Application

Launch the Streamlit dashboard:

streamlit run app.py

The application will automatically open in your browser.

🧪 Example Input
🟢 Positive Example
The new technology platform is fast, reliable, and extremely useful for students.

The application can generate:

😊 Sentiment
🔍 Named Entities
🏷️ Text Classification
🔑 Keywords
📊 Text Statistics
☁️ Word Cloud
📈 Visual Insights
🔴 Negative Example
The application is slow, confusing, and difficult to use.

The system can identify the negative sentiment and provide additional NLP insights.

🎯 Project Objectives

The main objectives of NLP InsightHub are:

🧠 Build an interactive NLP analysis platform.
🤗 Combine traditional NLP with modern Transformer models.
🎨 Simplify complex NLP analysis through an intuitive visual interface.
🔍 Extract meaningful information from unstructured text.
📚 Demonstrate practical applications of NLP and AI.
🚀 Provide multiple NLP capabilities through a single platform.
💡 Why NLP InsightHub?

Traditional NLP applications often focus on a single task.

NLP InsightHub brings multiple NLP capabilities together in one platform:

                 📝 Input Text
                      │
                      ▼
             🧹 Preprocessing
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       😊 Sentiment  🔍 NER   🏷️ Classification
          │           │           │
          └───────────┼───────────┘
                      ▼
               🔑 Keywords
                      │
                      ▼
                📊 Statistics
                      │
                      ▼
              ☁️ Visualization
                      │
                      ▼
               📥 Final Report

This makes the project a practical end-to-end NLP demonstration platform.

📊 Dataset

A sample NLP dataset is included in:

data/nlp_dataset.csv

The dataset contains:

Column	Description
📝 text	Sample text used for NLP analysis
😊 sentiment	Positive or negative sentiment
🏷️ category	Text category

The dataset can be used for experimentation, testing, analysis and demonstration purposes.

📌 Project Highlights
🧠 Multi-Task NLP Platform
🤗 Transformer-Based AI
😊 Sentiment Analysis
🔍 Named Entity Recognition
🏷️ Zero-Shot Classification
🧹 Text Preprocessing
🔑 Keyword Analysis
☁️ Word Cloud
📊 Text Statistics
📈 Interactive Visualizations
🎨 Streamlit Dashboard
📥 Downloadable Analysis Reports
🚀 Future Enhancements

The platform can be further enhanced with:

🌐 Multilingual NLP support
🤖 LLM-powered text summarization
💬 Question Answering
📄 PDF and document analysis
🧠 Topic modeling
🎙️ Speech-to-text analysis
📊 Advanced analytics dashboard
☁️ Cloud deployment
🔐 User authentication
🤝 Conversational AI integration
👩‍💻 Author
Reva Rao

NLP & AI Project

🔗 GitHub: @revarao31

📌 Repository: NLP_InsightHub

⭐ Support

If you find NLP InsightHub useful or interesting, consider giving the repository a ⭐ on GitHub.

Your support is appreciated! 💙
