from flask import render_template
from app import app
from .forms import FilterForm


@app.route('/')
@app.route('/index')
def index():
   return "placeholder"


@app.route('/submit', methods=['GET', 'POST'])
def submit_fields():
    form = FilterForm()
    hasht = form.hashtag.data
    loc = form.location.data

    return render_template('login.html', form=form)
