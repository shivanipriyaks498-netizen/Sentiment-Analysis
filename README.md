
# Sentiment Analysis Using Python

## Project Overview

Sentiment Analysis is a Data Analytics project that analyzes textual reviews and classifies opinions into three categories: Positive, Negative, and Neutral.

The project uses Python libraries and Natural Language Processing (NLP) techniques to understand customer opinions and visualize sentiment patterns.

## Objectives

- Analyze customer reviews and opinions.
- Clean and preprocess textual data.
- Classify reviews into positive, negative, and neutral sentiments.
- Calculate sentiment percentages.
- Visualize sentiment distribution.
- Generate WordClouds to identify frequently used words.
- Extract meaningful analytical insights.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- NLTK
- WordCloud

## Project Workflow

1. Dataset Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Text Analysis
5. Sentiment Classification using VADER
6. Data Visualization
7. Final Insights and Reporting

## Dataset

The project uses a manually prepared dataset containing 100 sample reviews.

The dataset is classified automatically using NLTK VADER.

## Sentiment Analysis Results

| Sentiment | Predicted Reviews | Percentage |
|---|---:|---:|
| Positive | 36 | 36% |
| Neutral | 33 | 33% |
| Negative | 31 | 31% |

## Visualizations

- Review Length Distribution
- Word Frequency Chart
- Review Statistics Chart
- Sentiment Distribution Bar Chart
- Sentiment Distribution Pie Chart
- Positive Sentiment WordCloud
- Negative Sentiment WordCloud

## Project Structure

```text
Sentiment Analysis/
├── dataset/
├── sentiment_analysis.py
├── analyze_data.py
├── visualize_data.py
├── classify_sentiment.py
├── visualize_sentiments.py
├── final_analysis.py
├── generate_dataset.py
├── analyze_large_dataset.py
├── visualize_large_dataset.py
├── requirements.txt
└── README.md
```

## How to Run

1. Clone the repository.
2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Run the dataset generation script:

```bash
python generate_dataset.py
```

4. Run sentiment classification:

```bash
python analyze_large_dataset.py
```

5. Generate visualizations:

```bash
python visualize_large_dataset.py
```

## Conclusion

This project demonstrates how Data Analytics and Natural Language Processing can be used to understand opinions from textual data.

The analysis provides insights into positive, negative, and neutral opinions through sentiment classification, statistical analysis, and visualizations.

## Limitations

- The sample dataset is relatively small and manually prepared.
- VADER uses a rule-based approach.
- Automated predictions may not correctly interpret sarcasm, context, or complex expressions.
- Results should not be treated as verified customer satisfaction measurements.

## Author

Developed as a Python Data Analytics project.

# Sentiment-Analysis
A Sentiment Analysis web application built using React.js, JavaScript, HTML, and CSS. It analyzes user-input text and classifies opinions into Positive, Negative, and Neutral categories. Features include keyword-based sentiment detection, negation handling, sentiment statistics, strength percentage, sample sentences, and clear functionality
>>>>>>> 1e79bf3da49950a93f60b4b23101c41d9f767562
