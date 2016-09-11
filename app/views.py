from flask import render_template, request, redirect, url_for
from app import app
from app import t
from twython import Twython
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
  if len(request.form['hashtag']) == 0:
    return redirect(url_for('submit'))
  elif request.form['hashtag'][0] == "#":
    hasht = request.form['hashtag'][1:]
  else:
    hasht = request.form['hashtag']

  lat = request.form['lat']
  lng = request.form['lng']


  search_results = t.search(q="%23" + hasht, result_type='recent', count=20)

  str_id_list = []
  for tweet in search_results["statuses"]:
    str_id_list.append(tweet["id_str"])

  return render_template('map.html', form=form, hasht=hasht, lat=lat, lng=lng, search_results=str_id_list)






