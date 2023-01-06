from flask import Flask, render_template, url_for, redirect
from forms import EntryDataFrom

app = Flask(__name__)

app.config['SECRET_KEY'] = 'UO_qu8aBUwxOJ7gtC-sxXgmZJ6O0pW9q'


@app.route('/')
def home():
    return render_template('home.html', title='home')


@app.route('/enterdata', methods=['POST', 'GET'])
def e_data():
    form = EntryDataFrom()
    if form.validate_on_submit():
        print(f'Name : {form.name.data} , Email : {form.email.data} , Phone : {form.phone.data}')
        return redirect(url_for('home'))
    return render_template('edata.html', title='Enter Data', form=form)


if __name__ == '__main__':
    app.run(debug=True)
