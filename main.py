import twitter
import re
from textblob import TextBlob
import pandas as pd
import os
from pathlib import Path
import numpy as np
import figures
import w_c


# Setting up the base Directory to decide the location where the dataset file will be stored.
BASE_DIR = Path(__file__).resolve().parent

# Initializing three empty strings.
positive_tweets = []
negative_tweets = []
neutral_tweets = []

# A basic function used to clean the tweet text using python regex.
def clean_tweet(tweet):
    '''
    Utility method to clean the tweet body by removing the links, special characters
    using python regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def analyze_sentiment(tweet):
    '''
    Utility method to carry out classification sentiment of the passed tweet
    using textblob's sentiment method.
    '''
    analysis = TextBlob(clean_tweet(tweet))
    
    if analysis.sentiment.polarity > 0:
        
        # Adding tweet to the postive_tweets list 
        positive_tweets.append(clean_tweet(tweet))
        return 'Positive'

    elif analysis.sentiment.polarity == 0:
        
        # Adding tweet to the neutral_tweets list
        neutral_tweets.append(clean_tweet(tweet))
        return 'Neutral'

    else:

        # Adding tweet to the negative_tweets list
        negative_tweets.append(clean_tweet(tweet))
        return 'Negative'

# Main Function
def main():

    # Calling the get_tweets function from the twitter.py file.
    twitter.get_tweets()

    # Reading the data from the csv file as a pandas dataframe
    dataframe = pd.read_csv(os.path.join(BASE_DIR, 'tweets.csv'))

    # Storing index of the data entries where language is not equal to English.
    index_names = dataframe[ dataframe['language'] != 'en' ].index
   
    # Dropping those data entries.
    dataframe.drop(index_names, inplace = True)

    # Creating a column named 'sentiment' in the dataframe and assigning each data entry its sentiment classification
    # by calling the 'analyze_sentiment' function and passing the tweet as a parameter to that function. 
    dataframe['sentiment'] = np.array([analyze_sentiment(tweet) for tweet in dataframe['tweet']])

    # Saving the update dataframe in the base directory.
    dataframe.to_csv(os.path.join(BASE_DIR, 'tweets.csv'))

    # Displaying the total no tweets after the data cleaning has happened.
    print(f'Total number of tweets after cleaning data: {len(dataframe)}')

    # Counting the number of Positive tweets.
    # Displaying no of Positive tweets as a console output.
    Positive = dataframe.id[dataframe['sentiment'] == 'Positive'].count()
    print(f'Total number of Positive tweets: {Positive}')

    # Counting the number of Neutral tweets.
    # Displaying no of Neutral tweets as a console output.
    Neutral = dataframe.id[dataframe['sentiment'] == 'Neutral'].count()
    print(f'Total number of Neutral tweets: {Neutral}')

    # Counting the number of Negative tweets.
    # Displaying no of Negative tweets as a console output.
    Negative = dataframe.id[dataframe['sentiment'] == 'Negative'].count()
    print(f'Total number of Negative tweets: {Negative}')

    # Drawing a Pie-Chart to visualize the results.
    figures.draw_figure()

if __name__ == '__main__':
    
    # Running the main function
    main()

    # Creating a WordCloud for the list of Positive Tweets.
    file_name = f'{positive_tweets=}'.split('=')[0] + '.png'
    w_c.create_wordcloud(positive_tweets, file_name)

    # Creating a WordCloud for the list of Neutral Tweets.
    file_name = f'{neutral_tweets=}'.split('=')[0] + '.png'
    w_c.create_wordcloud(neutral_tweets, file_name)

    # Creating a WordCloud for the list of Negative Tweets.
    file_name = f'{negative_tweets=}'.split('=')[0] + '.png'
    w_c.create_wordcloud(negative_tweets, file_name)

