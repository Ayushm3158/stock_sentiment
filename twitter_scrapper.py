import tweepy
import pandas as pd

# Twitter API credentials
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_SECRET = "your_access_secret"

def authenticate_twitter():
    """Authenticate to the Twitter API using Tweepy."""
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

def scrape_tweets(keyword, count=100):
    """
    Scrape tweets containing a specific keyword.

    Parameters:
        keyword (str): Keyword or hashtag to search for.
        count (int): Number of tweets to scrape.
    
    Returns:
        pd.DataFrame: DataFrame containing tweet data.
    """
    api = authenticate_twitter()
    tweets_data = []

    for tweet in tweepy.Cursor(api.search_tweets, q=keyword, lang="en", tweet_mode="extended").items(count):
        tweets_data.append({
            "created_at": tweet.created_at,
            "text": tweet.full_text,
            "retweet_count": tweet.retweet_count,
            "favorite_count": tweet.favorite_count,
            "user": tweet.user.screen_name,
        })
    
    return pd.DataFrame(tweets_data)

if __name__ == "__main__":
    keyword = "$AAPL"  # Example: Scraping tweets about Apple stock
    df = scrape_tweets(keyword, count=200)
    df.to_csv("tweets.csv", index=False)
    print("Tweets saved to tweets.csv")
