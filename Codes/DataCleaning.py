import pandas as pd
from datetime import datetime
from dateutil.parser import parse

data_df = pd.read_csv("Data/RawMoviesData.csv")

extracted_df = data_df.loc[: ,['name', 'gross', 'runtime', 'budget', 'score', 'genre', 'votes', 'year', 'director', 'rating','released', 'star', 'writer', 'company']]

tmp = []
tmp_index = []
for index, row in extracted_df.iterrows():
    if(row['gross'] >= 1000 and row['gross'] < 1000000):
        tmp.append('1')
    elif (row['gross'] >= 1000000 and row['gross'] < 10000000):
        tmp.append('2')
    elif (row['gross'] >= 10000000 and row['gross'] < 100000000):
        tmp.append('3')
    elif (row['gross'] >= 100000000 and row['gross'] < 1000000000):
        tmp.append('4')
    else:
        tmp_index.append(index)



extracted_df.drop( tmp_index , inplace=True)
extracted_df['gross_bin'] = tmp

tmp_index = []
for index, row in extracted_df.iterrows():
    if(row['budget'] == 0):
        tmp_index.append(index)

extracted_df.drop(tmp_index , inplace=True)

month = []
weekend = []
year = []
for index, row in extracted_df.iterrows():
    x = pd.to_datetime(pd.Series(row['released']))
    month.append(int(x.dt.month))
    year.append(x.dt.year)
    y = int(x.dt.weekday + 1)
    if  y < 6 :
        weekend.append(0)
    else:
        weekend.append(1)

    if row['rating'] == 'UNRATED' or row['rating'] == 'NOT RATED' or row['rating'] == 'Not specified':
        extracted_df.at[index,'rating'] = 'Nil'
    if 'Columbia Pictures' in row['company']:
        extracted_df.at[index,'company'] = 'Columbia Pictures'
    if 'BBC' in row['company']:
        extracted_df.at[index,'company'] = 'BBC'




extracted_df['month'] = month
extracted_df['isweekend'] = weekend
extracted_df['year'] = year


extracted_df.to_csv(r'C:\Users\reywe\OneDrive\Desktop\CleanMovieData.csv')
