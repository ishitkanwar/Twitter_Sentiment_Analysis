import twint
import os
from pathlib import Path

# Setting up the base Directory to decide the location where the dataset file will be stored.
BASE_DIR = Path(__file__).resolve().parent

# Function to basically check whether file 'tweets.csv' exist or not.
def check_file():

    # Gettin g the location of the file 'tweets.csv'.
    tweets_file = Path(os.path.join(BASE_DIR, 'tweets.csv'))

    # Condition to chaeck whether the file exists or not. 
    if tweets_file.is_file():

        # If file exits then deleting that file.
        os.remove(os.path.join(BASE_DIR, 'tweets.csv'))
        return
    
    else:
        # If the file 'tweets.csv' does not exist do nothing.
        return

# Funtion to gather the tweets from the internet.
def scrape_tweets():

    # Setting Up the tweet Scrapper.
    c = twint.Config()

    # Asking the user it's choice. 
    choice_1 = int(input('Which operation do you want to perform\n1. Scrape tweets containing a particular search query.\n2. Scrape tweets from a particular user.\n'))
    
    c.Lang = 'en'
    
    if choice_1 == 1:
        
        sq = input('Please Enter the search query:\nIn case you want to search a hashtag just add an # in the front eg: "#covid".\n')
        print(f'Your search query is {sq}')
        c.Search = sq

    elif choice_1 == 2:
        
        username = input('Please Enter the username:\n')
        c.Username = username

    else:
        
        print('Wrong Choice')
        exit()

    # Asking the number of tweets to be scraped from twitter by the user.
    limit = int(input('Please specify the number of tweets to be analyzed in multiples of 100, ranging from 100 - 3200:\n'))
    
    # Defining the limit.
    c.Limit = limit
    
    # Storing the results of the tweet scrapping in a .csv file ('tweets.csv').
    c.Store_csv = True
    
    # Defining the location of the tweets.csv file.
    c.Output = os.path.join(BASE_DIR, 'tweets.csv')
    
    # Running the twint scraping program.
    twint.run.Search(c)

# Main Function
def get_tweets():
    check_file()
    scrape_tweets()

if __name__ == '__main__':
    get_tweets()