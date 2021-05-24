import pandas as pd
from textblob import TextBlob
import text2emotion as te

def read_csv(path):
    return pd.read_csv(path)


def calculate_polarity(text):
    return  TextBlob(text).sentiment[0]

def calculate_subjetity(text):
    return  TextBlob(text).sentiment[1]


def extract_emotion(text):
    return te.get_emotion(text)

columns_to_drop = ['created_at',
                    'response_tweet_id',
                    'in_response_to_tweet_id',
                    ]

# Reading
df = read_csv('Datasets/sample.csv')

# Drop unwanted columns
df.drop(columns_to_drop,inplace=True, axis=1)

# Verify for a valid id
df['tweet_id'].is_unique

# Set this new column like a valid ID
df.set_index('tweet_id', inplace=True)

# Normalization of text column for content
clean_text = df['text'].str.replace('(@\S+)','')

# Re-apply the elements with clean data
df['text'] = clean_text

# Filter by 

#print(df['author_id'].unique())

#print(extract.head())
#print(df.head(5))




df['Polarity'] = df['text'].apply(calculate_polarity)

df['Subjetivity'] = df['text'].apply(calculate_subjetity)

df['Emotion'] = df['text'].apply(extract_emotion)

print(df['Polarity'].describe())

df = df.loc[df['Polarity'] < 0]

print(df.head())
print(df.loc[119253]['Emotion'])



def pipe(first, *args):
  for fn in args:
    first = fn(first)
  return first