from openai import OpenAI


def get_sentiment(text: list) -> list:
    """
    Uses OpenAI API to classify sentiment of a list of reviews as 
    'positive', 'negative', 'neutral', or 'irrelevant'.
    """

    if not text or not isinstance(text, list) or not all(isinstance(i, str) for i in text):
        return "Wrong input. text must be an array of strings."

    system_prompt = """
    You are a helpful assistant that interprets human sentiment in textual reviews for Zico coconut water.
    Your task is to classify each review as either "positive", "negative", "irrelevant", or "neutral"
    based solely on the text. Respond with one word per review. There are a total of 50 reviews.
    """

    prompt = f"""
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.
    Use only a one-word response per line. Do not include any numbers.

    {text}
    """

    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            { "role": "assistant", "content": system_prompt },
            { "role": "user", "content": prompt }
        ]
    )

    modified_list = response.choices[0].message.content.split("\n")
    striplist = []

    for sentiment in modified_list:
        sentiment = sentiment.strip()
        striplist.append(sentiment)

    return striplist

    
