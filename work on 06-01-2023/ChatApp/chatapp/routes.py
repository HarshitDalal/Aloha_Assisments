from flask import render_template, url_for
from .forms import DataForm
from . import app
from .models import Data
from . import db


@app.route('/harry', methods=['POST', 'GET'])
def harry():
    form = DataForm()
    if form.validate_on_submit():
        dt = Data(form.sender.data, form.receiver.data, form.msg.data)
        db.session.add(dt)
        db.session.commit()
    return render_template('harry.html', form=form, fsend='Harry', freceive='Kapu')


@app.route('/kapu', methods=['POST', 'GET'])
def kapu():
    form = DataForm()
    return render_template('kapu.html', form=form, fsend='Kapu', freceive='Harry')

