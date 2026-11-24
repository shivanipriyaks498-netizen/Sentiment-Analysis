
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_reviews.csv")

print("========== SENTIMENT DATA ANALYSIS ==========")

# Total reviews
total_reviews = len(df)
print("\nTotal Reviews:", total_reviews)

# Calculate review length
df["Review_Length"] = df["Review"].astype(str).apply(len)

# Average review length
average_length = df["Review_Length"].mean()
print("Average Review Length:", round(average_length, 2))

# Longest review
longest_review = df.loc[df["Review_Length"].idxmax(), "Review"]
print("\nLongest Review:")
print(longest_review)

# Shortest review
shortest_review = df.loc[df["Review_Length"].idxmin(), "Review"]
print("\nShortest Review:")
print(shortest_review)

# Word count
df["Word_Count"] = df["Review"].astype(str).apply(
    lambda x: len(x.split())
)

print("\nAverage Words Per Review:",
      round(df["Word_Count"].mean(), 2))

# Most frequent words
all_words = " ".join(df["Review"]).lower().split()

word_frequency = pd.Series(all_words).value_counts()

print("\nTop 10 Most Frequent Words:")
print(word_frequency.head(10))

# Save analysis dataset
df.to_csv("dataset/analyzed_reviews.csv", index=False)

print("\nAnalysis completed successfully!")
