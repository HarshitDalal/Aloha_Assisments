from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, SubmitField


class DataForm(FlaskForm):
    sender = StringField('Sender', validators=(DataRequired(), Length(min=3, max=20)))
    receiver = StringField('Receiver', validators=(DataRequired(), Length(min=3, max=20)))
    msg = StringField('Message', validators=(DataRequired(), Length(min=1, max=125)))
    send = SubmitField('Send')
