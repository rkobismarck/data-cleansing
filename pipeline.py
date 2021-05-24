import pandas as pd

df = pd.DataFrame({ 'A': [1,2,3,4], 
                   'B': [10,20,30,40],
                   'C': [20,40,60,80]
                  }, 
                  index=['Row 1', 'Row 2', 'Row 3', 'Row 4'])

to_drop = 'A'



def custom_sum(row):
    return row.sum()

def remove_columns():
    return df.drop(to_drop, inplace=True, axis=1)

def filt():
    ar = df.loc[df['B'] == 10]
    return ar
    


def calculate_pow():
    df['Sum'] = df.apply(custom_sum, axis=1)
    return df

tasks = [remove_columns,filt,calculate_pow]

def executor(steps):
    for step in steps:
        df = step()
   

executor(tasks)
print(df.head())