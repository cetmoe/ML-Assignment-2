
import numpy as np
import pandas as pd

import joblib
from pipeline_functions import *

# pipeline = joblib.load('models/pipeline.joblib')
model = joblib.load('models/model.joblib')


def get_form_data(data):

    feature_values = {
        'id',
        'belongs_to_collection',
        'budget',
        'genres',
        'homepage',
        'imdb_id',
        'original_language',
        'original_title',
        'overview',
        'popularity',
        'poster_path',
        'production_companies',
        'production_countries',
        'release_date',
        'runtime',
        'spoken_languages',
        'status',
        'tagline',
        'title',
        'Keywords',
        'cast',
        'crew',
        'revenue'
    }

    for key in [k for k in data.keys() if k in feature_values]:
        feature_values[key] = data[key]

    return feature_values


def predict(data):
    print(data)
