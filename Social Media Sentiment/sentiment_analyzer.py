def analyze_sentiment(text):
    """
    Analyze sentiment using simple keywords.
    """
    text = text.lower()
    positive_words = ["happy", "great", "love", "good", "fantastic"]
    negative_words = ["sad", "bad", "hate", "terrible", "angry"]

    if any(word in text for word in positive_words):
        return "Positive 😊"
    elif any(word in text for word in negative_words):
        return "Negative 😢"
    else:
        return "Neutral 😐"


def run_sentiment_analyzer():
    print("=== Social Media Sentiment Analyzer ===")
    while True:
        text = input("Enter text (or 'exit' to quit): ")
        if text.lower() == "exit":
            print("👋 Goodbye!")
            break
        sentiment = analyze_sentiment(text)
        print(f"Sentiment: {sentiment}")


if __name__ == "__main__":
    run_sentiment_analyzer()
