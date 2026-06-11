# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 14:45:20 2026

@author: t.daniel12299
"""

import pandas as pd
import numpy as np
import datetime
from sklearn.preprocessing import MultiLabelBinarizer
import ast
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification



##### defininf the top 25% of successful games

df= pd.read_csv("cleanedData.csv")

activeGames = df[df['Recommendations'] > 0]
threshold = activeGames['Recommendations'].quantile(.75)

df['Success'] = (
    df['Recommendations'] >= threshold
).astype(int)

##### feature engineering to include game age, log price, and languages

df['Release date'] = pd.to_datetime(df["Release date"])
currentYear = datetime.date.today().year
df['Release year'] = (df['Release date'].dt.year.fillna('').astype(int))
df['Game age'] = currentYear - df['Release year']

df['LogPrice'] = np.log1p(df['Price'])

df["Total supported languages"] = np.where(
    df['Supported languages'].fillna('').isin(['', '[]']),
    0,
    df['Supported languages'].str.count(',') + 1
)


##### convert genres to features

df['Clean Genres'] = df['Clean Genres'].apply(ast.literal_eval)  #since i downloaded to csv, the cleaned ones turned into strs
df['Clean Categories'] = df['Clean Categories'].apply(ast.literal_eval) #ast evaluates it and changes the datatype to list

genre_mlb = MultiLabelBinarizer()  #kinda like dummybins but for multi-categories
genre_df = pd.DataFrame(
    genre_mlb.fit_transform(df['Clean Genres']),
    columns=genre_mlb.classes_,
    index=df.index
)
cat_mlb = MultiLabelBinarizer()
cat_df = pd.DataFrame(
    cat_mlb.fit_transform(df['Clean Categories']),
    columns=cat_mlb.classes_,
    index=df.index
)

##### relevant columns

df_model = df[[
    "Required age", "Game age", "LogPrice", "Total supported languages"
    ]]

X = pd.concat(
    [
        df_model,
        genre_df,
        cat_df
    ],
    axis=1
)
y = df['Success']

#print(X.isnull().sum().sum()) make sure this is 0 before modelling
#print(y.value_counts()) this is making sure that the y values are balanced for the top 25 percentile

##### test, train split wit the features and the targets

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

##### Logistical Regression

model = LogisticRegression(
    random_state=42, max_iter=1000
)
model.fit(X_train, y_train)
model.predict(X_test)
model.predict_proba(X_test[:5])
model.score(X_test, y_test) # make sure data is trained on unseen values

coef_df = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_[0]
})

coef_df.sort_values(
    by='Coefficient',
    ascending=False
).head(n=30) #list the coefficients that show the likelihood of success

##### random forest classifer





















