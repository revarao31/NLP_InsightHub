import streamlit as st
import pandas as pd
import re
import nltk
import spacy
import matplotlib.pyplot as plt

from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from transformers import pipeline
from wordcloud import WordCloud


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="NLP InsightHub",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    margin-bottom: 25px;
}

.section-title {
    font-size: 25px;
    font-weight: 600;
}

div[data-testid="stMetric"] {
    border: 1px solid #dddddd;
    padding: 15px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# NLTK SETUP
# ============================================================

@st.cache_resource
def setup_nltk():

    packages = [
        "punkt",
        "punkt_tab",
        "stopwords",
        "wordnet"
    ]

    for package in packages:
        try:
            if package in ["punkt", "punkt_tab"]:
                nltk.data.find(
                    f"tokenizers/{package}"
                )
            elif package == "stopwords":
                nltk.data.find(
                    "corpora/stopwords"
                )
            elif package == "wordnet":
                nltk.data.find(
                    "corpora/wordnet"
                )

        except LookupError:
            nltk.download(
                package,
                quiet=True
            )


setup_nltk()


# ============================================================
# NLP TOOLS
# ============================================================

stop_words = set(
    stopwords.words("english")
)

lemmatizer = WordNetLemmatizer()


# ============================================================
# LOAD MODELS
# ============================================================

@st.cache_resource
def load_models():

    sentiment_model = pipeline(
        "sentiment-analysis",
        model="cardiffnlp/twitter-roberta-base-sentiment-latest"
    )

    classification_model = pipeline(
        "zero-shot-classification",
        model="facebook/bart-large-mnli"
    )

    ner_model = spacy.load(
        "en_core_web_sm"
    )

    return (
        sentiment_model,
        classification_model,
        ner_model
    )


with st.spinner(
    "Loading NLP models..."
):

    sentiment_analyzer, classifier, nlp = load_models()


# ============================================================
# PREPROCESSING
# ============================================================

def preprocess_text(text):

    text = text.lower()

    text = re.sub(
        r"http\S+|www\S+",
        "",
        text
    )

    text = re.sub(
        r"[^a-zA-Z\s]",
        "",
        text
    )

    tokens = nltk.word_tokenize(
        text
    )

    tokens = [
        word
        for word in tokens
        if word not in stop_words
    ]

    tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
    ]

    return tokens


# ============================================================
# TEXT STATISTICS
# ============================================================

def calculate_statistics(
    original_text,
    processed_tokens
):

    words = original_text.split()

    sentences = re.findall(
        r"[.!?]+",
        original_text
    )

    sentence_count = len(
        sentences
    )

    if sentence_count == 0:
        sentence_count = 1

    average_word_length = 0

    if processed_tokens:

        average_word_length = round(
            sum(
                len(word)
                for word in processed_tokens
            ) / len(processed_tokens),
            2
        )

    return {
        "Characters": len(
            original_text
        ),
        "Words": len(words),
        "Sentences": sentence_count,
        "Unique Words": len(
            set(processed_tokens)
        ),
        "Average Word Length":
            average_word_length
    }


# ============================================================
# SENTIMENT ANALYSIS
# ============================================================

def analyze_sentiment(text):

    result = sentiment_analyzer(
        text
    )[0]

    mapping = {
        "negative": "NEGATIVE",
        "neutral": "NEUTRAL",
        "positive": "POSITIVE",
        "LABEL_0": "NEGATIVE",
        "LABEL_1": "NEUTRAL",
        "LABEL_2": "POSITIVE"
    }

    label = mapping.get(
        result["label"],
        result["label"].upper()
    )

    return {
        "label": label,
        "score": result["score"]
    }


# ============================================================
# NAMED ENTITY RECOGNITION
# ============================================================

def extract_entities(text):

    doc = nlp(text)

    entities = []

    for entity in doc.ents:

        entities.append({
            "Entity": entity.text,
            "Type": entity.label_,
            "Description":
                spacy.explain(
                    entity.label_
                )
        })

    return pd.DataFrame(
        entities
    )


# ============================================================
# TEXT CLASSIFICATION
# ============================================================

def classify_text(text):

    categories = [
        "Technology",
        "Business",
        "Sports",
        "Politics",
        "Entertainment",
        "Education"
    ]

    result = classifier(
        text,
        candidate_labels=categories
    )

    return result


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">'
    '🧠 NLP InsightHub'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Multi-Task Text Intelligence Platform'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙️ NLP Modules")

    st.write(
        "Available analysis modules"
    )

    st.divider()

    st.success(
        "✓ Text Preprocessing"
    )

    st.success(
        "✓ Sentiment Analysis"
    )

    st.success(
        "✓ Named Entity Recognition"
    )

    st.success(
        "✓ Text Classification"
    )

    st.success(
        "✓ Keyword Analysis"
    )

    st.success(
        "✓ Word Cloud"
    )

    st.divider()

    st.info(
        "Powered by Transformers + spaCy"
    )

    st.caption(
        "NLP InsightHub v1.0"
    )


# ============================================================
# TEXT INPUT
# ============================================================

st.subheader(
    "📝 Text Analysis"
)

user_text = st.text_area(
    "Enter text for analysis",
    height=220,
    placeholder="Type or paste your text here..."
)


# ============================================================
# ANALYZE BUTTON
# ============================================================

analyze = st.button(
    "🚀 Analyze Text",
    type="primary",
    use_container_width=True
)


# ============================================================
# ANALYSIS
# ============================================================

if analyze:

    if not user_text.strip():

        st.warning(
            "Please enter some text first."
        )

    else:

        with st.spinner(
            "Running NLP analysis..."
        ):

            # --------------------------------------------
            # PREPROCESSING
            # --------------------------------------------

            processed_tokens = (
                preprocess_text(
                    user_text
                )
            )

            # --------------------------------------------
            # STATISTICS
            # --------------------------------------------

            statistics = (
                calculate_statistics(
                    user_text,
                    processed_tokens
                )
            )

            # --------------------------------------------
            # SENTIMENT
            # --------------------------------------------

            sentiment = (
                analyze_sentiment(
                    user_text
                )
            )

            # --------------------------------------------
            # NER
            # --------------------------------------------

            entities = (
                extract_entities(
                    user_text
                )
            )

            # --------------------------------------------
            # CLASSIFICATION
            # --------------------------------------------

            classification = (
                classify_text(
                    user_text
                )
            )

            # --------------------------------------------
            # KEYWORDS
            # --------------------------------------------

            frequency = Counter(
                processed_tokens
            )

            top_words = (
                frequency
                .most_common(10)
            )

        st.success(
            "Analysis completed successfully!"
        )


        # ====================================================
        # OVERVIEW
        # ====================================================

        st.markdown(
            '<div class="section-title">'
            '📊 Overview'
            '</div>',
            unsafe_allow_html=True
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Total Words",
                statistics["Words"]
            )

        with col2:

            st.metric(
                "Unique Words",
                statistics["Unique Words"]
            )

        with col3:

            st.metric(
                "Sentences",
                statistics["Sentences"]
            )

        with col4:

            st.metric(
                "Characters",
                statistics["Characters"]
            )


        # ====================================================
        # TABS
        # ====================================================

        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📊 Overview",
            "😊 Sentiment",
            "🔍 NER",
            "🏷️ Classification",
            "🔑 Keywords"
        ])


        # ====================================================
        # TAB 1 — OVERVIEW
        # ====================================================

        with tab1:

            st.subheader(
                "📋 Detailed Statistics"
            )

            statistics_df = pd.DataFrame(
                {
                    "Metric":
                        list(statistics.keys()),
                    "Value":
                        list(statistics.values())
                }
            )

            st.dataframe(
                statistics_df,
                use_container_width=True,
                hide_index=True
            )

            st.subheader(
                "🧹 Preprocessed Text"
            )

            st.code(
                " ".join(
                    processed_tokens
                )
            )


        # ====================================================
        # TAB 2 — SENTIMENT
        # ====================================================

        with tab2:

            st.subheader(
                "😊 Sentiment Analysis"
            )

            sentiment_label = (
                sentiment["label"]
            )

            sentiment_score = (
                sentiment["score"]
            )

            if sentiment_label == "POSITIVE":

                st.success(
                    "😊 POSITIVE"
                )

            elif sentiment_label == "NEGATIVE":

                st.error(
                    "😞 NEGATIVE"
                )

            else:

                st.info(
                    "😐 NEUTRAL"
                )

            st.write(
                f"Confidence: "
                f"{sentiment_score * 100:.2f}%"
            )

            st.progress(
                float(sentiment_score)
            )


        # ====================================================
        # TAB 3 — NER
        # ====================================================

        with tab3:

            st.subheader(
                "🔍 Named Entity Recognition"
            )

            if not entities.empty:

                st.dataframe(
                    entities,
                    use_container_width=True,
                    hide_index=True
                )

            else:

                st.info(
                    "No named entities detected."
                )


        # ====================================================
        # TAB 4 — CLASSIFICATION
        # ====================================================

        with tab4:

            st.subheader(
                "🏷️ Text Classification"
            )

            classification_df = pd.DataFrame(
                {
                    "Category":
                        classification["labels"],
                    "Confidence":
                        classification["scores"]
                }
            )

            classification_df[
                "Confidence (%)"
            ] = (
                classification_df[
                    "Confidence"
                ] * 100
            )

            top_category = (
                classification["labels"][0]
            )

            top_score = (
                classification["scores"][0]
            )

            st.success(
                f"Top Category: {top_category}"
            )

            st.write(
                f"Confidence: "
                f"{top_score * 100:.2f}%"
            )

            st.bar_chart(
                classification_df.set_index(
                    "Category"
                )["Confidence (%)"]
            )


        # ====================================================
        # TAB 5 — KEYWORDS
        # ====================================================

        with tab5:

            st.subheader(
                "🔑 Keyword Analysis"
            )

            if top_words:

                keyword_df = pd.DataFrame(
                    top_words,
                    columns=[
                        "Keyword",
                        "Frequency"
                    ]
                )

                st.dataframe(
                    keyword_df,
                    use_container_width=True,
                    hide_index=True
                )

                st.subheader(
                    "📈 Keyword Frequency"
                )

                st.bar_chart(
                    keyword_df.set_index(
                        "Keyword"
                    )
                )

            else:

                st.info(
                    "No keywords found."
                )


        # ====================================================
        # WORD CLOUD
        # ====================================================

        st.divider()

        st.subheader(
            "☁️ Word Cloud"
        )

        if processed_tokens:

            cloud_text = " ".join(
                processed_tokens
            )

            wordcloud = WordCloud(
                width=1200,
                height=500,
                background_color="white"
            ).generate(
                cloud_text
            )

            fig, ax = plt.subplots(
                figsize=(12, 5)
            )

            ax.imshow(
                wordcloud,
                interpolation="bilinear"
            )

            ax.axis("off")

            st.pyplot(
                fig,
                use_container_width=True
            )


        # ====================================================
        # DOWNLOAD REPORT
        # ====================================================

        st.divider()

        st.subheader(
            "📥 Export Analysis"
        )

        report = f"""
NLP INSIGHTHUB
Multi-Task Text Intelligence Report
====================================

TEXT STATISTICS
---------------
Characters: {statistics["Characters"]}
Words: {statistics["Words"]}
Sentences: {statistics["Sentences"]}
Unique Words: {statistics["Unique Words"]}
Average Word Length: {statistics["Average Word Length"]}

SENTIMENT
---------
Label: {sentiment_label}
Confidence: {sentiment_score * 100:.2f}%

CLASSIFICATION
--------------
Category: {top_category}
Confidence: {top_score * 100:.2f}%

TOP KEYWORDS
------------
"""

        for word, count in top_words:

            report += (
                f"{word}: {count}\n"
            )

        report += "\nNAMED ENTITIES\n--------------\n"

        if not entities.empty:

            for _, row in entities.iterrows():

                report += (
                    f"{row['Entity']} - "
                    f"{row['Type']}\n"
                )

        else:

            report += (
                "No named entities detected.\n"
            )


        st.download_button(
            label="📥 Download Analysis Report",
            data=report,
            file_name="nlp_analysis_report.txt",
            mime="text/plain",
            use_container_width=True
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "NLP InsightHub | "
    "Multi-Task NLP Analysis Platform | "
    "Python • Transformers • spaCy • Streamlit"
)