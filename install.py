import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def perform_sentiment_analysis(text):
    # Download the VADER lexicon for sentiment analysis
    nltk.download("vader_lexicon")
    
    # Initialize the sentiment analyzer
    sia = SentimentIntensityAnalyzer()
    
    # Perform sentiment analysis on the input text
    sentiment_score = sia.polarity_scores(text)["compound"]
    
    return sentiment_score

if __name__ == "__main__":
    input_text = input("Enter the text for sentiment analysis: ")
    sentiment_score = perform_sentiment_analysis(input_text)
    
    if sentiment_score >= 0.05:
        sentiment_label = "positive"
    elif sentiment_score <= -0.05:
        sentiment_label = "negative"
    else:
        sentiment_label = "neutral"
    
    print(f"Sentiment Score: {sentiment_score}")
    print(f"Sentiment Label: {sentiment_label}")
