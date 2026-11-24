
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download("vader_lexicon")

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_reviews.csv")

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to classify sentiment
def analyze_sentiment(review):

    score = sia.polarity_scores(str(review))

    compound = score["compound"]

    if compound >= 0.05:
        return "Positive"

    elif compound <= -0.05:
        return "Negative"

    else:
        return "Neutral"


# Apply sentiment analysis
df["Sentiment"] = df["Review"].apply(analyze_sentiment)

# Display results
print("\n========== SENTIMENT CLASSIFICATION ==========")

print(df)

# Count sentiment categories
print("\nSentiment Distribution:")
print(df["Sentiment"].value_counts())

# Save results
df.to_csv("dataset/sentiment_results.csv", index=False)

print("\nSentiment classification completed successfully!")
print("Results saved to dataset/sentiment_results.csv")
