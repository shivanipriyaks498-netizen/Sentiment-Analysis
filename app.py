
import streamlit as st
import pandas as pd
import nltk
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud

# Download VADER lexicon
nltk.download("vader_lexicon", quiet=True)

st.set_page_config(
    page_title="Sentiment Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sentiment Analysis Dashboard")
st.write("Analyze customer reviews using Python and VADER.")

@st.cache_resource
def load_analyzer():
    return SentimentIntensityAnalyzer()

analyzer = load_analyzer()

def classify_sentiment(review):
    score = analyzer.polarity_scores(str(review))["compound"]

    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    return "Neutral"

# Upload or use the existing dataset
uploaded_file = st.file_uploader(
    "Upload a CSV file containing a Review column",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
elif __import__("os").path.exists("dataset/large_reviews.csv"):
    df = pd.read_csv("dataset/large_reviews.csv")
    st.info("Showing your existing 100-review dataset.")
else:
    st.warning("Please upload a CSV file to begin.")
    st.stop()

if "Review" not in df.columns:
    st.error("Your CSV must contain a column named Review.")
    st.stop()

df = df.dropna(subset=["Review"]).copy()

if df.empty:
    st.warning("No reviews found in the dataset.")
    st.stop()

# Perform sentiment analysis
df["Sentiment"] = df["Review"].apply(classify_sentiment)

# Summary metrics
counts = df["Sentiment"].value_counts()
positive = counts.get("Positive", 0)
negative = counts.get("Negative", 0)
neutral = counts.get("Neutral", 0)

st.subheader("Sentiment Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Reviews", len(df))
col2.metric("Positive 😊", positive)
col3.metric("Negative 😞", negative)
col4.metric("Neutral 😐", neutral)

st.divider()

# Charts
st.subheader("Sentiment Distribution")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    fig, ax = plt.subplots()
    ax.bar(
        ["Positive", "Negative", "Neutral"],
        [positive, negative, neutral]
    )
    ax.set_ylabel("Number of Reviews")
    ax.set_title("Sentiment Bar Chart")
    st.pyplot(fig)
    plt.close(fig)

with chart_col2:
    fig, ax = plt.subplots()
    ax.pie(
        [positive, negative, neutral],
        labels=["Positive", "Negative", "Neutral"],
        autopct="%1.1f%%",
        startangle=90
    )
    ax.set_title("Sentiment Pie Chart")
    st.pyplot(fig)
    plt.close(fig)

st.divider()

# Word cloud
st.subheader("Review Word Cloud")

all_reviews = " ".join(df["Review"].astype(str))

if all_reviews.strip():
    wordcloud = WordCloud(
        width=900,
        height=400,
        background_color="white"
    ).generate(all_reviews)

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
    plt.close(fig)

# Results table
st.subheader("Analyzed Reviews")
st.dataframe(df, use_container_width=True)

# Download results
csv_data = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Sentiment Results",
    data=csv_data,
    file_name="sentiment_results.csv",
    mime="text/csv"
)

st.success("Sentiment analysis completed successfully!")
