
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download("vader_lexicon", quiet=True)

# Load large dataset
df = pd.read_csv("dataset/large_reviews.csv")

# Initialize analyzer
sia = SentimentIntensityAnalyzer()

# Sentiment classification function
def classify_sentiment(review):
    score = sia.polarity_scores(str(review))
    compound = score["compound"]

    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["Sentiment"] = df["Review"].apply(classify_sentiment)

# Display results
print("\n========== LARGE DATASET SENTIMENT ANALYSIS ==========")

print("\nTotal Reviews:", len(df))

print("\nFirst 10 Classified Reviews:")
print(df.head(10).to_string(index=False))

# Sentiment distribution
print("\nSentiment Distribution:")
print(df["Sentiment"].value_counts())

# Calculate percentages
print("\nSentiment Percentages:")

for sentiment, count in df["Sentiment"].value_counts().items():
    percentage = count / len(df) * 100
    print(f"{sentiment}: {percentage:.2f}%")

# Save results
df.to_csv("dataset/large_sentiment_results.csv", index=False)

print("\nLarge dataset analysis completed successfully!")
print("Results saved to dataset/large_sentiment_results.csv")
