import matplotlib.pyplot as plt

def make_plot(sentiments: list) -> list:
    """
    Creates a bar chart representing the sentiment distribution.
    
    Args:
    sentiments (list): A list of sentiment labels (positive, negative, neutral, irrelevant).
    
    Saves a bar chart showing the count of each sentiment in the "images" directory.
    """
    sentiments = [s.strip().lower() for s in sentiments]

    sentiment_types = ("positive", "neutral", "negative", "irrelevant")

    y_values = [sentiments.count(s) for s in sentiment_types]

    fig, ax = plt.subplots()
    ax.bar(sentiment_types, y_values)
    ax.set_title("Review Sentiments")
    ax.set_xlabel("Sentiments")
    ax.set_ylabel("Count")
    fig.savefig("images/bargraph.png")

sentiments = ["positive", "neutral", "negative", "positive", "irrelevant", "positive"]
# Test the function with example data
make_plot(sentiments)