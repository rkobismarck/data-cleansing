import pandas as pd
import statistics
from textblob import TextBlob


def totalizer(row):
    return row[0:len(row)-1].sum()

def dev_std(row):
    return round(statistics.stdev(row),2)

def calculate_polarity(string):
    return TextBlob(string).sentiment[0]


df = pd.DataFrame({ 'A': [1,2,3,4], 
                   'B': [10,20,30,40],
                   'C': [20,40,60,80],
                   'Content': ['Love this', 'I really hate this way of doing things!', 'Not sure about this','Love']
                  }, 
                  index=['Row 1', 'Row 2', 'Row 3', 'Row 4'])



df['Sigma'] = df.apply(totalizer,axis=1)
#df['StDev'] = df.apply(dev_std, axis=1)
df['Polarity'] = df['Content'].apply(calculate_polarity)
print(df.head())
