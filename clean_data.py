import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')
nltk.download('stopwords')

def clean_text(text):
    """
    Clean the tweet text by removing noise.

    Parameters:
        text (str): Raw text data.
    
    Returns:
        str: Cleaned text.
    """
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"@\w+", "", text)  # Remove mentions
    text = re.sub(r"#", "", text)  # Remove hashtags
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    text = text.lower()  # Convert to lowercase
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return " ".join(tokens)

if __name__ == "__main__":
    df = pd.read_csv("tweets.csv")
    df['cleaned_text'] = df['text'].apply(clean_text)
    df.to_csv("cleaned_tweets.csv", index=False)
    print("Cleaned data saved to cleaned_tweets.csv")
