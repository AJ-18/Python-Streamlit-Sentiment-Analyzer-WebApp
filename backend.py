from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

day = 21
entries = 0
pos_list = []
neg_list = []
results_list= []
dates = []

def diary_sentiment(day, entries):
    while day < 28:
        with open(f"diary/2023-10-{day}.txt", "r", encoding="utf-8") as file:
            diary = file.read()

            # Actual sentiment analysis
            sentiment = analyzer.polarity_scores(diary)
            results_list.append(sentiment)

            # Store the dates
            dates.append(f"Oct {day}")
            day = day + 1

    while entries < len(results_list):
        pos_list.append(results_list[entries]["pos"])
        entries = entries + 1

    # Reset the count to 0 so that we can iterate and append the negativity list as well
    entries = 0

    while entries < len(results_list):
        neg_list.append(results_list[entries]["neg"])
        entries = entries + 1

    return results_list, pos_list, neg_list, dates



if __name__=="__main__":
    diary_sentiment(day, entries)
    print(results_list)
    print(len(results_list))
    print(pos_list)
    print(neg_list)
    print(dates)