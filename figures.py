import pandas as pd
import numpy as np
import plotly.graph_objs as go
from warnings import filterwarnings
filterwarnings('ignore')
import os
from pathlib import Path
import plotly.io as pio

pio.renderers.default = "browser"

# Setting up the base Directory to decide the location where the dataset file will be stored.
BASE_DIR = Path(__file__).resolve().parent

def draw_figure():

    # Reading the Dataset 'tweets.csv'
    dataset = pd.read_csv(os.path.join(BASE_DIR, 'tweets.csv'))
    
    # Counting the number of Positive, Neutral and Negative sentiments.
    pd_series = dataset.sentiment.value_counts()

    index_1 = ['Positive', 'Neutral', 'Negative']
    pd_series.index = index_1
    
    # Making a Pie Chart
    labels = (np.array(pd_series.index))
    values = (np.array((pd_series / pd_series.sum())*100))
    colors = ['green', 'yellow', 'red']
    fig_pc = go.Figure(data=[go.Pie(labels=labels,values=values,hole=.3)])
    fig_pc.update_traces(hoverinfo='label+percent', textinfo='label+percent', textfont_size=20, marker=dict(colors=colors, line=dict(color='#000000', width=3)))
    fig_pc.update_layout(title="Sentiment Analysis", titlefont={'size': 30},)
    fig_pc.write_html(os.path.join(BASE_DIR, 'Sentiment Analysis.html'), auto_open=True)

if __name__ == '__main__':
    draw_figure()

