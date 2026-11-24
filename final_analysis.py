
import pandas as pd

# Load sentiment results
df = pd.read_csv("dataset/sentiment_results.csv")

print("\n========== FINAL SENTIMENT ANALYSIS REPORT ==========")

# Total reviews
total_reviews = len(df)

# Sentiment counts
sentiment_counts = (
    df["Sentiment"]
    .value_counts()
    .reindex(["Positive", "Negative", "Neutral"], fill_value=0)
)

print("\nTotal Reviews Analyzed:", total_reviews)

# Calculate percentages
print("\nSENTIMENT PERCENTAGES:")

for sentiment, count in sentiment_counts.items():
    percentage = (count / total_reviews) * 100

    print(
        f"{sentiment}: {count} reviews "
        f"({percentage:.2f}%)"
    )

# Identify most common sentiment
most_common = sentiment_counts.idxmax()

print("\nMost Common Sentiment:", most_common)

# Overall analysis
positive = sentiment_counts["Positive"]
negative = sentiment_counts["Negative"]
neutral = sentiment_counts["Neutral"]

print("\n========== DATA ANALYTICS INSIGHTS ==========")

if positive > negative:
    print("Overall opinion is more positive.")

elif negative > positive:
    print("Overall opinion is more negative.")

else:
    print("Positive and negative opinions are equally distributed.")

print("Positive Reviews:", positive)
print("Negative Reviews:", negative)
print("Neutral Reviews:", neutral)

# Generate final report
report = f"""
SENTIMENT ANALYSIS - FINAL REPORT

Total Reviews Analyzed: {total_reviews}

Positive Reviews: {positive}
Negative Reviews: {negative}
Neutral Reviews: {neutral}

Positive Percentage: {positive / total_reviews * 100:.2f}%
Negative Percentage: {negative / total_reviews * 100:.2f}%
Neutral Percentage: {neutral / total_reviews * 100:.2f}%

Most Common Sentiment: {most_common}

CONCLUSION:
The dataset contains positive, negative and neutral opinions.
Sentiment analysis helps understand customer opinions
and identify overall satisfaction patterns.

Note: Results are automated predictions using VADER.
They may not perfectly capture context or sarcasm.
"""

# Save report
with open("final_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("\nFinal report saved successfully!")
print("Final analysis completed successfully!")
