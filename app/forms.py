from flask_wtf import Form
from wtforms import TextField, StringField, BooleanField
from wtforms.validators import DataRequired

class FilterForm(Form):
	hashtag = StringField('Hashtag', validators=[DataRequired()])
	location = StringField('Location', validators=[DataRequired()])
	mapDisplay = BooleanField('Area Choice', description="Show data specific to your current location?", validators=[DataRequired()])

	