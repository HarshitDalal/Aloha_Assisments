from flask import Flask


app = Flask(__name__)
app.secret_key = '2811679f69efaee6de35c9c1b2bc3cb46adc696724204be885c7f8fa9a20a854'

from . import forms, routes

