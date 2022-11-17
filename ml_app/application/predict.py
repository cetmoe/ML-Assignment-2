
import numpy as np
import pandas as pd

import joblib
import transformer_module

pipeline = joblib.load('models/pipeline.joblib')
model = joblib.load('models/model.joblib')

genres = {
    'crime': 'Crime',
    'history': 'History',
    'family': 'Family',
    'horror': 'Horror',
    'thriller': 'Thriller',
    'foreign': 'Foreign',
    'fantasy': 'Fantasy',
    'music': 'Music',
    'action': 'Action',
    'romance': 'Romance',
    'documentary': 'Documentary',
    'comedy': 'Comedy',
    'tvmovie': 'TV Movie',
    'war': 'War',
    'animation': 'Animation',
    'drama': 'Drama',
    'sciencefiction': 'Science Fiction',
    'western': 'Western',
    'adventure': 'Adventure',
    'mystery: ': 'Mystery'
}


def get_form_data(data):

    feature_values = {
        'id': 0,
        'belongs_to_collection': None,
        'budget': 1000000,
        'genres': [],
        'homepage': None,
        'imdb_id': 1,
        'original_language': 'en',
        'original_title': 'The Dark Knight',
        'overview': 'The Dark Knight',
        'popularity': 3,
        'poster_path': '',
        'production_companies': [{'id': 1, 'name': 'Warner Bros.'}],
        'production_countries': [{'iso_3166_1': 'US', 'name': 'United States of America'}],
        'release_date': '05/01/15',
        'runtime': 100,
        'spoken_languages': [{'iso_639_1': 'en', 'name': 'English'}],
        'status': 'Released',
        'tagline': None,
        'title': 'The Dark Knight',
        'Keywords': None,
        'cast': None,
        'crew': None
    }

    key_features = [
        'production_companies',
        'production_countries',
    ]

    for key in [k for k in data.keys() if k in feature_values]:
        if key in key_features:
            seperate = data[key].split(',')
            list_of_names = []

            for i in seperate:
                list_of_names.append({'name': i})

            feature_values[key] = str(list_of_names)
        else:
            feature_values[key] = data[key]

    for genre in genres.keys():
        if genre in data and data[genre] == True:
            feature_values['genres'].append({'name': genres[genre]})

    feature_values['genres'] = str(feature_values['genres'])

    return feature_values


def predict(data):
    features = get_form_data(data)

    column_order = ['id', 'belongs_to_collection', 'budget', 'genres', 'homepage',
                    'imdb_id', 'original_language', 'original_title', 'overview',
                    'popularity', 'poster_path', 'production_companies',
                    'production_countries', 'release_date', 'runtime', 'spoken_languages',
                    'status', 'tagline', 'title', 'Keywords', 'cast', 'crew']

    df = pd.DataFrame([features], columns=column_order)

    prediction_set = pipeline.transform(df)

    prediction = model.predict(prediction_set)

    return prediction[0]
