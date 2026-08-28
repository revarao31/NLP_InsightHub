# 🧠 NLP InsightHub

### Multi-Task Text Intelligence Platform

Transform raw text into meaningful insights using modern NLP & Transformer-based AI — all from one interactive Streamlit dashboard.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14-blue?logo=python">
  <img src="https://img.shields.io/badge/Streamlit-Interactive%20UI-red?logo=streamlit">
  <img src="https://img.shields.io/badge/HuggingFace-Transformers-yellow?logo=huggingface">
  <img src="https://img.shields.io/badge/spaCy-NER-orange">
</p>

> 🌐 **Try NLP InsightHub live:** [Open the Application](https://nlp-insight.streamlit.app)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🧹 Text Preprocessing | Tokenization, stop-word removal, lemmatization |
| 😊 Sentiment Analysis | Detects emotional tone (positive/negative) |
| 🔍 Named Entity Recognition | Extracts people, orgs, locations, dates |
| 🏷️ Zero-Shot Classification | Classifies text into custom categories |
| 🔑 Keyword Analysis | Highlights frequently occurring terms |
| ☁️ Word Cloud | Visualizes dominant words |
| 📊 Text Statistics | Word, sentence & character counts |
| 📥 Analysis Report | Downloadable results |

## 🛠️ Tech Stack

Python · NLTK · spaCy · Hugging Face Transformers · PyTorch · Scikit-learn · Pandas · Matplotlib · WordCloud · Streamlit

## ⚙️ Installation

```bash
git clone https://github.com/revarao31/NLP_InsightHub.git
cd NLP_InsightHub
pip install -r requirements.txt
```

```python
import nltk
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
```

```bash
streamlit run app.py
```

## 📊 Dataset

`data/nlp_dataset.csv` — sample text data with `text`, `sentiment`, and `category` columns, for testing and demonstration.

## 🚀 Future Enhancements

Multilingual support · LLM-powered summarization · Question Answering · PDF/document analysis · Topic modeling · Cloud deployment

## 👩‍💻 Author

**Reva Rao** — [@revarao31](https://github.com/revarao31)

⭐ If you find NLP InsightHub useful, consider starring the repo!
