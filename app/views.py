from flask import render_template, request
from app import app
from .forms import FilterForm


@app.route('/')
@app.route('/index')
def index():
   return "placeholder"


@app.route('/submit', methods=['GET', 'POST'])
def submit():
  form = FilterForm()
  return render_template('login.html', form=form)

@app.route('/display', methods=['GET', 'POST'])
def display():
  form = FilterForm()
  if request.form['hashtag'][0] == "#":
    hasht = request.form['hashtag']
  else:
    hasht = "#" + request.form['hashtag']
  loc = request.form['location']

  return render_template('map.html', form=form, hasht = hasht, loc = loc)

