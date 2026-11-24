
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# Load sentiment results
df = pd.read_csv("dataset/sentiment_results.csv")

print("========== SENTIMENT VISUALIZATION ==========")

# Calculate sentiment counts
sentiment_counts = df["Sentiment"].value_counts()

print("\nSentiment Counts:")
print(sentiment_counts)

# Chart 1: Bar Chart
plt.figure(figsize=(8, 5))

sentiment_counts.plot(kind="bar", edgecolor="black")

plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=0)

plt.savefig("sentiment_bar_chart.png")
plt.show()

# Chart 2: Pie Chart
plt.figure(figsize=(7, 7))

sentiment_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sentiment Percentage Distribution")
plt.ylabel("")

plt.savefig("sentiment_pie_chart.png")
plt.show()

# Prepare stopwords
stopwords = set(STOPWORDS)

# Chart 3: Positive WordCloud
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
plt.title("Positive Reviews WordCloud")

plt.savefig("positive_wordcloud.png")
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
plt.title("Negative Reviews WordCloud")

plt.savefig("negative_wordcloud.png")
plt.show()

print("\nSentiment Bar Chart saved successfully!")
print("Sentiment Pie Chart saved successfully!")
print("Positive WordCloud saved successfully!")
print("Negative WordCloud saved successfully!")

print("\nAll sentiment visualizations created successfully!")
