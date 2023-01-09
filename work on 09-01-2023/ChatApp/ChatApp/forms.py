from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField, PasswordField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=(DataRequired(), Length(min=3, max=20)))
    email = EmailField('Email', validators=(DataRequired(), Length(max=50)))
    password = PasswordField('Password', validators=(DataRequired(), Length(min=8)))
    send = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=(DataRequired(), Length(min=3, max=20)))
    email = EmailField('Email', validators=(DataRequired(), Length(max=50)))
    password = PasswordField('Password', validators=(DataRequired(), Length(min=8)))
    conf_pass = PasswordField('Confirm Password', validators=(DataRequired(), Length(min=8)))
    send = SubmitField('Sign Up')
