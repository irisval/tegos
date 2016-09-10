from flask import Flask
from twython import Twython
app = Flask(__name__)

# move token keys to separate file later on

t = Twython(app_key='LA8IrKYhdTdXUH5nqFBy69Kco',
                      app_secret='wwrwJ5X9Xm5vkezNKPIldk01v55EYCeH2Bm3D9LTPkJ3ULjDn4',
                      oauth_token='769617056903888896-mWY2IgT1rCcT2v66v0DaFkE5UDnalcK',
                      oauth_token_secret='pmSmcgGMhUi3VWWTXSrxlhVXuu5BHEOhjf1hMhbuGwtn1')


app.config.from_object('config')



from app import views




