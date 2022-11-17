from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, BooleanField, SubmitField

from wtforms.validators import DataRequired, Length, NumberRange, Optional


class DataForm(FlaskForm):
    """Form for user input."""
    belongs_to_collection = StringField(
        'Is the movie in a collection? if so which', validators=[Optional()])
    budget = IntegerField('Budget', validators=[DataRequired()])
    production_companies = StringField(
        'Production Companies (comma seperated)', validators=[Optional()])
    production_countries = StringField(
        'Production Countries (comma seperated)', validators=[Optional()])
    original_language = StringField(
        'Original language (en, es, hi...):', validators=[DataRequired()])
    release_date = StringField('Release date:', validators=[DataRequired()])
    runtime = IntegerField('Runtime', validators=[DataRequired()])
    homepage = StringField('Homepage', validators=[Optional()])
    tagline = StringField('Tagline', validators=[Optional()])
    Keywords = StringField('Keywords', validators=[Optional()])

    crime = BooleanField('Crime')
    history = BooleanField('History')
    family = BooleanField('Family')
    horror = BooleanField('Horror')
    thriller = BooleanField('Thriller')
    foreign = BooleanField('Foreign')
    fantasy = BooleanField('Fantasy')
    music = BooleanField('Music')
    action = BooleanField('Action')
    romance = BooleanField('Romance')
    documentary = BooleanField('Documentary')
    comedy = BooleanField('Comedy')
    tvMovie = BooleanField('TvMovie')
    war = BooleanField('War')
    animation = BooleanField('Animation')
    drama = BooleanField('Drama')
    scienceFiction = BooleanField('ScienceFiction')
    western = BooleanField('Western')
    adventure = BooleanField('Adventure')
    mystery = BooleanField('Mystery')

    submit = SubmitField('Submit')

    # belongs_to_collection = BooleanField(
    #     'Does this movie belong to a collection?')
    # budget = IntegerField('Budget', validators=[DataRequired()])
    # companies = BooleanField(
    #     'Is the movie produced by one of the big 5 companies?')
    # popularity = FloatField('Popularity', validators=[DataRequired()])
    # spoken_languages = BooleanField(
    #     'Does the movie have a version in either English, French, Spanish, German or Russian?')
    # release_year = IntegerField('Release year', validators=[
    #                             DataRequired(), NumberRange(min=1900, max=2025)])
    # quarter = IntegerField('Quarter', validators=[
    #                        DataRequired(), NumberRange(min=1, max=4)])
    # runtime = IntegerField('Runtime', validators=[DataRequired()])

    # originalEnglish = BooleanField('Is the original language English?')
    # originalFrench = BooleanField('Is the original language French?')
    # originalSpanish = BooleanField('Is the original language Spanish?')
    # originalRussian = BooleanField('Is the original language Russian?')
    # originalHindi = BooleanField('Is the original language Hindi?')

    # hasHomepage = BooleanField('Does the movie have a homepage?')
    # hasTagline = BooleanField('Does the movie have a tagline?')
    # hasKeywords = BooleanField('Does the movie have keywords?')

    # producedInTop5Countries = BooleanField(
    #     'Is the movie produced in USA, UK, France, Germany, Canada?')
