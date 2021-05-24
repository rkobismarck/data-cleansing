import pandas as pd
import numpy as np

df = pd.read_csv('Datasets/BL-Flickr-Images-Book.csv')

columns_to_drop = ['Edition Statement',
                    'Corporate Author',
                    'Corporate Contributors',
                    'Former owner',  
                    'Engraver', 
                    'Contributors', 
                    'Issuance type','Shelfmarks']

df.drop(columns_to_drop, inplace=True, axis=1)

df['Identifier'].is_unique

df.set_index('Identifier', inplace=True)

print(df.head(20))

#print(df.dtypes.value_counts())

#print(df.loc[1905:, 'Date of Publication'].head(5))

extr = df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
#print(extr.head((20)))

df['Date of Publication'] = pd.to_numeric(extr)
#print(df['Date of Publication'].dtype)


#print(df.head(40).isnull().count())
#print(len(df))
#print(df['Date of Publication'].isnull().sum() / len(df))

print(df)

upper = df['Place of Publication'].str.upper()

df['Place of Publication'] = upper
print(df['Place of Publication'].head(10))


pub = df['Place of Publication']
london = pub.str.contains('LONDON')
print(london[:5])


oxford = pub.str.contains('OXFORD')
print(oxford.head(5))

df['Place of Publication'] = np.where(london, 'LONDON',
                                      np.where(oxford, 'OXFORD',
                                               pub.str.replace('-', ' ')))

print(df['Place of Publication'].head())


def sayHello(x):
    print(x)

df.apply(sayHello)
"""



≈
df = df.set_index('Identifier')

print(df.head(5))

print('-------------------------------------------')
print('-------------------------------------------')

print(df.loc[206]) #accesing by identifier

print('-------------------------------------------')
print('-------------------------------------------')

print(df.iloc[1]) #accesign by position in array

print('-------------------------------------------')
print('-------------------------------------------')

print(df.dtypes.value_counts())

print(df.loc[1905:, 'Date of Publication'].head(10))

extr = df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)

print(extr.head())

df['Date of Publication'] = pd.to_numeric(extr)
print(df['Date of Publication'].dtype)

print(df['Date of Publication'].isnull().sum() / len(df))


print(df.loc[4157862])

print(df.loc[4159587])
"""