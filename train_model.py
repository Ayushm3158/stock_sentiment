import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_model():
    """
    Train a machine learning model to predict stock movements based on sentiment.
    """
    df = pd.read_csv("sentiment_tweets.csv")
    df['target'] = (df['sentiment'] > 0).astype(int)  # Binary target: 1 for positive sentiment, 0 otherwise

    X = df['sentiment'].values.reshape(-1, 1)
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

if __name__ == "__main__":
    train_model()