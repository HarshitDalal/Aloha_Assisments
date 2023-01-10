from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, DateField, IntegerField
from wtforms.validators import DataRequired, Length


class ERPForm(FlaskForm):
    fullname = StringField('Full Name', validators=(DataRequired(), Length(min=3, max=50)))
    email = EmailField('Email', validators=(DataRequired(), Length(min=8, max=150)))
    phone = StringField('Phone', validators=(DataRequired(), Length(min=10, max=13)))
    pos = StringField('Position', validators=(DataRequired(), Length(min=2, max=20)))
    dob = DateField('Date of Birth')
    company = StringField('Company Name', validators=(DataRequired(), Length(min=2, max=30)))
    address = StringField('Address', validators=(DataRequired(), Length(min=5, max=200)))
    save = SubmitField('Save')
