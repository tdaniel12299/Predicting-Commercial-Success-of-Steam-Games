# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 14:45:20 2026

@author: t.daniel12299
"""

import pandas as pd
import numpy as np
import datetime



##### defininf the top 25% of successful games

df= pd.read_csv("cleanedData.csv")

activeGames = df[df['Recommendations'] > 0]
threshold = activeGames['Recommendations'].quantile(.75)

df['Success'] = (
    df['Recommendations'] >= threshold
).astype(int)

##### feature engineering to include game age, log price

df['Release date'] = pd.to_datetime(df["Release date"])
currentYear = datetime.date.today().year
df['Release year'] = (df['Release date'].dt.year.fillna('').astype(int))
df['Game age'] = currentYear - df['Release year']

df['LogPrice'] = np.log1p(df['Price'])
