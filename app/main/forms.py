from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from wtforms.validators import InputRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [InputRequired()])
    submit = SubmitField('Submit')