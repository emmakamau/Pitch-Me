from email.policy import default
from unicodedata import category
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import InputRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [InputRequired()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    pitch = TextAreaField('Create a new pitch', validators=[InputRequired()],
    render_kw={"placeholder":"I’m Greg and I work for ACME Corporation. We design, build, and distribute elaborate and dangerous devices...."})
    category = SelectField('Category',choices=[('Tech','Tech'),('Sales','Sales'),('Marketing','Marketing')],default='Tech', validators=[InputRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Add a Comment', validators=[InputRequired()])
    submit = SubmitField('Submit')