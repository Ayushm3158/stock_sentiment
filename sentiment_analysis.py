import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

def analyze_sentiment(text):
    """
    Perform sentiment analysis on text using VADER.

    Parameters:
        text (str): Input text data.
    
    Returns:
        dict: Sentiment scores (positive, neutral, negative, compound).
    """
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)

if __name__ == "__main__":
    df = pd.read_csv("cleaned_tweets.csv")
    sia = SentimentIntensityAnalyzer()
    df['sentiment'] = df['cleaned_text'].apply(lambda x: sia.polarity_scores(x)['compound'])
    df.to_csv("sentiment_tweets.csv", index=False)
    print("Sentiment analysis results saved to sentiment_tweets.csv")
