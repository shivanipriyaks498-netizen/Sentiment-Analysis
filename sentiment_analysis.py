
import pandas as pd

# Load dataset
df = pd.read_csv("dataset/reviews.csv")

# Display first five reviews
print("\n========== SENTIMENT ANALYSIS ==========")
print("\nFirst 5 Reviews:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Total number of reviews
print("\nTotal Reviews:", len(df))

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

# Remove duplicate reviews
df = df.drop_duplicates()

# Reset index
df = df.reset_index(drop=True)

# Display cleaned dataset
print("\nCleaned Dataset:")
print(df)

# Save cleaned dataset
df.to_csv("dataset/cleaned_reviews.csv", index=False)

print("\nCleaned dataset saved successfully!")
