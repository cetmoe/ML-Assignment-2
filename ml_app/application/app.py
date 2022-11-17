from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from forms import DataForm

from predict import predict

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'DAT158'


@app.route("/", methods=['GET', 'POST'])
def index():

    form = DataForm()
    if form.validate_on_submit():
        for fieldname, value in form.data.items():
            session[fieldname] = value

        pred = predict(session)
        session['prediction'] = pred

        return redirect(url_for('index'))

    return render_template('index.jinja', form=form)
