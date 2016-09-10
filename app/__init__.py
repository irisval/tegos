from flask import Flask
from twython import Twython
app = Flask(__name__)
# move creds to config file later on
# app.config.setdefault('TWEEPY_CONSUMER_KEY', 'LA8IrKYhdTdXUH5nqFBy69Kco')
# app.config.setdefault('TWEEPY_CONSUMER_SECRET', 'wwrwJ5X9Xm5vkezNKPIldk01v55EYCeH2Bm3D9LTPkJ3ULjDn4')
# app.config.setdefault('TWEEPY_ACCESS_TOKEN_KEY', 'pmSmcgGMhUi3VWWTXSrxlhVXuu5BHEOhjf1hMhbuGwtn1')
# app.config.setdefault('TWEEPY_ACCESS_TOKEN_SECRET', 'wwrwJ5X9Xm5vkezNKPIldk01v55EYCeH2Bm3D9LTPkJ3ULjDn4')

t = Twython(app_key='LA8IrKYhdTdXUH5nqFBy69Kco',
                      app_secret='wwrwJ5X9Xm5vkezNKPIldk01v55EYCeH2Bm3D9LTPkJ3ULjDn4',
                      oauth_token='769617056903888896-mWY2IgT1rCcT2v66v0DaFkE5UDnalcK',
                      oauth_token_secret='pmSmcgGMhUi3VWWTXSrxlhVXuu5BHEOhjf1hMhbuGwtn1')


app.config.from_object('config')



from app import views




