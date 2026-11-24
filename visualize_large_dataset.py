
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# Load large sentiment results
df = pd.read_csv("dataset/large_sentiment_results.csv")

print("========== LARGE DATASET VISUALIZATION ==========")

# Calculate sentiment counts
sentiment_counts = (
    df["Sentiment"].value_counts()
    .reindex(["Positive", "Negative", "Neutral"], fill_value=0)
)

# Chart 1: Sentiment Bar Chart
plt.figure(figsize=(8, 5))

sentiment_counts.plot(kind="bar", edgecolor="black")

plt.title("Sentiment Distribution - 100 Reviews")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("large_sentiment_bar.png")
plt.show()

# Chart 2: Sentiment Pie Chart
plt.figure(figsize=(7, 7))

sentiment_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sentiment Percentage Distribution")
plt.ylabel("")

plt.tight_layout()
plt.savefig("large_sentiment_pie.png")
plt.show()

# Chart 3: Positive WordCloud
stopwords = set(STOPWORDS)

positive_text = " ".join(
    df[df["Sentiment"] == "Positive"]["Review"].astype(str)
)

positive_cloud = WordCloud(
    width=1000,
    height=500,
    background_color="white",
    stopwords=stopwords
).generate(positive_text)

plt.figure(figsize=(10, 5))
plt.imshow(positive_cloud, interpolation="bilinear")
plt.axis("off")
plt.title("Positive Sentiment WordCloud")

plt.savefig("large_positive_wordcloud.png")
plt.show()

# Chart 4: Negative WordCloud
negative_text = " ".join(
    df[df["Sentiment"] == "Negative"]["Review"].astype(str)
)

negative_cloud = WordCloud(
    width=1000,
    height=500,
    background_color="white",
    stopwords=stopwords
).generate(negative_text)

plt.figure(figsize=(10, 5))
plt.imshow(negative_cloud, interpolation="bilinear")
plt.axis("off")
plt.title("Negative Sentiment WordCloud")

plt.savefig("large_negative_wordcloud.png")
plt.show()

print("\nLarge sentiment bar chart saved!")
print("Large sentiment pie chart saved!")
print("Positive WordCloud saved!")
print("Negative WordCloud saved!")

print("\nAll large dataset visualizations created successfully!")
