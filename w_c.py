from PIL import Image
from wordcloud import WordCloud, STOPWORDS
from pathlib import Path
import numpy as np
import os

# Setting up the base Directory to decide the location where the dataset file will be stored.
BASE_DIR = Path(__file__).resolve().parent

# Function to basically check whether file exist or not.
def check_file(file_name):

    # Getting the location of the file.
    tweets_file = Path(os.path.join(BASE_DIR, file_name))

    # Condition to chaeck whether the file exists or not. 
    if tweets_file.is_file():

        # If file exits then deleting that file.
        os.remove(os.path.join(BASE_DIR, file_name))
        return
    
    else:
        # If the file does not exist do nothing.
        return

def create_wordcloud(tweets, file_name):

	# Create a numpy araay for WordCloud mask image
	mask = np.array(Image.open(os.path.join(BASE_DIR, "cloud.png")))

	# Creating a set of stopwords	
	stopwords = set(STOPWORDS)

	# creating a WordCloud Instance
	wc = WordCloud(background_color="white", max_words=200, mask=mask, stopwords=stopwords)
	
	# Generating a WordCloud
	wc.generate(' '.join(tweets))

	check_file(file_name)

	# Saving the WorldCloud File as a PNG
	wc.to_file(os.path.join(BASE_DIR, file_name))