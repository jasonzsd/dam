# original dataset: 6820 records (https://www.kaggle.com/danielgrijalvas/movies)
# cleaned dataset: 4627 records

import pandas as pd
from datetime import datetime
from dateutil.parser import parse
import re
 
data_df = pd.read_csv("Data/moviesData.csv")

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
    # remove records with budget = 0
    if(row['budget'] == 0):
        tmp_index.append(index)
    # remove records with incomplete date format
    if (not bool(re.match('.+-.+-.+',row['released']))):
        tmp_index.append(index)
    # remove 2017 records
    y = pd.to_datetime(pd.Series(row['released']))
    if(int(y.dt.year) == 2017):
        tmp_index.append(index)

extracted_df.drop(tmp_index , inplace=True)

month = []
weekend = []
year = []
for index, row in extracted_df.iterrows():
    x = pd.to_datetime(pd.Series(row['released']))
    month.append(int(x.dt.month))
    year.append(int(x.dt.year))
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

#WM 1-16

    elif row['company'] in ["Cineplex Odeon Films", "Cineplex-Odeon Films"]:
        extracted_df.at[index, 'company'] = 'Cinpelex Odeon Films'
    elif "Cannon" in row['company'] and "City" not in row['company']:
        extracted_df.at[index, 'company'] = "The Cannon Group"
    elif "United Artist" in row['company']:
        extracted_df.at[index, 'company'] = "United Artists"
    elif "DreamWorks" in row['company']:
        extracted_df.at[index, 'company'] = "DreamWorks"
    elif "Vista Org" in row['company']:
        extracted_df.at[index, 'company'] = "Vista Organization"
    elif "Buena" in row['company']:
        extracted_df.at[index, 'company'] = "Buena Vista"
    elif "Disney" in row['company']:
        extracted_df.at[index, 'company'] = "The Walt Disney Company"
    elif "Warner" in row['company']:
        extracted_df.at[index, 'company'] = "Warner Bros."
    elif "Intermedia" in row['company']:
        extracted_df.at[index, 'company'] = "Intermedia Films"
    elif "Open Road" in row['company']:
        extracted_df.at[index, 'company'] = "Open Road Films"
    elif "Twentieth" in row['company']:
        extracted_df.at[index, 'company'] = "Twentieth Century Fox Film Corporation"
    elif "Canal" in row['company']:
        extracted_df.at[index, 'company'] = "StudioCanal"
    elif "Union Film" in row['company']:
        extracted_df.at[index, 'company'] = "Asian Union Film & Entertainment"
    elif "In-Gear" in row['company']:
        extracted_df.at[index, 'company'] = "In-Gear Film"

#SD 17-32

    if 'Yari Film' in row ['company']:
        extracted_df.at[index,'company'] = 'Yari Film Group'
    if 'Carolco' in row ['company']:
        extracted_df.at[index,'company'] = 'Carolco Pictures'
    if 'Universal Pictures' in row ['company']:
        extracted_df.at[index,'company'] = 'Universal Pictures'
    if 'Atlas' in row ['company']:
        extracted_df.at[index,'company'] = 'Atlas'
    if 'Avenue Pictures' in row ['company']:
        extracted_df.at[index,'company'] = 'Avenue Pictures'
    if 'Paramount' in row ['company']:
        extracted_df.at[index,'company'] = 'Paramount Pictures'
    if 'CBS' in row ['company']:
        extracted_df.at[index,'company'] = 'CBS Films'
    if 'American Playhouse' in row ['company']:
        extracted_df.at[index,'company'] = 'American Playhouse'
    if 'Sony Pictures' in row ['company']:
        extracted_df.at[index,'company'] = 'Sony Pictures'
    if 'Alliance' in row ['company']:
        extracted_df.at[index,'company'] = 'Alliance'
    if 'Cecchi Gori' in row ['company']:
        extracted_df.at[index,'company'] = 'Cecchi Gori Group'
    if ('Lionsgate' and 'Lions Gate') in row ['company']:
        extracted_df.at[index,'company'] = 'Lionsgate'
    if 'China Film' in row ['company']:
        extracted_df.at[index,'company'] = 'China Film Group Corporation'
    if 'Six Entertainment' in row ['company']:
        extracted_df.at[index,'company'] = 'Six Entertainment'
    if 'TriStar' in row ['company']:
        extracted_df.at[index,'company'] = 'TriStar Pictures'


extracted_df['month'] = month
extracted_df['isweekend'] = weekend
extracted_df['year'] = year


extracted_df.to_csv(r'C:\Users\jason\Desktop\cz4032 Data Analytic Mining\Data\CleanMovieData.csv')
