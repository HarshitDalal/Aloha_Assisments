from flask import Flask
from flask_socketio import SocketIO
from . import forms

app = Flask(__name__)
app.config['SECRET_KEY'] = '91a9aef87f2330c8325838dc30aeff262ce3ff0a913f11df839b6a387426fa41'
socketio = SocketIO(app)


from . import routes
