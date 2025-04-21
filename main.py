from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str):
    """
    This function processes a JSON file containing reviews, generates sentiment predictions for each review,
    and visualizes the sentiment distribution in a bar chart.
    
    Args:
    filepath (str): The path to the JSON file containing the reviews.
    
    Returns:
    list: A list of sentiment labels for each review in the file.
    """
    # open the json file using file i/o
    with open (filepath, "r", encoding="utf=8") as file:
        data = json.load(file)

    # extract the reviews from the json file
    reviews = data["results"]

    # get a list of sentiments for each line using get_sentiment
    sentiments = get_sentiment(reviews)

    # plot a visualization expressing sentiment ratio
    make_plot(sentiments)

    # return sentiments
    return sentiments

if __name__ == "__main__":
    print(run("data/raw/reviews.json"))


