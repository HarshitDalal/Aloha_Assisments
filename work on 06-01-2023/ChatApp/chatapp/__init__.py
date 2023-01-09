from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'UO_qu8aBUwxOJ7gtC-sxXgmZJ6O0pW9q'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:harshit@localhost/erp'

db = SQLAlchemy(app)

from . import routes
from . import models

