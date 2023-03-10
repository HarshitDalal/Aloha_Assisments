from flask_socketio import join_room

from . import app, socketio
from flask import render_template, url_for, redirect, request
from .forms import LoginForm, RegisterForm


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.html')


@app.route('/chat')
def chat():
    username = request.args.get('username')
    room = request.args.get('room')

    if username and room:
        return render_template('chat.html', username=username, room=room)
    else:
        return redirect(url_for('home'))


@socketio.on('join_room')
def handle_join_room_event(data):
    # app.logger.info(f"{data['username']} has joined the room {data['room']}")
    print(type(data))
    join_room(data['room'])
    socketio.emit('join_room_announcement', data, room=data['room'])


@socketio.on('send_message')
def handle_send_message_event(data):
    # app.logger.info(f"{data['username']} has sent message to the room { data['room']}: {data['message']}")
    socketio.emit('receive_message', data, room=data['room'])



