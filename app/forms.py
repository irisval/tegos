from flask_wtf import Form
from wtforms import TextField, StringField
from wtforms.validators import DataRequired

class FilterForm(Form):
	hashtag = StringField('Hashtag', validators=[DataRequired()])
	location = StringField('Location', validators=[DataRequired()])

	