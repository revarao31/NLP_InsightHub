\# 🧠 NLP InsightHub



\### Multi-Task Text Intelligence Platform



NLP InsightHub is an interactive Natural Language Processing platform that performs multiple NLP tasks on user-provided text through a modern Streamlit interface.



The system combines traditional NLP preprocessing with modern Transformer-based models to provide meaningful insights from unstructured text.



\---



\## 🚀 Features



\- 🧹 Text Preprocessing

\- 📊 Text Statistics

\- 😊 Sentiment Analysis

\- 🔍 Named Entity Recognition

\- 🏷️ Zero-Shot Text Classification

\- 🔑 Keyword Frequency Analysis

\- ☁️ Word Cloud Generation

\- 📈 Interactive Charts

\- 📥 Downloadable Analysis Report

\- 🎨 Interactive Streamlit Dashboard



\---



\## 🧠 NLP Techniques



\### 1. Text Preprocessing



The system performs:



\- Tokenization

\- Lowercase conversion

\- Stop-word removal

\- Lemmatization

\- URL and special-character removal



\### 2. Sentiment Analysis



A Transformer-based sentiment model analyzes the emotional tone of the input text.



Possible outputs:



\- Positive

\- Neutral

\- Negative



\### 3. Named Entity Recognition



spaCy identifies entities such as:



\- PERSON

\- ORGANIZATION

\- LOCATION

\- DATE

\- MONEY



\### 4. Text Classification



Zero-shot classification categorizes text into:



\- Technology

\- Business

\- Sports

\- Politics

\- Entertainment

\- Education



\### 5. Keyword Analysis



The system identifies frequently occurring meaningful words from the processed text.



\### 6. Word Cloud



Frequently occurring words are visualized using a Word Cloud.



\---



\## 🛠️ Technologies Used



| Technology | Purpose |

|---|---|

| Python | Core Programming |

| NLTK | Text Processing |

| spaCy | Named Entity Recognition |

| Hugging Face Transformers | AI/NLP Models |

| PyTorch | Deep Learning Backend |

| Scikit-learn | Machine Learning Utilities |

| Pandas | Data Processing |

| Matplotlib | Visualization |

| WordCloud | Keyword Visualization |

| Streamlit | Web Interface |



\---



\## 🏗️ System Architecture



```text

&#x20;               User Input

&#x20;                   │

&#x20;                   ▼

&#x20;         ┌───────────────────┐

&#x20;         │  Streamlit UI     │

&#x20;         └─────────┬─────────┘

&#x20;                   │

&#x20;                   ▼

&#x20;         ┌───────────────────┐

&#x20;         │ Text Preprocessing│

&#x20;         └─────────┬─────────┘

&#x20;                   │

&#x20;         ┌─────────┼─────────┐

&#x20;         ▼         ▼         ▼

&#x20;     Sentiment     NER    Classification

&#x20;         │         │         │

&#x20;         └─────────┼─────────┘

&#x20;                   ▼

&#x20;         Keyword \& Statistics

&#x20;                   │

&#x20;                   ▼

&#x20;            Visualization

&#x20;                   │

&#x20;                   ▼

&#x20;             Final Report

