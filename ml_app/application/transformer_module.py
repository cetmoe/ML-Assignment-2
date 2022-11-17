from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd

largest_movie_companies = [
    'Warner Bros.',                             # Warner Bros. Entertainment
    'Universal Pictures',                       # NBCUniversal
    'Paramount Pictures',                       # Paramount Global
    'Twentieth Century Fox Film Corporation',   # Walt Disney Studios
    'Columbia Pictures',                        # Sony Pictures
    'Metro-Goldwyn-Mayer (MGM)',                # Amazon
    'New Line Cinema',                          # Warner Bros. Entertainment
    'Touchstone Pictures',                      # Walt Disney Studios
    'Walt Disney Pictures',                     # Walt Disney Studios
    'Columbia Pictures Corporation',            # Sony Pictures
    'TriStar Pictures'                          # Sony Pictures
]

top5_spoken_languages = [
    'English',
    'Français',
    'Español',
    'Deutsch',
    'Pусский'
]

top5_original_languages = [
    'en',
    'fr',
    'ru',
    'es',
    'hi'
]

top5_production_countries = [
    'United States of America',
    'United Kingdom',
    'France',
    'Germany',
    'Canada'
]

genres = [
    'Crime',
    'History',
    'Family',
    'Horror',
    'Thriller',
    'Foreign',
    'Fantasy',
    'Music',
    'Action',
    'Romance',
    'Documentary',
    'Comedy',
    'TV Movie',
    'War',
    'Animation',
    'Drama',
    'Science Fiction',
    'Western',
    'Adventure',
    'Mystery'
]


def m_eval(x):
    try:
        out = eval(x)
    except:
        out = {}
    return out


def dictEncode(dataframe, column, key, categories, oneHot=True, destColumn=None):
    if oneHot == False and destColumn == None:
        raise Exception(
            'You must have a destination column if oneHot is set to False.')

    # Inserts new columns into the dataframe
    # if oneHot then add all categories, else add targetColumn
    if oneHot:
        for category in categories:
            dataframe.insert(len(dataframe.columns), category, 0)
    else:
        dataframe.insert(len(dataframe.columns), destColumn, 0)

    # loops through all the rows
    # if oneHot, then set each respective category to 1, else set targetColumn to 1
    for index, row in dataframe.iterrows():
        # reads string of form '{'name':'value'}' to dictionary
        dictionary = m_eval(row[column])

        # creates a list of every element of a particular key
        elements = list(map(lambda x: x[key], dictionary))

        for element in elements:
            if element in categories:
                if oneHot:
                    dataframe.at[index, element] = 1
                else:
                    dataframe.at[index, destColumn] = 1


def containOrNot(df, columnName, addedName=''):
    df[addedName + columnName] = df[columnName].notnull().astype('int')
    if addedName != '':
        df.drop(columnName, inplace=True, axis=1)


def rdConversion(dataframe):
    data = dataframe.copy()
    data['release_date'] = data['release_date'].fillna('01/01/01')
    data['release_date'] = pd.to_datetime(data['release_date'])
    data['year'] = data['release_date'].dt.year

    for i in range(1, 5):
        data.insert(len(data.columns), f'quarter_{i}', 0)

    for index, row in data.iterrows():
        quarter = row['release_date'].quarter
        if 1 <= quarter and quarter <= 4:
            data.at[index, f'quarter_{quarter}'] = 1

    return data


class CustomTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        if set(['status', 'crew', 'cast', 'overview', 'poster_path', 'imdb_id', 'title', 'original_title']).issubset(X.columns):
            X.drop(['status', 'crew', 'cast', 'overview', 'poster_path',
                   'imdb_id', 'title', 'original_title'], inplace=True, axis=1)

        dictEncode(X, 'genres', 'name', genres)
        dictEncode(X, 'production_countries',
                   'name', top5_production_countries)
        dictEncode(X, 'production_companies', 'name', largest_movie_companies,
                   oneHot=False, destColumn='top_movie_companies')
        dictEncode(X, 'spoken_languages', 'name', top5_spoken_languages,
                   oneHot=False, destColumn='top5_spoken_languages')

        for org in top5_original_languages:
            X.insert(len(X.columns), 'org_' + org, 0)

        for index, row in X.iterrows():
            if row['original_language'] in top5_original_languages:
                X.at[index, 'org_' + row['original_language']] = 1

        containOrNot(X, 'homepage', 'has_')
        containOrNot(X, 'belongs_to_collection')
        containOrNot(X, 'tagline', 'has_')
        containOrNot(X, 'Keywords', 'has_')

        rdConversion(X)
        X.drop('release_date', inplace=True, axis=1)
        X.drop(['genres', 'production_countries', 'production_companies',
               'spoken_languages', 'original_language'], inplace=True, axis=1)

        return X
