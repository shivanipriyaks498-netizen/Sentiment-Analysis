
import pandas as pd
import matplotlib.pyplot as plt

# Load analyzed dataset
df = pd.read_csv("dataset/analyzed_reviews.csv")

# Chart 1: Review Length Distribution
plt.figure(figsize=(8, 5))

plt.hist(df["Review_Length"], bins=8, edgecolor="black")

plt.title("Review Length Distribution")
plt.xlabel("Review Length (Characters)")
plt.ylabel("Number of Reviews")

plt.savefig("review_length.png")
plt.show()


# Chart 2: Top 10 Word Frequency
all_words = " ".join(df["Review"]).lower().split()

word_frequency = pd.Series(all_words).value_counts()

top_words = word_frequency.head(10)

plt.figure(figsize=(9, 5))

top_words.sort_values().plot(kind="barh")

plt.title("Top 10 Most Frequent Words")
plt.xlabel("Frequency")
plt.ylabel("Words")

plt.savefig("word_frequency.png")
plt.show()


# Chart 3: Review Statistics
average_length = df["Review_Length"].mean()
shortest_length = df["Review_Length"].min()
longest_length = df["Review_Length"].max()

statistics = pd.Series({
    "Average": average_length,
    "Shortest": shortest_length,
    "Longest": longest_length
})

plt.figure(figsize=(8, 5))

statistics.plot(kind="bar", edgecolor="black")

plt.title("Review Length Statistics")
plt.xlabel("Statistics")
plt.ylabel("Characters")

plt.savefig("review_statistics.png")
plt.show()

print("Review Length Chart saved successfully!")
print("Word Frequency Chart saved successfully!")
print("Review Statistics Chart saved successfully!")

print("\nAll 3 charts created successfully!")
