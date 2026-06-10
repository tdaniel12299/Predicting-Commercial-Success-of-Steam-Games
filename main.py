import pandas as pd

df = pd.read_csv("games.csv", names=[
    'AppID', 'Name', 'Release date', 'Estimated owners',
           'Peak CCU', 'Required age', 'Price', 'DiscountDLC count','unknown',
           'About the game', 'Supported languages', 'Full audio languages',
           'Reviews', 'Header image', 'Website', 'Support url', 'Support email',
           'Windows', 'Mac', 'Linux', 'Metacritic score', 'Metacritic url',
           'User score', 'Positive', 'Negative', 'Score rank', 'Achievements',
           'Recommendations', 'Notes', 'Average playtime forever',
           'Average playtime two weeks', 'Median playtime forever',
           'Median playtime two weeks', 'Developers', 'Publishers', 'Categories',
           'Genres', 'Tags', 'Screenshots', 'Movies'
    ])

####### split tags

df['Clean Tags'] = (
    df['Tags']
    .fillna('')
    .apply(lambda x: [tag.strip() for tag in x.split(',') if tag.strip()])
)
df['Clean Categories'] = (
    df['Categories']
    .fillna('')
    .apply(lambda x: [tag.strip() for tag in x.split(',') if tag.strip()])
)
df['Clean Genres'] = (
    df['Genres']
    .fillna('')
    .apply(lambda x: [tag.strip() for tag in x.split(',') if tag.strip()])
)

df = df.reset_index()
df.drop(0, inplace=True)
df.drop(columns=['index','unknown','Movies','Screenshots','Metacritic url'], inplace = True)

###### fix data types for columns

df['Price'] = pd.to_numeric(df["Price"])
df['AppID'] = pd.to_numeric(df["AppID"])
df['Estimated owners'] = df['Estimated owners'].astype('category')
df['Peak CCU'] = pd.to_numeric(df["Peak CCU"])
df['Required age'] = pd.to_numeric(df["Required age"])
df['DiscountDLC count'] = pd.to_numeric(df["DiscountDLC count"])
df['Achievements'] = pd.to_numeric(df["Achievements"])
df['Average playtime forever'] = pd.to_numeric(df["Average playtime forever"])
df['Average playtime two weeks'] = pd.to_numeric(df["Average playtime two weeks"])
df['Median playtime forever'] = pd.to_numeric(df["Median playtime forever"])
df['Median playtime two weeks'] = pd.to_numeric(df["Median playtime two weeks"])
df['Recommendations'] = pd.to_numeric(df["Recommendations"])

###### drop nan

df_cleaned = df.dropna(subset=['About the game'])
#df_cleaned.to_csv("cleanedData.csv", index = False)

print(df.info())