from flask_wtf import FlaskForm
from wtforms.fields import StringField, FileField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from ..models import Event, Image
