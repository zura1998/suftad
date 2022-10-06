from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, PasswordField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email, Length
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField(label="Name:", validators=[DataRequired(), Length(min=4, max=24)])
    email = EmailField(label="Email address:", validators=[Email()])
    password = PasswordField(label="Password:")
    confirm_password = PasswordField(label=" Confirm Password:", validators=[EqualTo("password", message="password "
                                                                                                         "don't match")])

    submit = SubmitField(label="Submit")

    def validate_email_from_db(self):
        temp_email = self.email.data
        if User.find_by_email(temp_email):
            return False
        else:
            return True
            # raise ValueError('Email already exists')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
